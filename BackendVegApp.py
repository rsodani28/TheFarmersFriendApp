import openai
from my_sk import my_sk
openai.api_key = my_sk
question = input("Ask your question about plants?")
messages_list = [{"role":"system","content":"I am The Farmers Best Friend, ask me any question about plants"},
                 {"role":"user","content":question},]
chat_completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
                                               messages = messages_list,
                                               n = 1,
                                               temperature = 0)
print(chat_completion.choices[0].message.content)

