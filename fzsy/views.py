from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_login
from .models import Post
from .models import Post1
from .models import Post2
from .models import Post3
from .models import Post4
from .models import Yqj
from .models import syqc
from .models import Student_login
from django.shortcuts import redirect
from  datetime import datetime
from django.contrib.sessions.models import Session


# Create your views here.
def homepage(request):
    if 'username' in request.session:
        username = request.session['username']
    posts = Post.objects.order_by('id').reverse()[:5]
    posts1 = Post1.objects.all().order_by('id').reverse()[:5]
    posts2 = Post2.objects.all().order_by('id').reverse()[:5]
    posts3 = Post3.objects.all().order_by('id').reverse()[:5]
    posts4 = Post4.objects.all().order_by('id').reverse()[:5]
    yqj = Yqj.objects.all().order_by('id').reverse()
    syqc_1 = syqc.objects.all().order_by('id').reverse()
    now = datetime.now()
    return render(request, 'index.html', locals())
'''
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("NO.{}:".format(str(count))+str(post)+"<br>")
        post_lists.append("<small>"+str(post.body.encode('utf=8'))+"</small><br><br>")
    return HttpResponse(post_lists)
'''


def showpost(request, slug):
     try:
         yqj = Yqj.objects.all().order_by('id').reverse()
         syqc_1 = syqc.objects.all().order_by('id').reverse()
         post = Post.objects.get(slug=slug)
         if post != None:
             return render(request,'post.html',locals())
     except:
         return redirect('/')


def showpost1(request, slug):
    try:
        yqj = Yqj.objects.all().order_by('id').reverse()
        syqc_1 = syqc.objects.all().order_by('id').reverse()
        post = Post1.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def showpost2(request, slug):
    try:
        yqj = Yqj.objects.all().order_by('id').reverse()
        syqc_1 = syqc.objects.all().order_by('id').reverse()
        post = Post2.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def showpost3(request, slug):
    try:
        yqj = Yqj.objects.all().order_by('id').reverse()
        syqc_1 = syqc.objects.all().order_by('id').reverse()
        post = Post3.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def showpost4(request, slug):
    try:
        yqj = Yqj.objects.all().order_by('id').reverse()
        syqc_1 = syqc.objects.all().order_by('id').reverse()
        post = Post4.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def showyqj(request, slug):
    try:
        yqj = Yqj.objects.all().order_by('id').reverse()
        syqc_1 = syqc.objects.all().order_by('id').reverse()
        post = Yqj.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def showsyqc(request, slug):
    try:
        yqj = Yqj.objects.all().order_by('id').reverse()
        syqc_1 = syqc.objects.all().order_by('id').reverse()
        post = syqc.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def login(request):
    if request.method == 'POST' and request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        inDB = Student_login.objects.filter(username=username).first()
        if inDB:
            if password == inDB.password:
                result = 'success'
                request.session['username'] = username
                Student_login.objects.filter(username=username).update(logintime=inDB.logintime+1)
                return render(request,'registerlogin/login.html', {'result': result})
            else:
                result = 'error'
                return render(request,'registerlogin/login.html', {'result': result})
        else:
                result = 'none'
                return render(request,'registerlogin/login.html', {'result': result})
    return render(request,'registerlogin/login.html')


def logout(request):
    if 'username' in request.session:
        Session.objects.all().delete()
        return redirect('/')
    return redirect('/')
