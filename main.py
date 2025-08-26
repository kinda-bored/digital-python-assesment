import random
import math
numbers1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
    "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
    "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
    "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
    "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
    "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
    "81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
    "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"
]


sides = ["H","O","A"]

#start menu function
def start_menu(result):
    print("STUDY!!!")
    while True:
        try:
            num_questions = int(input("how many questions do you want to awnser? "))
            if num_questions < 1:
                print("please enter a number higher than 0")
                continue
            break
        except ValueError:
            print("please enter a number")
    score = 0
    question_maker(num_questions,result)
    
   
#question maker function
def question_maker(num_questions, result):
        for i in range(num_questions):
            side1 = random.choice(sides)
            side2 = random.choice(sides)
            if side1 == side2:
                question_maker(num_questions)
            num1 = random.choice(numbers1)
            num2 = random.choice(numbers1)
            quiz(side1, side2, num1, num2, result)

#quiz function
def quiz(side1, side2, num1, num2, result):
    while True:
        try:
            print(f"side one is {side1} and is {num1} long and side two is {side2} and is {num2} long")
            awnser = float(input("what is the awnser? "))
            return awnser
        except ValueError:
            print("please enter a number")
        correct = result
        user_ans = awnser
        if user_ans == correct:
            print("correct")
        else:
            print("wrong")
            print(f"the correct awnser is {correct}")
        
      

#caclculate function
def caclculate(side1, side2, num1, num2, num_questions):
   notdone = True
   while notdone:
        try:
            known1 = int(side1)
            known2 = int(side2)
            if  known2.lower() in ["h", "a", "o"] and known1.lower() in ["h", "a", "o"] and known1 != known2:
                length1 = float(num1)
                length2 = float(num2)
                if known1 == "h" and known2 == "a":
                    result = math.degrees(math.acos(length2/length1))
                if known1 == "a" and known2 == "h":
                    result = math.degrees(math.acos(length1/length2))
                if known1 == "h" and known2 == "o":
                    result = math.degrees(math.asin(length2/length1))
                if known1 == "o" and known2 == "h":
                    result = math.degrees(math.asin(length1/length2))                   
                if known1 == "o" and known2 == "a":
                    result = math.degrees(math.atan(length1/length2))                
                if known1 == "a" and known2 == "o":
                    result = math.degrees(math.atan(length2/length1))                  
                notdone = False
                return result
        except ValueError:
            print("error in calculation")
            print(f"debug info: known1 = {known1}, known2 = {known2}, length1 = {length1}, length2 = {length2}")
            input("press Y to continue or Z to try again")
            if input().lower() == "Z":
                caclculate(side1, side2, num1, num2)
            else:  
                question_maker(num_questions)
                
            
            return None
            
            
           
 
    

start_menu("")