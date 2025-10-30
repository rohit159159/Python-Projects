import random

item_list=['rock','paper','scissors']

print("🎮 Welcome to Rock-Paper-Scissors Game 🎮")
print("Type 'exit' anytime to quit the game.\n")

while True:
 user_choice=input("enter your choice: \n")
 if user_choice=='exit':
     print("Thanks for playing ! Goodbye!")
     break

 if user_choice not in item_list:
        print("❌ Invalid input! Please choose rock, paper, or scissors.\n")
        continue
    
 computer_choice=random.choice(item_list)

 print(f"user choice: {user_choice}\ncompurter choice: {computer_choice}")

 if user_choice==computer_choice:
    print("Both choice are same: it's a tie")
    
 elif user_choice=='rock':
    if computer_choice=='paper':
        print("paper covers rock: computer wins")
    else:
        print("rock smashes scissors: user win")

 elif user_choice=='paper':
    if computer_choice=='scissors':    
        print("scissors cut the paper: computer wins")
    else:
        print("paper covers rock: user win")

 elif user_choice=='scissors':
    if computer_choice=='rock':
        print("rock smashes scissors:computer wins")
    else:
        print("scissors cut the paper: user win")