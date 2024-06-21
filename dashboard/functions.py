import os
from django.conf import settings
from openai import OpenAI

from openai import OpenAI
from dotenv import load_dotenv

#client = OpenAI()
# Load API Key from evironment variable or secret managment service
#openai.api_key = settings.OPENAI_API_KEY
#openai.api_key = os.getenv("OPENAI_API_KEY")

# Load environment variables from .env file
load_dotenv()

# Load API Key from environment variable or secret management service
api_key = os.getenv("OPENAI_API_KEY")


if not api_key:
    raise ValueError("OpenAI API key not set. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

# Set the API key for openai module
def generateBlogTopicIdeas(topic, keywords):
    response = client.completions.create(model="gpt-3.5-turbo-instruct",
    prompt=f"Generate blog topic ideas on the following topic: {topic}\nKeywords: {keywords}",
    temperature=0.7,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)
    return response
