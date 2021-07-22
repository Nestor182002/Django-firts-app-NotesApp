
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    # registro y manejo de usuarios
    path("",include("User_data.urls")),

    # posts globales,comentarios y likes
    path("",include("posts.urls")),

    # imagesuser
    path("",include("userpictures.urls"))
]
