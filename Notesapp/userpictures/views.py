# listview
from django.views.generic import ListView
# delete view
from django.views.generic.edit import DeleteView

# modelos
from userpictures.models import pictureUser
# render
from django.shortcuts import render, redirect

# Create your views here.


# pintar mis imagenes
class ListPictures(ListView):
    model=pictureUser
    template_name="picturesusers/picturelist.html"
    context_object_name="pictures"

    def get_context_data(self, **kwargs):
        context = super(ListPictures, self).get_context_data(**kwargs)
        context['personal']=context['pictures'].filter(users=self.request.user)
        return context

# delete view
class Deletepictures(DeleteView):
    model=pictureUser
    template_name="picturesusers/deletepictures.html"

    def dispatch(self, *args, **kwargs):
        # obtengo el id del posts y lo guardo en posts
        # en modelposts lo obtengo de la db
        pictures=self.kwargs.get('pk')   
        modelpicture=pictureUser.objects.get(pk=pictures)
        # if el usuario logueado es igual al post user
        # que siga pero si son diferentes que lo mande 
        # a los posts
        if modelpicture.users == self.request.user:
            return super().dispatch(*args, **kwargs)
        else:
            return redirect('/pictures/')
        return super().dispatch(*args, **kwargs)



