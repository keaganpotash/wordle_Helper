import re

GRAY = 0
GREEN = 1
YELLOW = 2

with open('wordle_words.txt', 'r') as file:
    pattern = ""
    
    # starting patterns used for regular expression script
    green_1 = "abcdefghijklmnopqrstuvwxyz"
    green_2 = "abcdefghijklmnopqrstuvwxyz"
    green_3 = "abcdefghijklmnopqrstuvwxyz"
    green_4 = "abcdefghijklmnopqrstuvwxyz"
    green_5 = "abcdefghijklmnopqrstuvwxyz"
    yellow_1 = "."
    yellow_2 = "."
    yellow_3 = "."
    yellow_4 = "."
    yellow_5 = "."
    
    text = file.read()
    # Split the text into words   
    words = text.splitlines()
    # Read the contents of the file
    done = False
    grey_letters = ""
    
    while (done == False):
    
    #first input for grey letters within the word aka letters that are not in this wordle
        grey = input("type the grayed out letters within the word EX: adk. Else type ? if none are grey: ")
        
    # below are the input checks for each of the 5 positions of letters 
        first = input("Is the first letter yellow green or gray? type y for yellow g for green or x for gray: ")
        if (first == "y" or first == "Y"):
            f_letter = input("Type the 1st letter of the word you tried in lower case. ")
            while (len(f_letter) !=1):
                f_letter = input("Miss input. what is the first letter? ")
            green_1 = green_1.replace(f_letter, "")
            yellow_1 = f_letter
        elif (first == "g" or first == "G"):
             f_letter = input("Type the 1st letter of the word you tried in lower case. ")
             while (len(f_letter) !=1):
                f_letter = input("Miss input. what is the first letter? ")
             green_1 = f_letter
             
        second = input("Is the second letter yellow green or gray? Type y for yellow g for green or x for gray: ")
        if (second == "y" or second == "Y"):
            f_letter = input("Type the 2nd letter of the word you tried in lower case. ")
            while (len(f_letter) !=1):
                f_letter = input("Miss input. What is the second letter? ")
            green_2 = green_2.replace(f_letter, "")
            yellow_2 = f_letter
        elif (second == "g" or second == "G"):
            f_letter = input("Type the 2nd letter of the word you tried in lower case. ")
            while (len(f_letter) !=1):
                f_letter = input("Miss input. What is the second letter? ")
            green_2 = f_letter
            
        third = input("Is the third letter yellow green or gray? Type y for yellow g for green or x for gray: ")
        if (third == "y" or third == "Y"):
            f_letter = input("Type the 3rd letter of the word you tried in lower case. ")
            while (len(f_letter) !=1):
                f_letter = input("Miss input. What is the third letter? ")
            green_3 = green_3.replace(f_letter, "")
            yellow_3 = f_letter
        elif (third == "g" or third == "G"):
            f_letter = input("type the 3rd letter of the word you tried in lower case. ")
            while (len(f_letter) !=1):
                f_letter = input("miss input. what is the third letter? ")
            green_3 = f_letter
            
        fourth = input("Is the fourth letter yellow green or gray? Type y for yellow g for green or x for gray: ")
        if (fourth == "y" or fourth == "Y"):
            f_letter = input("Type the 4th letter of the word you tried in lower case. ")
            while (len(f_letter) !=1):
                f_letter = input("Miss input. What is the fourth letter? ")
            green_4 = green_4.replace(f_letter, "")
            yellow_4 = f_letter
        elif (fourth == "g" or fourth == "G"):
            f_letter = input("Type the 4th letter of the word you tried in lower case. ")
            while (len(f_letter) !=1):
                f_letter = input("Miss input. What is the fourth letter? ")
            green_4 = f_letter
            
        fifth = input("Is the fifth letter yellow green or gray? Type y for yellow g for green or x for gray: ")
        if (fifth == "y" or fifth == "Y"):
            f_letter = input("Type the 5th letter of the word you tried in lower case. ")
            while (len(f_letter) !=1):
                f_letter = input("Miss input. What is the fifth letter? ")
            green_5 = green_5.replace(f_letter, "")
            yellow_5 = f_letter
        elif (fifth == "g" or fifth == "G"):
            f_letter = input("Type the 5th letter of the word you tried in lower case. ")
            while (len(f_letter) !=1):
                f_letter = input("Miss input. What is the fifth letter? ")
            green_5 = f_letter
            
        grey_letters = grey
       # print("yellow_1 " + yellow_1)
       # print("yellow_2 " + yellow_1)
       # print("yellow_3 " + yellow_1)
       # print("yellow_4 " + yellow_1)
       # print("yellow_5 " + yellow_1)
       # print("green_1 " + green_1)
       # print("green_2 " + green_2)
       # print("green_3 " + green_3)
       # print("green_4 " + green_4)
       # print("green_5 " + green_5)
        print(grey_letters)
    # pattern for grey letters (?=.*{re.escape(yellow_2)})(?=.*{re.escape(yellow_3)})(?=.*{re.escape(yellow_4)})(?=.*{re.escape(yellow_5)})
   # {re.escape(green_2)}{re.escape(green_3)}{re.escape(green_4)}{re.escape(green_5)}
   
   # regular expression pattern using all the variables with yellow being letters that must be included, grey letters being not encluded and green letters being the possible letters in each position.
        pattern = rf'^(?=.*{yellow_1})^(?=.*{yellow_2})^(?=.*{yellow_3})^(?=.*{yellow_4})^(?=.*{yellow_5})(?!.*[{re.escape(grey_letters)}])[{re.escape(green_1)}][{re.escape(green_2)}][{re.escape(green_3)}][{re.escape(green_4)}][{re.escape(green_5)}].*$'
        
    # shortening the list of words
        words = [word for word in words if re.match(pattern, word)]
        print ("possible words" + str(words))
        print ("is the game done?")
        input_string = input("if yes type 0: ")
    # while loop break.
        if (input_string == "0"):
            done = True
        
    file.close()
        

   