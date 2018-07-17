from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse, \
    FileResponse
from books.models import Book
from django.core.mail import send_mail
import json

# Create your views here.
def hello(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknow')
    return HttpResponse("Your browser is {}".format(ua))

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_form.html', {'books': books,
                                                           'query': q})

    return render_to_response('search_form.html', {'error': errors})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(request.POST['subject'],
                      request.POST['message'],
                      request.POST.get('email', 'noreply@example.com'),
                      ['siteowner@example.com'])
            return HttpResponse('')

    return render_to_response('contact_form.html', {'errors': errors})

def download_image(request):
    """文件下载方式一"""
    with open('C:/Users/kioij/Desktop/dog.jpg', 'rb') as f:
        c = f.read()

    response = HttpResponse(c)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={}'.format('dog.jpg')
    return response

def download_image1(request):
    """文件下载方式二"""
    file = open('C:/Users/kioij/Desktop/dog.jpg', 'rb')
    response = StreamingHttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={}'.format('dog.jpg')
    return response

# 推荐使用
def download_image2(request):
    """文件下载方式三"""
    file = open('C:/Users/kioij/Desktop/dog.jpg', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename={}'.format('dog.jpg')
    return response

def jsondata(request):
    """返回json格式数据"""
    data = {
        'code': 0,
        'msg': 'hello world'
    }
    return HttpResponse(json.dumps(data), content_type="application/json")