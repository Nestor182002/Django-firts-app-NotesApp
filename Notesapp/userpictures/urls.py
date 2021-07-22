# archivos estaticos
from django.conf import settings
from django.conf.urls.static import static
# views
from userpictures.views import ListPictures, Deletepictures
# login required
from django.contrib.auth.decorators import login_required
# path
from django.urls import path  

urlpatterns = [
    
#     pintar
     path("pictures/",ListPictures.as_view(),name="pictures"),
     
     # borrar
     path('deletepictures/<int:pk>',login_required(Deletepictures.as_view()), name='pictures-delete'), 

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# esto para añadir imagenes
