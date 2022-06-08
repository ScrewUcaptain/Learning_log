from django.shortcuts import render, redirect
from .models import  Topics
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        #No data submitted; create a blank form
        form = TopicForm()
    else:
        #POST data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    #Display a blank or valid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request,topic_id):
    """Add a new entry for a particular topic."""
    topic = Topics.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm()
        #No data submitted 
    else:
        #POST data submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid:
            form.        
            
    
    
 

