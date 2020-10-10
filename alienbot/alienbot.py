# importing regex and random libraries
import re
import random

class AlienBot:
  """The AlienBot class represents 
    an alien object
    """
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  # random starter questions an alien might ask
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

  def __init__(self):
    self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                        'answer_why_intent': r'why\sare.*',
                        'cubed_intent': r'.*cube.*(\d+)'
                            }
  # START of methods for core chatbot functionality
  # alien greets the user
  def greet(self):
    self.name = input("Hello there, what's your name? ")
    will_help = input(f"Hi, {self.name}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? ")
    # checks if the user wants to chat
    if will_help in self.negative_responses:
      print("Ok, have a nice Earth day!")
      return
    self.chat()
    

  # checks if a user has used an exit command
  def make_exit(self, reply):
    for command in self.exit_commands:
      if command in reply:
        print("Ok, have a nice Earth day!")
        return True

  # runs the program allowing users to chat with the alien
  def chat(self):
    # asks the user a random question:
    # alien selects a question from random_questions, asks the user, and then saves the user's response
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply))


  # matches the response pairs in alienbabble
  def match_reply(self, reply):
    for key, value in self.alienbabble.items():
      intent = key
      regex_pattern = value
      found_match = re.match(regex_pattern, reply)
      if found_match and intent == "describe_planet_intent":
        return self.describe_planet_intent()
      elif found_match and intent == "answer_why_intent":
        return self.answer_why_intent()
      elif found_match and intent == "cubed_intent":
        return self.cubed_intent(found_match.groups()[0])
      else:
        return self.no_match_intent()

  # END of methods for core chatbot functionality

  # START of methods associated with user intents
  # includes responses about the alien's planet
  def describe_planet_intent(self):
    responses = ("My planet is a utopia of diverse organisms and species. ", "I am from Opidipus, the capital of the Wayward Galaxies. ")
    return random.choice(responses)

  # includes responses for why the alien is visiting
  def answer_why_intent(self):
    responses = ("I come in peace. ", "I am here to collect data on your planet and its inhabitants. ", "I heard the coffee is good. ")
    return random.choice(responses)
       
  # returns the cube of a number
  def cubed_intent(self, number):
    number = int(number)
    cubed_number = number * number * number
    return f"The cube of {number} is {cubed_number}. Isn't that cool? "

  # responds with something general when none of the other intents are matched
  def no_match_intent(self):
    responses = ("Please tell me more. ", "Tell me more! ", "Why do you say that? ", "I see. Can you elaorate? ", "Interesting. Can you tell me more? ", "I see. How do you think? ", "Why? ", "How do you think I feel when you say that? ")
    return random.choice(responses)

# create an instance of AlienBot and try it out
alien = AlienBot()
alien.greet()
