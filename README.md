# ReAct Agent Implementation

### Overview
This repo contains a simple implementation of the ReAct Agent Pattern for LLMs.
The base of this code is taken directly from Simon Wilison's approach outlined [here](https://til.simonwillison.net/llms/python-react-pattern)


### Running the code
To run the code you just need to plug in your openai api key.
The agent will then run in a loop in the command line awaiting questions until you type 'exit'

You can run this locally or by forking [this Repl](https://replit.com/@mattambrogi/Agent-Implementation)

### Example queries / outputs

**User:** Whats on my todo list for today?

**Agent:**
Thought: I should fetch the last item from the todo list.
Action: fetch_last_todo: none
PAUSE
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
Answer: The last item on your todo list is "delectus aut autem" and it is not completed.


*Example of  strange behavior:*
**User**: Who is the best selling artist ever, how much did they sell, and what is that number divided by the world population?

**Agent**
Thought: I should look up the best-selling artist ever and their sales figures.

Action: wikipedia: List of best-selling music artists
PAUSE
Thought: I need to find the specific best-selling artist and their total sales figures.

Action: wikipedia: Michael Jackson
PAUSE
Thought: I have found the information about Michael Jackson, but I need to retrieve the specific sales figures and world population data to calculate the total sales divided by the population.

Action: fetch_last_todo: none
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
Thought: It seems like there's a glitch in fetching the last todo item. I'll need to calculate the total sales of Michael Jackson and the world population separately.

Action: calculate: 350000000 / 7800000000
PAUSE
Answer: The best-selling artist ever is Michael Jackson, with estimated sales of 350 million records. When this number is divided by the world population of approximately 7.8 billion, the result is approximately 0.0449.


### Other example queries
- "calculate: 4 * 7 / 3"
- "Has Simon been to Madagascar?"
- "Who was the first man on the moon?"

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


