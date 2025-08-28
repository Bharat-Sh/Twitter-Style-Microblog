from .models import Tweet

def global_feed(request):
    # Show latest 10 tweets from all users (read-only)
    try:
        qs = Tweet.objects.select_related('user').order_by('-created_at')[:10]
    except Exception:
        # Fallback if created_at not present
        qs = Tweet.objects.select_related('user').order_by('-updated_at')[:10]
    return {'global_feed_tweets': qs}
