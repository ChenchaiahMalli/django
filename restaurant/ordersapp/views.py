from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    
    data={
        'title':'Hello this is my page',
        'homename': 'Malli Chenchaiah (Full stack developer)',
        'list':['PYTHON','DJANGO','MYSQL','HTML','CSS','JAVASCRIPT'],
        'student_details':[{'name':'Malli','phone':'8978648730','gender':'male','marks':'40'},
                           {'name':'Karna','phone':'6303836411','gender':'male','marks':'30'}]
    }
    return render(request,'demo.html',data)