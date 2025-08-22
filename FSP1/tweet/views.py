from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm

# Create your views here.



def index(request):
    return render(request, 'index.html')

def tweet_list(request): #to list all tweets
    tweets= Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets':tweets})

def tweet_create(request):  # create tweet
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user   # ✅ fix
            tweet.save()
            return redirect('tweet_list')

    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form':form})

def tweet_edit(request, tweet_id): #to edit tweet
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method=="POST":
        form = TweetForm(request.POST, request.FILES,instance=tweet)
        if form.is_valid():
            tweet =form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'from':form})

def tweet_delete(request, tweet_id): #delete tweet
    tweet= get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method=="POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})