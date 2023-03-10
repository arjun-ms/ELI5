import openai
from keys import OPEN_AI_API_KEY

openai.api_key = OPEN_AI_API_KEY

def ask(question,related_keywords):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": f"Explain like I am five years old: {question} ;  related-keywords:"}]
        )
    
    print(completion.choices[0].message.content)
    # print(completion.choices[0])
    # print("+=======================+")
    # print(completion.choices[0].message)
    
    ans = completion.choices[0].message.content
    return ans