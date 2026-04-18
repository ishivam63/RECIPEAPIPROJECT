from contextlib import redirect_stderr

from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    data = requests.get("https://dummyjson.com/recipes").json()
    context = {
        "recipes" : data["recipes"]
    }
    return render(request, "index.html", context)

def recipedetails(request, id):
    data = requests.get(f"https://dummyjson.com/recipes/{id}").json()
    tag = data["tags"][0]
    related =  requests.get(f"https://dummyjson.com/recipes/tag/{tag}").json()
    context = {
        "recipedetails" : data,
        "related" : related["recipes"]

    }
    print(data)
    return render(request, "recipe.html", context)

def contact(request):
    return render(request, "contact.html")

def search(request):
    data = requests.get("https://dummyjson.com/recipes").json()
    context = {
        "data" : data["recipes"]
    }
    return render(request, "search.html", context)

def signup(request):
    return render(request, "sign-up.html")

def signin(request):
    return render(request, "sign-in.html")


def recipeslist(request):
    data =  requests.get("https://dummyjson.com/recipes").json()
    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    context= {
        "recipes" : data["recipes"],
        "tags" : tags
    }
    return render(request, "recipeslist.html", context)

def recipesbytag(request, tag):
    data =  requests.get(f"https://dummyjson.com/recipes/tag/{tag}").json()
    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    context= {
        "recipes" : data["recipes"],
        "tags" : tags
    }
    return render(request, "recipesbytag.html", context)

def registeruser(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        print(fullname)
        print(email)
        print(phone)
        print(password)

        if Registration.objects.filter(email=email).exists():
            print("Account all ready exists")
            return redirect(signup)

        insertUser = Registration(full_name=fullname, email=email, phone=phone, password=password)
        insertUser.save()

        messages.success(request,"Register Successful")

        return redirect(signin)
    return redirect(signup)


def verifyuser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Registration.objects.get(email=email, password=password)

            if user is not None:
                request.session["login_id"] = user.id
                request.session["login_name"] = user.full_name
                request.session["email"] = user.email
                request.session["phone"] = user.phone

            messages.success(request, "Login Successful")
            return redirect(index)
        except:
            messages.error(request, "Invalid Details")
            return redirect(signin)


def logout(request):
    try:
        del request.session["login_id"]
        del request.session["login_name"]
        del request.session["email"]
        del request.session["phone"]
        messages.success(request, "Logout Successful")
        return redirect(signin)
    except:
        pass


def storecontact(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        print(username)
        print(email)
        print(phone)
        print(subject)
        print(message)

        insertcontact = ContactUs(username=username, email=email, phone=phone, subject=subject, message=message)
        insertcontact.save()

        messages.success(request, "Inquiry Submitted Successful.")
        return redirect(contact)

    return render(request, "contact.html")


def searchresults(request):
    if request.method == "GET":
        query = request.GET.get("query")
        print(query)

        data = requests.get(f"https://dummyjson.com/recipes/search?q={query}").json()
        print(data["recipes"])

        context = {
            "recipes" : data["recipes"]
        }
        return render(request, "searchresults.html", context)

    return render(request, "searchresults.html")


def add_to_wishlist(request,id):
    uid = request.session["login_id"]
    print(id)
    insertToWishlist = Wishlist(user=Registration(id=uid), recipe_id=id)
    insertToWishlist.save()
    messages.success(request, "Added To Wishlist")
    return redirect(index)

def wishlist(request):
    uid = request.session["login_id"]
    wishlistItems = Wishlist.objects.filter(user=uid)

    print(wishlistItems)

    context = {
        "wishlistItems" : wishlistItems
    }

    return render(request, "wishlist.html", context)

def removeItem(request, id):
    item = Wishlist.objects.get(id=id)
    item.delete()
    messages.success(request, "Item removed from wishlist.")
    return redirect(wishlist)