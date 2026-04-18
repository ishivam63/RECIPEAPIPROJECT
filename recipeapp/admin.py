from django.contrib import admin
from .models import *

@admin.register(Registration)
class ShowUsers(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone", "password", "timestamp"]

@admin.register(ContactUs)
class DisplayContacts(admin.ModelAdmin):
    list_display = ["username", "email", "phone", "subject", "message", "timestamp"]


@admin.register(Wishlist)
class DisplayWishlist(admin.ModelAdmin):
    list_display = ["user", "recipe_name", "added_on"]