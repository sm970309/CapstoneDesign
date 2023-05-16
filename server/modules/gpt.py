import openai

openai.api_key = "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"

def ask_chatGPT(content):    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        temperature=0.1
        )
    return completion.choices[0].message.content
text='바로 죽여버립니다'
print(text)
print(ask_chatGPT(f"{text} \n대답은 한국어로 해주고, 이 문장에서 문제가 되는 내용이 있으면 문제가 되는 내용과 이유를 알려줘. 만약 문제가 되는 내용이 없으면 no라고 대답해줘"))