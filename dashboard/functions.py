import os
from django.conf import settings
import openai
from openai import OpenAIError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API Key from environment variable or Django settings
api_key = os.getenv("OPENAI_API_KEY") or getattr(settings, 'OPENAI_API_KEY', None)

if not api_key:
    raise ValueError("OpenAI API key not set. Please set the OPENAI_API_KEY environment variable.")

# Initialize OpenAI client
openai.api_key = api_key

def generateBlogTopicIdeas(topic, audience, keywords):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Generate 5 blog topic ideas on the following topic: {topic}\nAudience: {audience}\nKeywords: {keywords}\n*",
            temperature=0.7, 
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        blog_topics = []
        choices = response.get('choices', [])
        if choices:
            res = choices[0].get('text', '')
            a_list = res.split('*')
            blog_topics = [blog.strip() for blog in a_list if blog.strip()]

        return blog_topics

    except (OpenAIError) as e:
        print(f"OpenAI API error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return []  # Return an empty list if an error occurs

# def generateBlogSectionHeadings(topic, keywords):
#     try:
#         response = openai.Completion.create(
#             model="gpt-3.5-turbo-instruct",
#             prompt=f"Generate blog section headings and section titles, based on the following blog section topic.\nTopic: {topic}\nKeywords: {keywords}\n*",
#             temperature=0.7,
#             max_tokens=300,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#         )

#         choices = response.get('choices', [])
#         if choices:
#             return choices[0].get('text', '')

#     except (OpenAIError) as e:
#         print(f"OpenAI API error: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

#     return None  # Return None if an error occurs



def generateBlogSectionTitles(topic, audience, keywords):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Generate 5 Blog Sections Titles for the following Topic: {topic}\nAudience: {audience}\nKeywords: {keywords}\n*",
            temperature=0.7, 
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # if 'choices' in response:
        #     if len(response['choices'])>0:
        #         res = response['choices'][0]['text']
        #     else:
        #         return [] 
        # else:
        #     return []

        # a_list = res.split('*')
        # if len(a_list) > 0:
        #     for blog in a_list:
        #         blog_sections.append(blog)
        # else:
        #     return []    

        # return blog_sections                       


        blog_sections = []
        choices = response.get('choices', [])
        if choices:
            res = choices[0].get('text', '')
            a_list = res.split('*')
            blog_sections = [blog.strip() for blog in a_list if blog.strip()]

        return blog_sections

    except (OpenAIError) as e:
        print(f"OpenAI API error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return []  # Return an empty list if an error occurs


def generateBlogSectionDetails(blogTopic, sectionTopic, audience, keywords):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Generate detaled blog section for the following blog title, blog section heading, audience and keywords provided.\nBlog Title:{}\nBlog section Heading: {}\nAudience: {}\nKeywords: {}\n\n".format(blogTopic, sectionTopic, audience, keywords),
        temperature=0.7, 
        max_tokens=300,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']
            cleanedRes = res.replace('\n', '<br>')
            return cleanedRes
        else:
            return '' 
    else:
        return ''  


