import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

class Chat:
  '''
  Wrapper class for OpenAI's Chat API. Designed by Simon
  '''
  def __init__(self, system="", model=None):
    self.system = system
    self.model = model
    self.messages = []
    if self.system:
      self.messages.append({"role": "system", "content": self.system})
    if self.model is None:
      self.model = "gpt-3.5-turbo-1106"

  def __call__(self, message):
    self.messages.append({"role": "user", "content": message})
    result = self.execute()
    self.messages.append({"role": "assistant", "content": result})
    return result

  def execute(self):
    completion = openai.chat.completions.create(
      model=self.model,
      messages=self.messages
    )
    response = completion.choices[0].message.content
    return response