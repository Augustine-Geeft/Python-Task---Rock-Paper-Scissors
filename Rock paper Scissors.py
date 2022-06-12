import random

while True:
  
  game_options = ["Rock", "Paper", "Scissors"]
  r = "Rock"
  p = "Paper"
  s = "Scissors"
  
  user_choice = input("What do you choose? Type R for Rock, P for Paper or S for Scissors.\n").lower()
  
  while user_choice != "r" and user_choice != "p" and user_choice != "s":
    print("Invalid! Input is not amongst our options")
    user_choice = input("What do you choose? Type R for Rock, P for Paper or S for Scissors.\n").lower()
        
  computer_choice = random.choice(game_options)
  
  if user_choice == "r":
    user_choice = game_options[0]
    print(f"Player({game_options[0]}): CPU ({computer_choice})")
  elif user_choice == "p":
    user_choice = game_options[1]
    print(f"Player({game_options[1]}): CPU ({computer_choice})")
  elif user_choice == "s":
    user_choice = game_options[2]
    print(f"Player({game_options[2]}): CPU ({computer_choice})")

 
  if user_choice == computer_choice:
      print("It's a tie")
      continue
  if user_choice == "Rock" and computer_choice == "Paper":
    print("CPU wins!")
  elif computer_choice == "Rock" and user_choice == "Paper":
    print("You win")
  elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You win!")
  elif user_choice == "Scissors" and computer_choice == "Rock":
    print("CPU wins!")
  elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You win!")
  elif computer_choice == "Paper" and user_choice == "Scissors":
    print("CPU wins")
  
  break