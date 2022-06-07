from django.shortcuts import render
from .models import  Topics

# Create your views here.
def index(request):
    """Home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics"""
    topics = Topics.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request,"learning_logs/topics.html", context)

def topic(request, topic_id=1):
    """Show a single topic and all its entries."""
    topic = Topics.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {"topic":topic,
               'entries': entries}
    return render(request,'learning_logs/topic.html',context)   

def new_topic(request)
 

