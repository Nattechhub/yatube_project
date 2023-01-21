from django.shortcuts import render
from django.http import HttpResponse

 # Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text,
    }
#     # Третьим параметром передаём словарь context
    return render(request, template, context) 

 # посты, отфильтрованные по группам
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = f'Страница постов группы {slug}'
    context = {
        'title': title,
    }
    return render(request, template, context, slug)
#def group_posts(request, slug):    
#     template = 'posts/group_list.html'
#     group = get_object_or_404(Group, slug=slug)
#     text = f'Страница постов группы {slug}'
#     # Метод .filter позволяет ограничить поиск по критериям.
#     # Это аналог добавления
#     # условия WHERE group_id = {group_id}
#     posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
#     context = {
#         'group': group,
#         'posts': posts,
#         'text':text,
#     }
#     return render(request, template, context) 
