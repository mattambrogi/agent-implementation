from agent import Agent
from tools import (
  wikipedia,
  simon_blog_search,
  calculate,
  fetch_last_todo
)

def main():
  # define tools
  tools = [wikipedia, simon_blog_search, calculate, fetch_last_todo]

  # initialize agent with tools
  agent = Agent(tools)

  # run agent in loop until user exits
  while True:
    user_query = input("Enter a question or type 'exit' to quit: ")

    if user_query.lower() == 'exit':
      print('Exiting...')
      break

    agent.query(user_query)
  
main()

