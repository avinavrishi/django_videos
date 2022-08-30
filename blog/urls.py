from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('category/',views.CategoryView, name="category_page"),

    path('category/<str:category>/',views.CategoryFileView, name="category_page_files"),
    path('<str:query>/',views.SearchPageView, name="search_page"),
    path('post/<slug:slug>/', views.post_detail, name="post_detail"),
] 
