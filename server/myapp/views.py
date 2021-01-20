from django.shortcuts import render, redirect, get_object_or_404
from .models import Idea, Devtool
from django.urls import reverse
from django.http.response import HttpResponse
from .forms import IdeaForm, DevtoolForm


# Idea

def idea_list(request):
    ideas = Idea.objects.all().order_by('id')
    context = {
        'ideas': ideas,
    }
    return render(request, 'myapp/idea_list.html', context)



def idea_detail(request, pk):
    idea = Idea.objects.get(id=pk)
    context = {
        'idea':idea,
    }
    return render(request, 'myapp/idea_detail.html', context)



def idea_create(request):
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect("myapp:idea_detail", pk=idea.pk)
    else:
        form = IdeaForm()
        ctx = {
            "form": form
        }
        return render(request, "myapp/idea_create.html", ctx)

def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            return redirect("myapp:idea_detail", pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
        ctx = {
            "form": form
        }
        return render(request, "myapp/idea_update.html", ctx)

def idea_delete(request, pk):
    '''
    '''
    idea = get_object_or_404(Idea, id=pk)

    if request.method == "GET":
        return redirect('myapp:idea_detail', idea.id)
    elif request.method == "POST":
        idea.delete()
        return redirect('myapp:idea_list')




# Devtool


def devtool_list(request):
    devtools = Devtool.objects.all().order_by('id')
    context = {
        'devtools': devtools,
    }
    return render(request, 'myapp/devtool_list.html', context)

    
def devtool_detail(request, pk):
    devtool = Devtool.objects.get(id=pk)
    context = {
        'devtool':devtool,
    }
    return render(request, 'myapp/devtool_detail.html', context)



def devtool_delete(request, pk):
    devtool = get_object_or_404(Devtool, id=pk)

    if request.method == "GET":
        return redirect('myapp:devtool_detail', devtool.id)
    elif request.method == "POST":
        devtool.delete()
        return redirect('myapp:devtool_list')


def devtool_create(request):
    if request.method == "POST":
        form = DevtoolForm(request.POST, request.FILES)
        if form.is_valid():
            devtool = form.save()
            return redirect("myapp:devtool_detail", pk=devtool.pk)
    else:
        form = DevtoolForm()
        ctx = {
            "form": form
        }
        return render(request, "myapp/devtool_create.html", ctx)

def devtool_update(request, pk):
    devtool = get_object_or_404(Devtool, pk=pk)

    if request.method == "POST":
        form = DevtoolForm(request.POST, request.FILES, instance=devtool)
        if form.is_valid():
            devtool = form.save()
            return redirect("myapp:idea_detail", pk=devtool.pk)
    else:
        form = DevtoolForm(instance=devtool)
        ctx = {
            "form": form
        }
        return render(request, "myapp/devtool_update.html", ctx)