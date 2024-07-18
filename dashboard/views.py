from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

# Local Imports
from .forms import ProfileForm, ProfileImageForm
from .models import Profile, Blog, BlogSection  # Ensure BlogSection is imported
from .functions import generateBlogTopicIdeas, generateBlogSectionTitles, generateBlogSectionDetails

@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def profile(request):
    user_profile = request.user.profile
    context = {}
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        image_form = ProfileImageForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid() and image_form.is_valid():
            form.save()
            image_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = ProfileForm(instance=user_profile)
        image_form = ProfileImageForm(instance=user_profile)
    
    context['form'] = form
    context['image_form'] = image_form
    return render(request, 'dashboard/profile.html', context)

@login_required
def blogTopic(request):
    context = {}

    if request.method == 'POST':
        #Retrieve the blogIdea String from the submitted Form
        blogIdea = request.POST.get('blogIdea')
        request.session['blogIdea'] = blogIdea

        keywords = request.POST.get('keywords')
        request.session['keywords'] = keywords

        audience = request.POST.get('audience')
        request.session['audience'] = audience

        blogTopics = generateBlogTopicIdeas(blogIdea, audience, keywords)
        if blogTopics:
            request.session['blogTopics'] = blogTopics
            return redirect('blog-sections')
        else:
            messages.error(request, "Oops, please try again.")
            return redirect('blog-topic')

    return render(request, 'dashboard/blog-topic.html', context)

@login_required
def blogSections(request):
    if 'blogTopics' in request.session:

        pass
    else:
        messages.error(request, "Start by creating blog topic ideas")
        return redirect('blog-topic')
    
    context = {'blogTopics': request.session['blogTopics']}
    return render(request, 'dashboard/blog-sections.html', context)

@login_required
def saveBlogTopic(request, blogTopic):
    if 'blogIdea' in request.session and 'keywords' in request.session and 'audience' in request.session and 'blogTopics' in request.session:
        blog = Blog.objects.create(
            title = blogTopic,
            blogIdea = request.session['blogIdea'],
            keywords = request.session['keywords'],
            audience = request.session['audience'],
            profile = request.user.profile)
        blog.save()

        blogTopics = request.session['blogTopics']
        blogTopics.remove(blogTopic)
        request.session['blogTopics'] = blogTopics
        return redirect('blog-sections')
    else:
        return redirect('blog-sections')    

@login_required
def useBlogTopic(request, blogTopic):
    context = {}
    if 'blogIdea' in request.session and 'keywords' in request.session and 'audience' in request.session:
        blog = Blog.objects.create(
            title = blogTopic,
            blogIdea = request.session['blogIdea'],
            keywords = request.session['keywords'],
            audience = request.session['audience'],
            profile = request.user.profile)
        blog.save()
        
        blogSections = generateBlogSectionTitles(blogTopic, request.session['audience'], request.session['keywords'])
    else:
        return redirect('blog-topic')

    if len(blogSections) > 0:
        #Adding the sections to the session
        request.session['blogSections'] = blogSections

        #Adding the sections to the context
        context['blogSections'] = blogSections
    else:
        messages.error(request, "Oops, you beat the AI, try again.")
        return redirect('blog-topic')

    if request.method == 'POST':    
        for val in request.POST:
            if not 'csrfmiddlewaretoken' in val:
                section = generateBlogSectionDetails(blogTopic, val, request.session['audience'], request.session['keywords'])

                ##Create Database Record
                blogSec = BlogSection.objects.create(
                    title = val,
                    body = section,
                    blog = blog)  
                blogSec.save()

        return redirect('view-generated-blog', slug=blog.slug)     

    return render(request, 'dashboard/select-blog-sections.html', context)

@login_required
def viewGeneratedBlog(request, slug):   
    try: 
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        messages.error(request, 'Something went wrong in viewGeneratedBlog')
        return redirect('blog-topic')    

    blogSections = BlogSection.objects.filter(blog=blog)

    context = {
        'blog': blog,
        'blogSections': blogSections,
    }

    return render(request, 'dashboard/view-generated-blog.html', context)

# from django.shortcuts import render, redirect
# from django.templatetags.static import static
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django.contrib import messages

# # Local Imports
# from .forms import ProfileForm, ProfileImageForm
# from .models import Profile, Blog
# from .functions import generateBlogTopicIdeas, generateBlogSectionTitles
# from .functions import *


# @login_required
# def home(request):
#     return render(request, 'dashboard/home.html')

# @login_required
# def profile(request):
#     user_profile = request.user.profile
#     context = {}
    
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=user_profile)
#         image_form = ProfileImageForm(request.POST, request.FILES, instance=user_profile)

#         if form.is_valid() and image_form.is_valid():
#             form.save()
#             image_form.save()
#             messages.success(request, 'Profile updated successfully')
#             return redirect('profile')
#         else:
#             messages.error(request, 'Please correct the error below.')

#     else:
#         form = ProfileForm(instance=user_profile)
#         image_form = ProfileImageForm(instance=user_profile)
    
#     context['form'] = form
#     context['image_form'] = image_form
#     return render(request, 'dashboard/profile.html', context)

# @login_required
# def blogTopic(request):
#     context = {}

#     if request.method == 'POST':
#         #Retrieve the blogIdea String from the submitted Form
#         blogIdea = request.POST.get('blogIdea')
#         request.session['blogIdea'] = blogIdea

#         keywords = request.POST.get('keywords')
#         request.session['keywords'] = keywords

#         audience = request.POST.get('audience')
#         request.session['audience'] = audience

#         blogTopics = generateBlogTopicIdeas(blogIdea, audience, keywords)
#         if blogTopics:
#             request.session['blogTopics'] = blogTopics
#             return redirect('blog-sections')
#         else:
#             messages.error(request, "Oops, please try again.")
#             return redirect('blog-topic')

#     return render(request, 'dashboard/blog-topic.html', context)

# @login_required
# def blogSections(request):
#     if 'blogTopics' in request.session:

#         pass
#     else:
#         messages.error(request, "Start by creating blog topic ideas")
#         return redirect('blog-topic')
    
#     context = {'blogTopics': request.session['blogTopics']}
#     return render(request, 'dashboard/blog-sections.html', context)

# @login_required
# def saveBlogTopic(request, blogTopic):
#     if 'blogIdea' in request.session and 'keywords' in request.session and 'audience' in request.session and 'blogTopics' in request.session:
#         blog = Blog.objects.create(
#         title = blogTopic,
#         blogIdea = request.session['blogIdea'],
#         keywords = request.session['keywords'],
#         audience = request.session['audience'],
#         profile = request.user.profile)
#         blog.save()

#         blogTopics = request.session['blogTopics']
#         blogTopics.remove(blogTopic)
#         request.session['blogTopics'] = blogTopics
#         return redirect('blog-sections')
#     else:
#         return redirect('blog-sections')    


# @login_required
# def useBlogTopic(request, blogTopic):
#     context = {}
#     if 'blogIdea' in request.session and 'keywords' in request.session and 'audience' in request.session:
#         blog = Blog.objects.create(
#         title = blogTopic,
#         blogIdea = request.session['blogIdea'],
#         keywords = request.session['keywords'],
#         audience = request.session['audience'],
#         profile = request.user.profile)
#         blog.save()
        
#         blogSections = generateBlogSectionTitles(blogTopic, request.session['audience'], request.session['keywords'])
#     else:
#         return redirect('blog-topic')

#     if len(blogSections) > 0:
#         #Adding the sections to the session
#         request.session['blogSections'] = blogSections

#         #Adding the sections to the context
#         context['blogSections'] = blogSections
#         # return redirect('select-blog-sections')
#     else:
#         messages.error(request, "Oops, you beat the AI, try again.")
#         return redirect('blog-topic')

#     if request.method == 'POST':    
#         for val in request.POST:
#             if not 'csrfmiddwaretoken' in val:
#                 # print(val)
#                 section = generateBlogSectionDetails(blogTopic, val, request.session['audience'], request.session['keywords'])

#                 ##Create Database Record
#                 blogSec = BlogSection.objects.create(
#                 title = val,
#                 body = section,
#                 blog = blog)  
#                 blogSec.save()

#         return redirect ('view-generated-blog', slug=blog.slug)     

#     return render(request, 'dashboard/select-blog-sections.html', context)   


# @login_required
# def viewGeneratedBlog(request, slug):   
#     try: 
#         blog = Blog.objects.get(slug=slug)
#     except:
#         messages.error(request, 'Something went wrong in viewGeneratedBlog')
#         return redirect('blog-topic')    

#     blogSections = blogSections.objects.filter(blog=blog)

#     context ={}
#     context['blog'] = blog
#     context['blogSections'] = blogSections

#     return render(request, 'dashboard/view-generated-blog.html', context)
    

    








  
