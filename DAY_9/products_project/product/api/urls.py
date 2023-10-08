from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path("category/", views.ListCreateCategoryAPIView.as_view(), name='category_list'),
    path("category/<int:pk>/", views.RetrieveUpdateDestroyCategoryAPIView.as_view(), name='category_detail'),
    path('product',views.ListCreateProductAPIView.as_view(), name="product_list"),
    path("product/<int:pk>/", views.RetrieveUpdateDestroyCategoryAPIView.as_view(), name='product_detail'),
    path("category/<int:pk>/products/", views.ListProductOfCategory.as_view(), name='product_of_category'),
    path("product/<int:pk>/comment", views.ListCommentOfProduct.as_view(), name='comment_of_product'),
]