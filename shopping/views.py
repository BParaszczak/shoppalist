from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.views.generic.edit import FormMixin, ProcessFormView
from django.contrib.auth.mixins import LoginRequiredMixin #CBV  wzorzec projektowy 
from django.contrib.auth.decorators import login_required #FBV


from .models import Product, Category, Entry
from .forms import DeleteSelectedForm


@login_required
# /index/
def index(request):
    return render(request, "shopping/index.html")
# /login/

# /products/
class ListProducts(FormMixin, ListView, ProcessFormView):
    model = Product 
    template_name = 'shopping/product_list.html'
    form_class = DeleteSelectedForm
    extra_context ={    
        'title': 'Moje produkty',
    }

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        for product in form.cleaned_data.get('products', []):
            Entry.objects.filter(product=product).delete()
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('products')

# /products/add/
class AddProduct(CreateView):
    model = Product
    fields = ['name', 'amount', 'unit', 'comment', 'categories', 'owner']
    template_name = 'shopping/p_add.html'
    extra_context ={   
        'title': 'Dodaj nowy produkt',
    }
    
# /products/edit/
class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'amount', 'unit', 'comment', 'categories', 'owner']
    template_name = 'shopping/p_edit.html'
    extra_context ={   
        'title': 'Edytuj produkt:',
    }

# /products/delete/
class ProductDelete(DeleteView):
    model = Product
    fields = ['name']
    template_name = 'shopping/p_delete.html'
    success_url = reverse_lazy('products')
    extra_context = { 
        'title': 'Czy chcesz usunąć produkt?'
    }

# /products/<int:pk>/
class ProductDetails(DetailView):
    model = Product
    template_name = 'shopping/product.html'
    extra_context = {
        'title': 'Szczegóły produktu',
    }
    
    
# /categories/add/
class AddCategory(CreateView):
    model = Category
    template_name = 'shopping/c_add.html'
    fields = ['name']
    success_url = reverse_lazy('categories')
    extra_context ={   
        'title': 'Utwórz nową listę',
    }

# /categories/edit/
class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'shopping/c_edit.html'
    fields = ['name']
    extra_context ={   
        'title': 'Zmień nazwę listy',
    }
# /categories/delete/
class CategoryDelete(DeleteView):
    model = Category
    template_name = 'shopping/c_delete.html'
    fields = ['name']
    success_url = reverse_lazy('categories')
    extra_context ={   
        'title': 'Czy chcesz usunąć poniższą listę?',
    }

# /categories/<int:pk>/
class CategoryDetails(FormMixin, DetailView, ProcessFormView):
    model = Category
    template_name = 'shopping/category.html'
    form_class = DeleteSelectedForm
    # fields = ['name']
    context_object_name = 'name'
    # extra_context ={   
    #     'title': 
    # }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '{0}'.format(self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        for product in form.cleaned_data.get('products', []):
            Entry.objects.filter(product=product).delete()
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('category', args=[self.object.pk])
    
      


# /categories/
class ListCategories(ListView):
    queryset = Category.objects.annotate(liczba=Count('product'))
    model = Category 
    template_name = 'shopping/cat_list.html'
    extra_context ={     
        'title': 'Moje listy zakupów',
    }