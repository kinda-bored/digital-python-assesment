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
def start_menu():
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
    question_maker(num_questions)

def question_maker(num_questions):
    score = 0
    for i in range(num_questions):
        side1, side2 = random.sample(sides, 2)  # ensure different sides
        num1 = random.choice(numbers1)
        num2 = random.choice(numbers1)

        result = caclculate(side1, side2, num1, num2)
        if result is None:
            print("Skipping question due to calculation error.")
            continue

        user_ans = quiz(side1, side2, num1, num2)
        if abs(user_ans - result) < 1e-3:
            print("correct")
            score += 1
        else:
            print("wrong")
            print(f"the correct awnser is {result}")
    print(f"Score: {score}/{num_questions}")

#quiz function
def quiz(side1, side2, num1, num2):
    while True:
        try:
            print(f"side one is {side1} and is {num1} long and side two is {side2} and is {num2} long")
            return float(input("what is the awnser? "))
        except ValueError:
            print("please enter a number")

#caclculate function
def caclculate(side1, side2, num1, num2):
    k1 = side1.lower(); k2 = side2.lower()
    if k1 == k2 or k1 not in ("h","o","a") or k2 not in ("h","o","a"):
        return None
    try:
        length1 = float(num1); length2 = float(num2)
        if k1 == "h" and k2 == "a":
            return math.degrees(math.acos(length2/length1))
        if k1 == "a" and k2 == "h":
            return math.degrees(math.acos(length1/length2))
        if k1 == "h" and k2 == "o":
            return math.degrees(math.asin(length2/length1))
        if k1 == "o" and k2 == "h":
            return math.degrees(math.asin(length1/length2))
        if k1 == "o" and k2 == "a":
            return math.degrees(math.atan(length1/length2))
        if k1 == "a" and k2 == "o":
            return math.degrees(math.atan(length2/length1))
    except Exception:
        return None
    return None

start_menu()