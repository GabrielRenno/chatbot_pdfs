import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
import openai

def gen_auto_response(ques):
    load_dotenv()
    
    response = openai.Completion.create(
        model="code-cushman-001",
        prompt=f""""Given a Python solution for the leetcode question below
                     Question: how much is 2 + 2?
                    Solution: """,
        temperature=0,
        max_tokens=1114,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    print(response)
    return response.choices[0].text