from django.urls import path

from . import views

urlpatterns = [
    #shopping
    path('', views.index, name="index"),

    #products
    path('products/', views.ListProducts.as_view(), name="products"),
    path('products/add/', views.AddProduct.as_view(), name="p_add"),
    path('products/edit/<int:pk>/', views.ProductUpdate.as_view(), name="p_edit"),
    path('products/delete/<int:pk>/', views.ProductDelete.as_view(), name="p_delete"),
    path('products/<int:pk>/', views.ProductDetails.as_view(), name="product"),

    #categories
    path('categories/', views.ListCategories.as_view(), name="categories"),
    path('categories/add/', views.AddCategory.as_view(), name="c_add"),
    path('categories/edit/<int:pk>/', views.CategoryUpdate.as_view(), name="c_edit"),
    path('categories/delete/<int:pk>/', views.CategoryDelete.as_view(), name="c_delete"),
    path('categories/<int:pk>/', views.CategoryDetails.as_view(), name="category"),

    #admin
    # path('admin/', admin.site.urls)
    
    #login
    # path('login/', views.login, name="login")

]