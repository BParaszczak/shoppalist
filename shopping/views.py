from django.shortcuts import render

from .models import Product, Category



# /login/
# /shopping/
# /product/add/
# /products/
# /categories/
# /categories/add/
# /category/<category_id>/
def category(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    context = {
        'title': cat.name,
        '': ,
    }
    return render(request, "shopping/category.html", context)
