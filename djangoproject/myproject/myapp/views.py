from django.shortcuts import render
import requests   # <-- add this

def homepage(request):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    posts = response.json()  # convert API response to JSON

    context = {
        "posts": posts
    }

    return render(request, "myapp/homepage.html", context)

def todolist(request):
    return render(request, "myapp/todolist.html")

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")