"""A package to give you a daily stoic quote!"""

__version__ = "0.1"

import requests

api_url = "https://stoic-quotes.com/api/quote"

def get_quote():
  response = requests.get(api_url)
  #print(response.json())
  if response.status_code == 200:
    data = response.json()
    author = data["author"]
    quote = data["text"]
    full_message: str = f"{author} said: {quote}"
    # print("print data ['author'] is: ", data["author"])
    return full_message
  else:
    return "Failed to fetch message."

def main():
  """Print daily quote result"""
  message = get_quote()
  print(message)

if __name__ == "__main__":
    main()