# ReAct Agent Implementation

### Overview
This repo contains a simple implementation of the ReAct Agent Pattern for LLMs.
The base of this code is taken directly from Simon Wilison's approach outlined [here](https://til.simonwillison.net/llms/python-react-pattern)


### Running the code
To run the code you just need to plug in your openai api key.
The agent will then run in a loop in the command line awaiting questions until you type 'exit'

You can run this locally or by forking [this Repl](https://replit.com/@mattambrogi/Agent-Implementation)

### Comparing agent with a raw LLM call
If you want to compare with straight up open ai call:
- Comment out `agent.query(user_query)`
- Add the following
```
from chat import Chat
chat = Chat()
chat_response = chat(user_query)
print("Chat Response:", chat_response)
```


### Example queries
- "calculate: 4 * 7 / 3"
- "Has Simon been to Madagascar?"
- "Who was the first man on the moon?"

### Examples of agent utility over plain LLM

**Raising to a power**
Both LLM and Agent get this right:
chat("How old is the United States and what is its age in days?")

But here only agent gets right
agent.query("How old is the United States and what is its age raised to the 4th power?")
chat("How old is the United States and what is its age raised to the 4th power?")






Agent responds:
`Answer: The United States is approximately 244 years old, and its age raised to the 4th power is 354,453,529,6.`

Which is right outside of the formatting issue (should be 3,544,535,296)

LLM responds:
```
The United States is 245 years old as of 2021. 

Raising its age to the 4th power would give us:
245^4 = 282,853,250,000
```

Which is fairly far off from the true value ~3.6 billion


