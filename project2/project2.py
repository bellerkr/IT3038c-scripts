import random
import os
import re

os.system('cls' if os.name=='nt' else 'clear')

while (1 < 2):
    
    
    
    print("Rock, Paper, Scissors - Shoot!")
    
    Selection = raw_input("Choose one of the floowing: [R]ock], [P]aper, or [S]cissors: ")
    
    if not re.match("[SsRrPp]", (Selection)):
        
        print("Please choose a letter:")
        
        print("[R]ock, [S]cissors or [P]aper.")
        
        continue
    
    
    print("Your choice was: " + Selection)
    
    choices = ['R', 'P', 'S']
    
    randomChoice = random.choice(choices)
    
    print("I chose: " + randomChoice)
    
    if randomChoice == str.upper(Selection):
        print("Tie ")
        
        if randomChoice == str("R") and str.upper(Selection) == str("P")
    
    elif randomChoice == str('R') and Selection.upper() == str('S'):      
        print("Scissors beats rock, I win ")
        continue
    
    elif randomChoice == str('S') and Selection.upper() == str('P'):      
        print("Scissors beats paper! I win ")
        continue
    
    elif randomChoice == str('P') and Selection.upper() == str('R'):      
        print("Paper beats rock, I win ")
        continue
    
    else:       
        print("You win!")
