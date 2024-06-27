import os
from django.conf import settings
import openai
from openai import OpenAI
from openai import OpenAIError
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


def generateBlogTopicIdeas(topic, keywords):
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Generate blog topic ideas on the following topic: {topic}\nKeywords: {keywords}\n*",
            temperature=0.7,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        blog_topics = []

        if 'choices' in response:
            if len(response['choices']) > 0:
                res = response['choices'][0]['text']
                a_list = res.split('*')
                blog_topics = [blog.strip() for blog in a_list if blog.strip()]

        return blog_topics

    except InvalidRequestError as e:
        print(f"Invalid request error: {e}")
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
    except RateLimitError as e:
        print(f"Rate limit error: {e}")
    except APIError as e:
        print(f"OpenAI API returned an error: {e}")
    except OpenAIError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return []  # Return an empty list if an error occurs


def generateBlogSectionHeadings(topic, keywords):
    try:
        response = client.completions.create(model="gpt-3.5-turbo-instruct",
            prompt="Generate blog section headings and section titles, based on the following blog section topic.\nTopic: {}\nKeywords: {}\n*".format(topic, keywords),
            temperature=0.7,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        if 'choices' in response and len(response['choices']) > 0:
            return response['choices'][0]['text']
        else:
            return None

    except InvalidRequestError as e:
        print(f"Invalid request error: {e}")
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
    except RateLimitError as e:
        print(f"Rate limit error: {e}")
    except APIError as e:
        print(f"OpenAI API returned an error: {e}")
    except OpenAIError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None  # Return None if an error occurs    