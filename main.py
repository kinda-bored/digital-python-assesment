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

#this is the start menu
def start_menu():
    print("STUDY!!!")
    print("welcome to study")
    input("what is your name? ")
    print("what would you like to study?")
    subject_choice()
    
#this is where u pick what subject u want to study
def subject_choice():
    print("1. trigonometry")
    choice = input("enter the number of the subject you want to study: ")
    if choice == "1":
        start_math()
    else:
        print("invalid choice")
        subject_choice()
        
# this is where u slect how many questions u want to awnser
def start_math():
        while True:
            try:
                num_questions = int(input("how many questions do you want to awnser? "))
                if num_questions < 1:
                    print("please enter a number higher than 0")
                    continue
                break
            except ValueError:  
                print("please enter a number")
        question_maker(num_questions)
        
#this is where the lengths and sides are picked and the awnsers are checked
def question_maker(num_questions):
    score = 0
    asked = 0
    attempts = 0
    max_attempts = num_questions * 10  # safety limit
    while asked < num_questions and attempts < max_attempts:
        attempts += 1
        # pick two different sides
        side1, side2 = random.sample(sides, 2)
        num1 = random.choice(numbers1)
        num2 = random.choice(numbers1)
        result = caclculate(side1, side2, num1, num2)
        if result is None:
            # invalid question — skip and do not increment `asked`
            continue
        user_ans = quiz(side1, side2, num1, num2)
        if abs(user_ans - result) < 1e-2:
            print("correct")
            print(attempts)
            score += 1
        else:
            print("wrong")
            print(f"the correct answer is {round(result, 2)}")
            print(attempts)
            print(asked)
        asked += 1
    if attempts >= max_attempts and asked < num_questions:
        print("Could not generate enough valid questions; finishing early.")
    end_menu_math(score, asked)
    
#this is where the question is asked
def quiz(side1, side2, num1, num2):
    while True:
        try:
            print(f"side one is {side1} and is {num1} long and side two is {side2} and is {num2} long")
            print("what is the angle?")
            return float(input("what is the answer? "))
        except ValueError:
            print("please enter a number")

#this is where the angle is caclculated is that the sides and lengths are vaild and so the anwer is generated
def caclculate(side1, side2, num1, num2):
    k1 = side1.lower(); k2 = side2.lower()
    if k1 == k2 or k1 not in ("h","o","a") or k2 not in ("h","o","a"):
        return None
    try:
        length1 = float(num1); length2 = float(num2)
    except ValueError:
        return None
    if length1 <= 0 or length2 <= 0:
        return None
    try:
        if k1 == "h" and k2 == "a":
            ratio = length2 / length1
            if abs(ratio) > 1: return None
            return math.degrees(math.acos(ratio))
        if k1 == "a" and k2 == "h":
            ratio = length1 / length2
            if abs(ratio) > 1: return None
            return math.degrees(math.acos(ratio))
        if k1 == "h" and k2 == "o":
            ratio = length2 / length1
            if abs(ratio) > 1: return None
            return math.degrees(math.asin(ratio))
        if k1 == "o" and k2 == "h":
            ratio = length1 / length2
            if abs(ratio) > 1: return None
            return math.degrees(math.asin(ratio))
        if k1 == "o" and k2 == "a":
            if length2 == 0: return None
            return math.degrees(math.atan(length1 / length2))
        if k1 == "a" and k2 == "o":
            if length1 == 0: return None
            return math.degrees(math.atan(length2 / length1))
    except ZeroDivisionError:
        return None
    return None

#this is where the score is displayed at the end and asked if u want to play again
def end_menu_math(score, num_questions):
    print(f"Score: {score}/{num_questions}")
    play_again = input("press 1 to return to the main menu or any other key to exit: ")
    if play_again == "1":
        start_math()
    else:
        exit()
        
#this starts the program    
start_menu()