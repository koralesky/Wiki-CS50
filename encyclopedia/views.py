from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
import random

from . import util


class EncyclopediaEntry(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": 5, "rows": 5}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(title),
            "title": title
        })
    else:
        return render(request, "encyclopedia/404.html")


def new_page(request):
    if request.method == "POST":
        form = EncyclopediaEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "encyclopedia/new_page.html", {
                "form": EncyclopediaEntry
            })
    return render(request, "encyclopedia/new_page.html", {
        "form": EncyclopediaEntry()
    })


def random_page(request):
    entries = util.list_entries()
    selected_page = random.choice(entries)
    return redirect('entry', title=selected_page)
