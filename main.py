from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  """format account data"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return(f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, A_followers, B_followers):
  """Take the user guess and follower counts and returns if they got it right"""
  if A_followers > B_followers:
    return guess == "A"
  else:
    return guess == "B"

print(logo)
score = 0
continue_game = True
account_B = random.choice(data)

while continue_game:
  
  account_A = account_B
  account_B = random.choice(data)
  
  while account_A == account_B:
    account_B = random.choice(data)
  
  print(f"Compare A:  {format_data(account_A)}.")
  print(vs)
  print(f"Against B:  {format_data(account_B)}.")
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  
  A_follower_count = account_A["follower_count"]
  B_follower_count = account_B["follower_count"]
  is_correct = check_answer(guess, A_follower_count, B_follower_count)

  clear()
  print(logo)
  
  if is_correct:
    score += 1 
    print(f"You're right! Current score: {score}.")
  else:
    continue_game = False
    print(f"Sorry, that's wrong. Final score: {score}.")  