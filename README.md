# ReAct Agent Implementation

Todo: clean up the read me

If you want to compare with straight up open ai call:
- Comment out `agent.query(user_query)`
- Add the following
```
from chat import Chat
chat = Chat()
chat_response = chat(user_query)
print("Chat Response:", chat_response)
```



'''
Example queries  
agent.query("calculate: 4 * 7 / 3")
agent.query("Has Simon been to Madagascar?")
agent.query("Who was the first man on the moon?")

Some interesting to compare with straight up GPT call
Both LLM and Agent get this right:
chat("How old is the United States and what is its age in days?")

But here only agent gets right
agent.query("How old is the United States and what is its age raised to the 4th power?")
chat("How old is the United States and what is its age raised to the 4th power?")

agent.query("How old is the United States and what is its age raised to the 4th power?")

#chat = Chat()
'''


Good example: how old is the united states and whats its age in days?
If you ask chat gpt, knows age, uses code interpreter math part
Simliar thing here, successful agent looks up age wikipedia and then does math

Interesting API gets that right too 

Now let's change it to age raised to 4th power - agent gets that
~ 3.5 billion - well actually only kind of. The answer returned is correct but LLM formats wrong to 354,453,529,6

Answer: The United States is approximately 244 years old, and its age raised to the 4th power is 354,453,529,6.

Now LLM completely lies
The United States is 245 years old as of 2021. 

Raising its age to the 4th power would give us:
245^4 = 282,853,250,000
245^4 is actually ~3.6 billion


