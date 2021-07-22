# listview
from django.views.generic.list import ListView
# createview
from django.views.generic.edit import CreateView
# updateview
from django.views.generic.edit import UpdateView
# delete view
from django.views.generic.edit import DeleteView
# detail view
from django.views.generic.detail import DetailView

# redirect
from django.shortcuts import redirect
# mis modelos
from posts.models import PostsModels, ComentPosts
# render
from django.shortcuts import render



# listar mis posts
class posts(ListView):
    model= PostsModels
    template_name="posts_global/posts.html"
    paginate_by = 10

#crear mis posts
class createPosts(CreateView):
    model=PostsModels
    template_name="posts_global/create-post.html"
    fields = ['title', 'problem','solution']
    success_url = '/post/'

    def form_valid(self, form):
        form.instance.userforeign = self.request.user
        return super().form_valid(form)

# actualizar mis posts y restringir acceso con dispatch
class updatePosts(UpdateView):
    model=PostsModels
    fields = ['title', 'problem','solution']
    template_name="posts_global/update-post.html"
    success_url = '/post/'

    def dispatch(self, *args, **kwargs):
        # obtengo el id del posts y lo guardo en posts
        # en modelposts lo obtengo de la db
        posts=self.kwargs.get('pk')   
        modelposts=PostsModels.objects.get(pk=posts)
        # if el usuario logueado es igual al post user
        # que siga pero si son diferentes que lo mande 
        # a los posts
        if modelposts.userforeign == self.request.user:
            return super().dispatch(*args, **kwargs)
        else:
            return redirect('/post/')
        return super().dispatch(*args, **kwargs)



# borrar mis posts y restringir acceso con dispatch
class DeletePosts(DeleteView):
    model=PostsModels
    template_name="posts_global/delete-post.html"
    success_url = '/post/'
    
    def dispatch(self, *args, **kwargs):
        # obtengo el id del posts y lo guardo en posts
        # en modelposts lo obtengo de la db
        posts=self.kwargs.get('pk')   
        modelposts=PostsModels.objects.get(pk=posts)
        # if el usuario logueado es igual al post user
        # que siga pero si son diferentes que lo mande 
        # a los posts
        if modelposts.userforeign == self.request.user:
            return super().dispatch(*args, **kwargs)
        else:
            return redirect('/post/')
        return super().dispatch(*args, **kwargs)



# detalle del post y comentarios
class DetailPostComent(DetailView):
    model=PostsModels
    template_name="posts_global/detail-post.html"
    context_object_name="posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk')
        context['comentario'] = ComentPosts.objects.filter(postforeign=pk)
        return context


# crear comentarios y form valid para guardar por instance el comentario en el posts
class createcoments(CreateView):
    model=ComentPosts
    template_name="posts_global/create-coment.html"
    fields = ['comentario']
     
    def form_valid(self, form):
        urlcoment=PostsModels.objects.get(pk=self.kwargs.get('pk'))
        form.instance.usercoment = self.request.user
        form.instance.postforeign =urlcoment
        print(urlcoment)
        return super().form_valid(form)

    
    


    

    
    

    
        

    



    
