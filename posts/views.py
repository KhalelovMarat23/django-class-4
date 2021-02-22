from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from posts import models
from django.db.models import F

import posts


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
        'posts': models.Post.objects.all().order_by('-id'),
        'categories': models.Category.objects.all().order_by('-id'),
        'tags': models.Tag.objects.all().order_by('id')
    }
    return render(request, 'post.html', data)


def getpost(request, myslug, des='get'):
    post = models.Post.objects.get(slug=myslug)
    # post.views += 1
    # post.save()
    if des == 'delete':
        models.Post.objects.filter(slug=myslug).delete()
        return redirect('/posts')
    if des == 'update':
        if request.method == 'POST':
            cat_id = request.POST.get('category')
            data = {
                "title": request.POST.get('title'),
                "description": request.POST.get('description'),
                "category": models.Category.objects.get(pk=cat_id)
            }

            # data['image'] = request.FILES.get('image') if request.FILES.get('image') is not None else None 
            
            if request.FILES.get('image') is not None:
                data['image'] = request.FILES.get('image')
                print('New File')
            
            post = models.Post.objects.filter(slug=myslug).update(**data)
            # post.tag.set(request.POST.getlist('tag'))
            return redirect('/posts')
    else:
        models.Post.objects.filter(slug=myslug).update(views=F('views') + 1)

    data = {
        'post': post
    }
    return render(request, 'detail.html', data)



def savepost(request):
    if request.method == 'POST':
        
        cat_id = request.POST.get('category')
        
        data = {
            "title": request.POST.get('title'),
            "description": request.POST.get('description'),
            "slug": request.POST.get('slug'),
            "category": models.Category.objects.get(pk=cat_id),
            "image": request.FILES.get('image')
        }
        
        post = models.Post.objects.create(**data)
        # post = models.Post(**data)
        # post.save()
        post.tag.set(request.POST.getlist('tag'))
        
        return redirect('/posts')
    return HttpResponse('GET')


def get_post_json(request, myslug):
    post = models.Post.objects.filter(slug=myslug)
    
    response = {
        'title': post[0].title,
        'description': post[0].description,
        'slug': post[0].slug,
        'category': post[0].category.pk,
        'tag': list(post.values_list('tag', flat=True)),
        'image': post[0].image.name
    }
    
    return JsonResponse(response)





def main_page(request):
    
    catid = 0
    
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    
    posts = models.Post.objects.filter(title__contains=q).order_by('-id').select_related('category')
    
    if 'catid' in request.GET and request.GET.get('catid') != '0':
        catid = request.GET.get('catid')
        posts = models.Post.objects.filter(category=catid).order_by('-id').select_related('category')
    
    data = {
        'posts': posts,
        'categories': models.Category.objects.all().order_by('id'),
        'tags': models.Tag.objects.all().order_by('id')
    }
    
    return render(request, 'main.html', data)