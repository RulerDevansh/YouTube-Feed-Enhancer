from groq import Groq
import urllib.request
import re
import webbrowser
import time

query = input("Enter your Topic: ")

# Api Key **************************** PRIVATE *******************************************
client = Groq(
    api_key="ADD KEY HERE",
)
# ****************************************************************************************

completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Give 15 YouTube search suggestions that a user can search if he or she wants to know. I will provide the topic . Only give searches do not explain . Give in form of comma separated"
        },
        {
            "role": "assistant",
            "content": "Please provide the topic. I'll provide 15 YouTube search suggestions in a comma-separated list."
        },
        {
            "role": "user",
            "content": query,
        },

    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
response = ""
for chunk in completion:
    response = response + (chunk.choices[0].delta.content or "")
responcelist = response.split(",") 

# print(responcelist)

for i in responcelist:
    search_keyword = i.replace(' ', '+')
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query='+search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = "https://www.youtube.com/watch?v=" + video_ids[4]
    
    webbrowser.open(url)
    time.sleep(10)
