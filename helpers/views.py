from django.shortcuts import render

def page_not_found(request, exception):
    print('hello error')
    return render(request, '404.html')