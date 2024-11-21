from django.http import Http404
from django.shortcuts import render
from blog.data import posts


def blog(request):
    print('blog')
    return render(
        request,
        'blog/index.html',
        context = {
            'title' : 'Blog - ',
            'h1' : 'Página do blog',
            'posts' : posts
        }
    )
    
def post(request, post_id):
    found_post = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
        
    if found_post is None:
        raise Http404('Post não existe.')
    
    
    
    return render(
        request,
        'blog/post.html',
        context = {
            'title' : found_post['title'] + ' - ',
            'h1' : 'Página do blog',
            'post' : found_post
        }
    )
    
def example(request):
    print('exemplo')
    return render(
        request,
        'blog/example.html',
        context = {
            'title' : 'Exemplo - ',
            'h1' : 'Página de exemplo'
        }
    )
