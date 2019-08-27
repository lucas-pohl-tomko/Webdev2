from datetime import datetime

from django.contrib.auth.models import User
from django.http import cookie
from django.shortcuts import (
    get_object_or_404, redirect, render, HttpResponse
)
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from app.forms import EditProfileForm, EditUserForm, PostForm, DocumentForm
from app.models import Post, Profile, Document, Letra

from django.forms import ModelForm


class LetraForm(ModelForm):
    class Meta:
        model = Letra
        fields = ['name', 'letra']


class PostCreate(CreateView):
    model = Post
    fields = ['body']


class PostUpdate(UpdateView):
    model = Post
    fields = ['body']


class UserProfile(View):
    template_name = 'users/user.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(username=self.kwargs['username']).first()
        profile = Profile.objects.filter(user=user).first()
        posts = Post.objects.filter(author=user)
        following = request.user.is_following(user)
        return render(request, self.template_name, {
            'user': user,
            'profile': profile,
            'posts': posts,
            'following': following,
        })


class UserFollow(View):
    template_name = 'users/user.html'

    def get(self, request, *args, **kwargs):
        user_follower = User.objects.filter(
            username=self.kwargs['follower']).first()
        user_followed = User.objects.filter(
            username=self.kwargs['followed']).first()
        user_follower.follow(user_followed)

        profile = Profile.objects.filter(user=user_follower).first()
        posts = Post.objects.filter(author=user_follower)
        return render(request, self.template_name, {
            'user': user_follower,
            'profile': profile,
            'posts': posts,
        })


class UserUnfollow(View):
    template_name = 'users/user.html'

    def get(self, request, *args, **kwargs):
        user_follower = User.objects.filter(
            username=self.kwargs['follower']).first()
        user_followed = User.objects.filter(
            username=self.kwargs['followed']).first()
        user_follower.unfollow(user_followed)

        profile = Profile.objects.filter(user=user_follower).first()
        posts = Post.objects.filter(author=user_follower)
        return render(request, self.template_name, {
            'user': user_follower,
            'profile': profile,
            'posts': posts,
        })


class UserProfileEditAdmin(View):
    template_name = 'users/edit_user.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(username=self.kwargs['username']).first()
        profile = Profile.objects.filter(user=user).first()
        user_form = EditUserForm(instance=user)
        profile_form = EditProfileForm(instance=profile)
        args = {}
        args['user_form'] = user_form
        args['profile_form'] = profile_form
        return render(request, self.template_name, args)

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=self.kwargs['username']).first()
        profile = Profile.objects.filter(user=user).first()
        user_form = EditUserForm(request.POST, instance=user)
        profile_form = EditProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form = user_form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('user', username=user.username)
        return render(request, self.template_name, args)


class Index(View):
    def get(self, request, *args, **kwargs):
        show_followed = 'all'
        if 'index' in request.session:
            show_followed = request.session['index']
        if show_followed == 'followed':
            # posts = Post.objects.all()
            posts = request.user.followed_posts()
        else:
            posts = Post.objects.all()
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.timestamp = datetime.utcnow()
                post.save()
                return redirect('index')
        else:
            form = PostForm()
        context = {
            'posts': posts,
            'form': form,
            'show_followed': show_followed,
        }
        return render(request, "index.html", context)


def index_all(request):
    request.session["index"] = "all"
    # response = HttpResponseRedirect('/')
    # response.set_cookie('showAll', '0', max_age=30 * 24 * 60 * 60)
    return redirect('index')


def index_followed(request):
    request.session["index"] = "followed"
    # response = HttpResponseRedirect('/')
    # response.set_cookie('showAll', '1', max_age=30 * 24 * 60 * 60)
    return redirect('index')


def users(request):
    users = User.objects.all()
    return render(request, 'users/list_users.html', {'users': users})


def user(request, username):
    pass


def post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/post.html', {'posts': [post]})

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.author = request.user
            form.save()
            return redirect('homedoc')
    else:
        form = DocumentForm()
    return render(request, 'users/model_form_upload.html', {
        'form': form
    })

def letra_update(request, pk, template_name='users/model_form_upload.html'):
    doc= get_object_or_404(Document, pk=pk)
    form = DocumentForm(request.POST or None, instance=doc)
    if form.is_valid():
        form.save()
        return redirect('homedoc')
    return render(request, template_name, {'form':form})

def homedoc(request):
    documents = Document.objects.all().filter(author=1)
    return render(request, 'users/homedoc.html', { 'documents': documents })

def doc_delete(request, pk, template_name='users/doc_delete.html'):
    documents= get_object_or_404(Document, pk=pk)    
    if request.method=='POST':
        documents.delete()
        return redirect('homedoc')
    return render(request, template_name, {'object':documents})

# ----------letras-------------


def letra_list(request, template_name='index.html'):
    
    def get(self, request, *args, **kwargs):
        show_followed = 'all'
        if 'index' in request.session:
            show_followed = request.session['index']
        if show_followed == 'followed':
            # posts = Post.objects.all()
            posts = request.user.followed_posts()
        else:
            posts = Post.objects.all()
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.timestamp = datetime.utcnow()
                post.save()
                return redirect('index')
        else:
            form = PostForm()
        context = {
            'posts': posts,
            'form': form,
            'show_followed': show_followed,
        }

    letra = Letra.objects.all().filter(author=1)
    data = {}
    data['object_list'] = letra
    return render(request, template_name, data)

def letra_view(request, pk, template_name='letras/letra_detail.html'):
    letra= get_object_or_404(Letra, pk=pk) 
    return render(request, template_name, {'object':letra})

def letra_create(request, template_name='letras/letra_form.html'):
    form = LetraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('letra_list')
    return render(request, template_name, {'form':form})

def letra_update(request, pk, template_name='letras/letra_form.html'):
    letra= get_object_or_404(Letra, pk=pk)
    form = LetraForm(request.POST or None, instance=letra)
    if form.is_valid():
        form.save()
        return redirect('letra_list')
    return render(request, template_name, {'form':form})

def letra_delete(request, pk, template_name='letras/letra_confirm_delete.html'):
    letra= get_object_or_404(Letra, pk=pk)    
    if request.method=='POST':
        letra.delete()
        return redirect('letra_list')
    return render(request, template_name, {'object':letra})