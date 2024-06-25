import os
from django.conf import settings
import openai
from openai import OpenAI
from dotenv import load_dotenv


#client = OpenAI()
# Load API Key from evironment variable or secret managment service
# Load environment variables from .env file
load_dotenv()

# Load API Key from environment variable or secret management service
#api_key = os.getenv("OPENAI_API_KEY")
api_key = settings.OPENAI_API_KEY


if not api_key:
    raise ValueError("OpenAI API key not set. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)


#blog_topics = []

def generateBlogTopicIdeas(topic, keywords):
    blog_topics = []

    response = client.completions.create(model="gpt-3.5-turbo-instruct",
      prompt=f"Generate blog topic ideas on the following topic: {}\nKeywords: {} \n*".format(topic, keywords),
      temperature=0.7,
      max_tokens=300,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0)

    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']
        else:
           return []
    else:
        return []

    a_list = res.split('*')
    return res

    # if len(a_list) > 0:
    #     for blog in a_list:
    #         blog_topics.append(blog)
    # else:
    #     return []

    # return blog_topics    


def generateBlogSectionHeadings(topic, keywords):
    response = client.completions.create(model="gpt-3.5-turbo-instruct",
    prompt="Generate blog section headings and section titles, based on the following blog section topic.\nTopic: {}\nKeywords: {}\n*".format(topic, keywords),
    temperature=0.7,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)

    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']
        else:
            res = None
    else:
        res = None 
        
    return res    

# res = generateBlogTopicIdeas(topic, keywords).replace('\n', '')
# b_list = res.split('*')
# for blog in b_list:
#     blog_topics.append(blog)
#     print ('\n')
#     print (blog)
