from django.shortcuts import render


from . import util


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
    return render(request, "encyclopedia/new_page.html")

