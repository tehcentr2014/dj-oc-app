from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='dashboard'),
    path('profile', views.profile, name='profile'),

    ###Blog Generation Routes
    path('generate-blog-topic', views.blogTopic, name='blog-topic'), 
    path('generate-blog-sections', views.blogSections, name='blog-sections'),
]

# urlpatterns = [
#     path('home/', views.home, name='dashboard'),
#     path('profile/', views.profile, name='profile'),
#     path('generate-blog-topic/', views.blogTopic, name='blog-topic'),
#     path('generate-blog-sections/', views.blogSections, name='blog-sections'),
# ]