from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='dashboard'),
    path('profile', views.profile, name='profile'),

    ###Blog Generation Routes
    path('generate-blog-topic', views.blogTopic, name='blog-topic'), 
    path('generate-blog-sections', views.blogSections, name='blog-sections'),

    #Saving Blog Topics for future use
    path('save-blog-topic/<str:blogTopic>/', views.saveBlogTopic, name='save-blog-topic'),
    path('use-blog-topic/<str:blogTopic>/', views.useBlogTopic, name='use-blog-topic'),
    path('view-generated-blog/<slug:slug>/', views.viewGeneratedBlog, name='view-generated-blog'),
]

