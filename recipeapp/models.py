from django.db import models
import requests
# Create your models here.
class Registration(models.Model):
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class ContactUs(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)



class Wishlist(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    recipe_id = models.IntegerField()
    added_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.full_name}'s wishlist - Recipe {self.recipe_id}"

    def recipe_name(self):
        try:
            response = requests.get(f"https://dummyjson.com/recipes/{self.recipe_id}")
            if response.status_code == 200:
                return response.json().get("name", f"Recipe #{self.recipe_id}")
        except:
            pass
        return f"Recipe #{self.recipe_id}"

    recipe_name.short_description = "Recipe"