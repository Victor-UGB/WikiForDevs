from email import utils
from email.policy import default
from turtle import title
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from random import randint
from django.contrib import messages
from . import util,forms
import encyclopedia


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html",{
        "entry" : util.get_entry(title)
    })

def search(request):
    if request.method == "GET":
        form = forms.NewSearchForm(request.GET)

        if form.is_valid():
            search_query = form.cleaned_data["search"].lower()
            all_entries = util.list_entries()

            files = [filename for filename in all_entries if search_query in filename.lower()]

            if len(files) == 0:
                return render(request, "encyclopedia/search_results.html", {
                    'error' : "No results found",
                    'form':form
                })

            elif len(files) == 1 and files[0].lower() == search_query:
                title = files[0]
                return entry(request, title)

            else:
                title = [filename for filename in all_entries if search_query in filename.lower()]

                if len(title) > 0:
                    return entry(request, title[0])
                    
                else:
                    return render(request, "encyclopedia/search_results.html",{
                        'results': files,
                        'form' : form
                    })

        else:
            return index(request)

    return index(request)


# def new_entry(request):
#     return render(request, "encyclopedia/new_entry.html" )


def new_entry(request):
    # Check request method 
    if request.method == "POST":
        form = forms.NewEntryForm(request.POST)

        # Check that form is valid
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            pages = [util.list_entries()]

            util.save_entry(title, content)

            return entry(request, title)

    return render(request, "encyclopedia/new_entry.html", {
        "form": forms.NewEntryForm()
    })


def edit_entry(request, title):

    if request.method == "GET":
        content = util.get_entry(title)
        
        if content == None:
            messages.error(request, f"{title} page doesn not exists")

        return render(request, "encyclopedia/edit_entry.html", {
            'title' : title,
            'edit_form' : forms.EditEntryForm(initial={'content': content}),
            'search_form' : forms.NewSearchForm()
        })

    elif request.method == "POST":
        form = forms.EditEntryForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data['content']
            util.save_entry(title, content)

            return redirect(reverse('entry', args=[title]))

        else:
            messages.error(request, f'Form Edit not valid')
            return render(request, 'encyclopedia/edit_entry.html', {
                "title": title,
                'edit_form' : form,
                "search_form" : forms.NewSearchForm()
            })


    # if form.is_valid():
    #     util.save_entry(title, file)

    #     return entry(request, title)

    
    # return render(request, "encyclopedia/edit_entry.html", {
    #     "form": form 
    # })


def random_page(request):

    # Get all the markdown files
    all_entries = util.list_entries()

    # index them in a list
    files = [filename for filename in all_entries]

    random_pick = randint(0, len(files))

    file = files[random_pick - 1]

    return entry(request, file)

