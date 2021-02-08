from django.shortcuts import render
from django.http import HttpResponse
from posts import models

def main(request):
    return HttpResponse('<h1>Hello This is my first Django page</h1>')

def second(request):
    output = """
        <h1>Hello Second Page render from string</h1>
        <p>Some description about this page</p>
        <a href="/">Main Page</a>
    """
    return HttpResponse(output)


"""
    ModelName.objects.all() - SELECT * FROM table_name;

"""

def html_file(request):

    data = {
        'name': 'Yedil',
        'skills': ['Django', 'HTML', 'CSS'],
        'vehicle': {
            'car': 'Toyota',
            'moto': 'Suzuki',
        },
        'posts': models.Post.objects.all()
    }


    return render(request, 'cv.html', data)