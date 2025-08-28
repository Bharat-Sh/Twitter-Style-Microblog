from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Tweet
from .forms import TweetForm, RegistrationForm

def index(request):
    # If user is logged in, redirect to /tweets/ (not /tweets/mytweets/)
    if request.user.is_authenticated:
        return redirect('tweet_list')  # This goes to /tweets/
    # If not logged in, show homepage with global feed
    return render(request, 'index.html')

@login_required  # Add this decorator
def tweet_list(request):
    # Filter tweets to show ONLY the current user's tweets
    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')
    print(f"Found {tweets.count()} tweets for user {request.user.username}")
    return render(request, 'tweet_list.html', {'tweets': tweets})
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
        else:
            # Add this to see form errors
            print("Form errors:", form.errors)
    else:
        form = TweetForm()
    
    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})