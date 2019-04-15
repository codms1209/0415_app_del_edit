from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts = Post.objects
    return render (request, 'blog/home.html',{'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog/detail.html',{'post' : post_detail})

def post_new(request) :
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/new.html',{'form':form})

def post_edit(request,post_id): #수정은 post new와 비슷ㄷ하다.
    post= get_object_or_404(Post,pk=post_id)#원래 작성된걸 가져와야되서 id를달고 작성한글을 post에 넣는다
    if request.method=="POST": # 제출하기를 누르면 post방식으로 바뀐다.
        form = PostForm(request.POST,instance=post)#instance=post는 원래 있던걸 수정하기 위해 추가.instance 가 post인거슬 가져와랑
        #form에 수정된것을 넣음
        if form.is_valid():
            post=form.save(commit=False)#수정한 내용을 넣자
            post.published_date=timezone.datetime.now() #시간을 수정한 시간으로 빠꾸짜
            post.save()#저장하자. 두개가 바꼈으니까(내용 날짜)
            return redirect('detail',post_id=post.pk) # post id가 방금 수정한 post pk로 가져온다
    else:
        form=PostForm(instance=post)#()가 다르다#new와  post는 위에 추가된 post와 똑같다. instance = 우리가 쓴글
    return render(request,'blog/edit.html',{'form':form}) #randering 해주는데 여기서 원래 써져 있던 글이 나오는거다 

def post_delete(request,post_id):#post id를 삭제를하자
        post=get_object_or_404(Post,pk=post_id)#어떤걸 삭제해야 하는지
        post.delete()#post 지정했으면 post를 삭제
        return redirect('home') # 삭제 했으면 home로 돌아가자