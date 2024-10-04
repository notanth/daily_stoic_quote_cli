"""A package to give you a daily stoic quote!"""

__version__ = "0.1"

import requests

api_url = "https://stoic-quotes.com/api/quote"

def get_quote():
  response = requests.get(api_url)
  #print(response.json())
  data = response.json()
  author = data["author"]
  quote = data["text"]
  full_message = f"{author} said: {quote}"
  #print("print data ['author'] is: ", data["author"])
  return full_message

print(get_quote())
