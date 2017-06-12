from django.shortcuts import render,redirect
from .forms import AuthorForm,RegisterForm, BlogForm
from django.http import HttpResponse
from django.utils import timezone
from django.template import loader
from .models import Author,Post, Comments
from itertools import chain
# Create your views here.
from django.db.models.functions import Lower
mypost = None
posts = None
def index(request):
    global user
    user = None
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            try:
                author = Author.objects.get(username = form.cleaned_data['username'],password=form.cleaned_data.get('password') )
            except:
                author = None
            if(author is not None):
                user = author
                request.session['username'] = author.username
                request.session['seach'] = ''
                return redirect('home')
            else:
                return render(request, 'index.html', {'AuthorForm': form, 'check': True})
    else:
        form = AuthorForm()

    return render(request, 'index.html' ,{'AuthorForm' : form,'check':False})

def specific(request, Post_id):

    post = Post.objects.get(id = Post_id)
    if request.method == "POST":
        try:
            comment = Comments(author = Author.objects.get(username=request.session['username']), Ppost = post,cdate = timezone.now(), content = request.POST['commenty'])
            comment.save()
            print(request.POST['commenty'])
        except:
            None
    return render(request, 'key_blog.html', {'post':post,'comments':Comments.objects.filter(Ppost = post),'user': Author.objects.get(username=request.session['username'])})


def Home(request):
    posts = None
    postsa = None
    postsb = None
    postsc = None
    reversed = True
    print(request.session['username'])
    if(request.method == "POST"):
        posts = request.session['search']
        try:
            request.session['search'] = request.POST['filter']

        except:
            None
        posts = Post.objects.all()
        postsa = posts.filter(title__icontains=request.session['search'])
        postsb = posts.filter(author__first_name__icontains=request.session['search'])
        postsc = posts.filter(content__icontains=request.session['search'])

        # seta = set(postsa)
        # setb = set(postsb)
        # setc = set(postsc)
        # setb = setb - seta
        # setd = set(list(seta)+list(setb))
        # setc = setc - (setd)

        # posts =list(seta)+list(setb)+list(setc)
        posts = postsa | postsb | postsc
        postsort = []
        try:
            if (request.POST['author'] == 'author'):
                ##posts = posts.order_by('author__first_name','author__last_name')
                postsort.append('-author__first_name')
                postsort.append('-author__last_name')
                autho = True

        except:
            None
        try:
            if (request.POST['le'] == 'le'):
                ##posts = posts.order_by('edate')
                postsort.append('edate')
        except:
            None
        try:
            if (request.POST['date'] == 'date'):
                ##posts = posts.order_by('cdate')
                postsort.append('-cdate')

        except:
            None
        try:
            if (request.POST['title'] == 'title'):
                ##posts = posts.order_by('cdate')
                postsort.append('-title')
                print('beng')

        except:
            None
        print(reversed)
        posts = posts.order_by(*postsort)
    else:
        request.session['search'] = ''
        posts = Post.objects.all()
    context = {
        'posts': posts,
        'user': Author.objects.get(username=request.session['username']),
        'reveresed': reversed,
    }
    return render(request, 'Posts.html', context)

def Delete(request, Post_id):
    global user
    post = Post.objects.get(id=Post_id)
    if (Post is not None and post.author == Author.objects.get(username=request.session['username'])):
        post.delete()

    return redirect('home')
def Update(request, Post_id):
    global user
    post = Post.objects.get(id = Post_id)
    if(Post is not None and post.author == Author.objects.get(username=request.session['username'])):
        if request.method == "POST":

            post.edate=timezone.now()
            post.title=request.POST['title']
            post.content=request.POST['content']
            post.save()


            return redirect('home')


        return render(request, 'UBlog.html', {'user':  Author.objects.get(username=request.session['username']), 'post':post})
    else:
        print('not yours')
    return redirect('home')
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            author = Author(username=form.cleaned_data['username'],password=form.cleaned_data.get('password'),first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'])

            try:
                if (Author.objects.get(username = author.username)):
                    return render(request, 'Register.html',{'RegisterForm':form,'check':True})
            except:
                None
            author.save()
            request.session['username'] = author.username
            request.session['seach'] = ''
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'Register.html' ,{'RegisterForm' : form,'check':False})

def Logout(request):
    return redirect('index')

def Cblog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Post(author=Author.objects.get(username=request.session['username']), cdate=timezone.now(),edate=timezone.now(),title=form.cleaned_data['title'],content = form.cleaned_data['content'])
            post.save()
            return redirect('home')

    else:
        form = BlogForm()

    return render(request, 'CBlog.html' ,{'BlogForm' : form,'user': Author.objects.get(username=request.session['username'])})