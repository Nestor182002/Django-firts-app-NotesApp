from django.urls import path
from posts.views import posts, createPosts, updatePosts , DeletePosts, DetailPostComent,createcoments

# login required
from django.contrib.auth.decorators import login_required



urlpatterns = [
    # posts y crear post
    path("post/",login_required(posts.as_view()),name="posts"),    
    path("post/newPosts",login_required(createPosts.as_view()),name="postsnew"), 
   
    
# actualizar y eliminar posts
    path('updateposts/<int:pk>/',login_required( updatePosts.as_view()), name='post-update'), 
    path('<int:pk>/deleteposts',login_required(DeletePosts.as_view()), name='post-delete'), 

    # detalles y comentarios
    path('detailpost/<int:pk>/',login_required(DetailPostComent.as_view()), name='detail-post'), 
    path('detailpost/comentar/<int:pk>/',login_required(createcoments.as_view()), name='createcoments'),
    
]