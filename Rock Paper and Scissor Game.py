"""
Cases:
A - Rock
Rock - Rock = Match Tie
Rock - Paper = Rock Win
Rock - Scissor = Rock Win

B - Paper
Paper - Paper = Match Tie
Paper - Rock = Paper Win
Paper - Scissor = Scissor Win

C - Scissor
Scissor - Scissor = Scissor Win
Scissor - Paper = Scissor Win
Scissor - Rock = Rock Win

"""
import random
while True:
    print("\nRock Paper and Scissor Game")
    item=["Rock","Paper","Scissor"]
    print("Choices are Rock,Paper,Scissor")
    user=(input("Enter your Choice from Rock,Paper,Scissor or type 'Exit' to quit: ")).capitalize()

    if user == "Exit":
        print("\nThanks for playing! Goodbye!")
        break
        
    if user not in item:
        print("\nEnter Correct Input")
    else:
        comp_choice= random.choice(item)
        print(f"User Choice is: {user}, Computer Choice is: {comp_choice}")
        
        if user == comp_choice:
            print("Match Tie") 
        
        elif user == "Rock":
            if comp_choice == "Paper":
                print("Computer Win")
            else:
                print("User Win")
                
        elif user == "Scissor":
            if comp_choice == "Paper":
                print("User Win")
            else:
                print("Computer Win")
                
        elif user == "Paper":
            if comp_choice == "Scissor":
                print("Computer Win")
            else:
                print("User Win")