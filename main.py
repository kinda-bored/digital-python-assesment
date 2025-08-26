import random
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
    num_questions = int(input("how many questions do you want to awnser?"))
    if num_questions < 1:
        print("please pick a number higher than 0")
        start_menu()
    else:
        score = 0
        question_maker(num_questions)
    
   
#question maker function
def question_maker(num_questions):
    side1 = random.choice(sides)
    side2 = random.choice(sides)
    if side1 == side2:
        question_maker(num_questions) 
    else:
        for i in range(num_questions):
            num1 =  random.choice(numbers1)
            num2 =  random.choice(numbers1)
            caclculate(side1, side2, num1, num2)
            print(f"what is the awnser of {num1} {side1} + {num2} {side2}")
            quiz()


#quiz function
def quiz():
    awnser = int(input("what is the awnser?"))
    if awnser == int(awnser):
        return awnser
    else:
        print("please enter a number")
        quiz()
      

#caclculate function
def caclculate( side1, side2, awnser):
    if awnser == 1:
        print("correct")
    else:
        print("wrong")
        print(f"the correct awnser is {awnser}")
      
    

if __name__ == "__main__":
    start_menu()