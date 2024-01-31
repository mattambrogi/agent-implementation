from agent import Agent
from chat import Chat
from tools import (
  wikipedia,
  simon_blog_search,
  calculate,
  fetch_last_todo
)

def main():

  # todo = fetch_last_todo()
  # print(f'todo: {todo}')

  tools = [wikipedia, simon_blog_search, calculate, fetch_last_todo]
  agent = Agent(tools)

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

  while True:
    user_query = input("Enter a question or type 'exit' to quit: ")

    if user_query.lower() == 'exit':
      print('Exiting...')
      break

    agent.query(user_query)
  

  # Uncomment if you also want to use the Chat class
  # chat = Chat()
  # chat_response = chat(user_query)
  # print("Chat Response:", chat_response)


main()

