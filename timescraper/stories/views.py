from django.shortcuts import render
from django.http import JsonResponse
import requests

def get_time_stories(request):
    url = "https://time.com"
    response = requests.get(url)
    html_content = response.text

    # Basic string parsing logic to extract stories
    stories = []
    start_tag = '<a href="'
    end_tag = '</a>'
    start_title = '">'

    index = 0
    while len(stories) < 6 and index != -1:
        index = html_content.find(start_tag, index)
        if index == -1:
            break
        index += len(start_tag)
        end_index = html_content.find('"', index)
        link = url + html_content[index:end_index]

        title_start = html_content.find(start_title, end_index) + len(start_title)
        title_end = html_content.find(end_tag, title_start)
        title = html_content[title_start:title_end]

        stories.append({"title": title.strip(), "link": link.strip()})
        index = title_end

    return JsonResponse(stories, safe=False)

# View for the homepage
def home(request):
    return render(request, 'index.html')

