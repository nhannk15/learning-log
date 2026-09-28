from django.shortcuts import render
from learning_logs.models import Topic

# Create your views here.
def hello(request):
    """The homepage for Learning Log"""
    return render(request, 'learning_logs/index.html')

def about(request):
    """The about page for Learning Log"""
    return render(request, 'learning_logs/about.html')

def topics(request):
    """The topics page for the topic list"""
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, "learning_logs/topics.html", context)

def topic(request, topic_id):
    """The topics page for a specific topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.all()
    context = {'topic': topic, 'entries': entries}
    return render(request, "learning_logs/topic.html", context)