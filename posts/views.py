from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts import models
from django.db.models import F


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




def getposts(request):
    data = {
        'posts': models.Post.objects.all().order_by('id')
    }
    return render(request, 'post.html', data)


def getpost(request, myslug, des='get'):
    post = models.Post.objects.get(slug=myslug)
    # post.views += 1
    # post.save()
    if des == 'delete':
        models.Post.objects.filter(slug=myslug).delete()
        return redirect('/posts')
    else:
        models.Post.objects.filter(slug=myslug).update(views=F('views') + 1)

    data = {
        'post': post
    }
    return render(request, 'detail.html', data)