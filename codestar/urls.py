from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Add this import
from blog import views as blog_views

# Temporary view for the homepage
def home(request):
    return HttpResponse("Welcome to the Codestar homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_views.my_blog, name="blog"), # the app urls are loaded as the main urls
    path('', home, name='home'),  # Add this line for the root URL
]