import re
from chat import Chat

class Agent:
  action_re = re.compile('^Action: (\w+): (.*)$')

  def __init__(self, tools, max_turns=10):
    self.tools = tools
    self.max_turns = max_turns
    self.prompt = self.get_agent_prompt(self.tools)
    self.chat = Chat(self.prompt)
    self.known_actions = self.get_actions(self.tools)

  def query(self, prompt):
    i = 0
    if i == 0: print(prompt)
    next_prompt = prompt
    action_re = self.__class__.action_re
    while i < self.max_turns:
      i+=1
      result = self.chat(next_prompt)
      print(result)
      actions = [action_re.match(a) for a in result.split('\n') if action_re.match(a)]
      if actions:
        groups = actions[0].groups()
        action = groups[0]
        action_input = groups[1] if len(groups) > 1 else None
        if action not in self.known_actions:
          raise Exception("Unknown action: {}: {}".format(action, action_input))
        if action_input:
          observation = self.known_actions[action](action_input)
        else:
          observation = self.known_actions[action]()
        next_prompt = "Observation: {}".format(observation)
      else:
        return
        
    
  def get_agent_prompt(self, tools):
    tools_str = "\n".join([f"{tool.__doc__} \n" for tool in tools])
    print(tools_str)
    
    prompt = f"""
    You run in a loop of Thought, Action, PAUSE, Observation.
    At the end of the loop you output an Answer
    Use Thought to describe your thoughts about the question you have been asked.
    Use Action to run one of the actions available to you - then return PAUSE.
    Observation will be the result of running those actions.
    
    Your available actions are:
    
    {tools_str}
    
    Always look things up on Wikipedia if you have the opportunity to do so.
    
    Example session:
    
    Question: What is the capital of France?
    Thought: I should look up France on Wikipedia
    Action: wikipedia: France
    PAUSE
    
    You will be called again with this:
    
    Observation: France is a country. The capital is Paris.
    
    You then output:
    
    Answer: The capital of France is Paris
    """.strip()
    
    return prompt

  def get_actions(self, tools):
    return {tool.__name__: tool for tool in tools}
    
    

