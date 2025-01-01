from django.shortcuts import render
from .models import Tweet,Vote
from .forms import TweetForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .utils import fetch_news, fetch_random_joke
from django.http import JsonResponse
from better_profanity import profanity
import openai
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return render(request,'index.html')


def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})


@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            text = form.cleaned_data['text']

            # Check for offensive language
            if profanity.contains_profanity(text):
                form.add_error('text', 'Your tweet contains inappropriate language.')
            else:
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                return redirect('tweet_list')
        
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})    
    

@login_required
def tweet_edit(request,tweet_id):
    tweet =get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet= form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
        
    else:
        form=TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})    
 
@login_required    
def tweet_delete(request,tweet_id):
    tweet= tweet =get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})  


def register(request):
    if request.method == 'POST':
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form =UserRegistrationForm()   
    return render(request,'registration/register.html',{'form':form})


def search_tweets(request):
    query = request.GET.get('q')  # Get the query from the search input
    if query:
        results = Tweet.objects.filter(text__icontains=query)  
    else:
        results = Tweet.objects.none()
    return render(request, 'search_results.html', {'results': results, 'query': query})


def news_view(request):
    api_key = "ac1d0954ed5446a68e9fc64fbe035def"
    query = request.GET.get("query", "cricket")  # Get search keyword from user
    news_articles = fetch_news(api_key, query=query)

    return render(request, "news.html", {"articles": news_articles})

def joke_view(request):
    joke = fetch_random_joke()
    return render(request, "jokes.html", {"joke": joke})

@login_required 
def upvote_tweet(request, tweet_id):
    if request.method == "POST":
        tweet = get_object_or_404(Tweet, id=tweet_id)
        user = request.user

        # Check if the user has already voted
        existing_vote = Vote.objects.filter(user=user, tweet=tweet).first()

        if existing_vote:
            if existing_vote.vote_type == 'upvote':
                return JsonResponse({"error": "You have already upvoted this tweet."}, status=400)
            else:
                # Switch the vote from downvote to upvote
                existing_vote.vote_type = 'upvote'
                existing_vote.save()
                tweet.downvotes -= 1
                tweet.upvotes += 1
                tweet.save()
        else:
            # Create a new upvote
            Vote.objects.create(user=user, tweet=tweet, vote_type='upvote')
            tweet.upvotes += 1
            tweet.save()

        return JsonResponse({"upvotes": tweet.upvotes, "downvotes": tweet.downvotes})

@login_required 
def downvote_tweet(request, tweet_id):
    if request.method == "POST":
        tweet = get_object_or_404(Tweet, id=tweet_id)
        user = request.user

        # Check if the user has already voted
        existing_vote = Vote.objects.filter(user=user, tweet=tweet).first()

        if existing_vote:
            if existing_vote.vote_type == 'downvote':
                return JsonResponse({"error": "You have already downvoted this tweet."}, status=400)
            else:
                # Switch the vote from upvote to downvote
                existing_vote.vote_type = 'downvote'
                existing_vote.save()
                tweet.upvotes -= 1
                tweet.downvotes += 1
                tweet.save()
        else:
            # Create a new downvote
            Vote.objects.create(user=user, tweet=tweet, vote_type='downvote')
            tweet.downvotes += 1
            tweet.save()

        return JsonResponse({"upvotes": tweet.upvotes, "downvotes": tweet.downvotes})


# OpenAI API key
openai.api_key = 'Your_api_key'

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        if user_message:
            try:
                # Generate response using OpenAI API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_message}]
                )
                bot_reply = response['choices'][0]['message']['content']
                return JsonResponse({'reply': bot_reply})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'No message provided'}, status=400)
    elif request.method == 'GET':
        # Render the chatbot HTML page
        return render(request, "chatbot.html")
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
