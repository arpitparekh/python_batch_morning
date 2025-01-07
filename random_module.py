import random
# rock paper scissors
list = ["rock", "paper", "scissors"]

user_points = 0
computer_points = 0

while True:
  n = int(input("Please Enter 101 for exit: and 102 for new game:\n"))

  if(n==101):
    print("User Points:", user_points)
    print("Computer Points:", computer_points)
    if(user_points > computer_points):
      print("You Win the overall game")
    elif(user_points < computer_points):
      print("You Lose the overall game")
    else:
      print("Tie")

    break
  elif(n==102):
    user_choice = input("Enter Your Choice:")
    computer_choice = random.choice(list)
    print("Computer Choice:", computer_choice)

    if user_choice == computer_choice:
      print("Tie")
      user_points += 0.5
      computer_points += 0.5

    elif user_choice == "rock" and computer_choice == "scissors":
      print("You Win")
      user_points += 1.0

    elif user_choice == "rock" and computer_choice == "paper":
      print("You Lose")
      computer_points += 1.0

    elif user_choice == "paper" and computer_choice == "rock":
      print("You Win")
      user_points += 1.0

    elif user_choice == "paper" and computer_choice == "scissors":
      print("You Lose")
      computer_points += 1.0

    elif user_choice == "scissors" and computer_choice == "paper":
      print("You Win")
      user_points += 1.0

    elif user_choice == "scissors" and computer_choice == "rock":
      print("You Lose")
      computer_points += 1.0

    else:
      print("Invalid Input")
  else:
    print("Invalid Input")



