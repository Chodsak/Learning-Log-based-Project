from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

@login_required
def index(request):
    """The home page for Learning log"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'Topics': topics}
    return render(request, 'learning_logs/index.xhtml',context)


@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'Topics': topics}
    return render(request, 'learning_logs/topics.xhtml', context)


@login_required
def topic(request, topic_id):
    """Show each topic details and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the invalid user cant see page
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'Topic': topic, 'Entries': entries}
    return render(request, 'learning_logs/topic.xhtml', context)


@login_required
def new_topic(request):
    """add a new topic"""
    if request.method != 'POST':
        """if no data submitted, create a blank form"""
        form = TopicForm()
    else:
        """if data submitted, process data"""
        form = TopicForm(data=request.POST)
        if form.is_valid():
            n_topic = form.save(commit=False)
            n_topic.owner = request.user
            n_topic.save()
            return redirect('learning_logs:topics')

    # display a blank or invalid form
    context = {'Topic': form}
    return render(request, 'learning_logs/new_topic.xhtml', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for new_added topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'Topic': topic, 'Entry': form}
    return render(request, 'learning_logs/new_entry.xhtml', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Make sure the invalid user cant see page
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        """pre-fill the form with the current entry"""
        form = EntryForm(instance=entry)
    else:
        """process editing data"""
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'Entry': entry, 'Topic': topic, 'Form': form}
    return render(request, 'learning_logs/edit_entry.xhtml', context)