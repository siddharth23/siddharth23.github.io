from azure.ai.inference import  ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
import os

from git import Repo

from path import pathlib

open_ai_url=os.getenv("OPENAI_URL")
open_ai_key=os.getenv("OPENAI_API_KEY")

PATH_BLOG=pathlib.Path("/Users/siddarthkala/code/siddharth23.github.io")
PATH_TO_CONTENT=PATH_BLOG/"content"

# client=ChatCompletionsClient(
#     endpoint=open_ai_url,
#     credential=AzureKeyCredential(open_ai_key)
# )
# prompt="Given two reasons to learn OPENAI with python"
# response=client.complete(
#     max_tokens=300,
#     model="gpt-4.1-mini",
#    messages=[
#             {"role": "system", "content": "You are a query answer agent."},
#             {"role": "user", "content": prompt}
#         ],
# )
# 
# print(response['choices'][0]['message']['content'])

print(PATH_TO_CONTENT)

PATH_TO_CONTENT.mkdir(exist_ok=True,parents=True)
def update_blog(commit_message="Updates blog"):
    repo=Repo(PATH_BLOG)
    repo.git.add(all=True)
    repo.index.commit(commit_message)
    origin=repo.remote(name="origin")
    origin.push()
    
with open(PATH_BLOG/"index.html",'a') as file:
    file.write("It's Working Sid")

update_blog()    
    