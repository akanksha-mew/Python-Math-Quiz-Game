import random

print(" QUESTIONS ".center(50, "~"))

print("\nChoose Difficulty Levels for Questions : \n Press [1] for Easy \n Press [2] for Medium \n Press [3] for Hard")

ch = int(input("\nEnter your Choice : "))
print("_"*50)

print("\nQuestions :")

score = 0
if ch == 1:
    ops = ['+', '-', '//', '*']

    for i in range(1, 6):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(ops)
        print(num1,operator,num2)
        sol = int(input("Enter your solution : "))
        ans = eval(str(num1) + operator + str(num2))
        if sol == ans:
            print("CORRECT\n")
            score += 1
        else:
            print("INCORRECT\n")

elif ch == 2:
    ops = ['+', '-', '//', '*']

    for i in range(1, 6):
        num1 = random.randint(100, 1000)
        num2 = random.randint(100, 1000)
        operator = random.choice(ops)
        print(num1, operator, num2)
        sol = int(input("Enter your solution : "))
        ans = eval(str(num1) + operator + str(num2))
        if sol == ans:
            print("CORRECT\n")
            score += 1
        else:
            print("INCORRECT\n")

elif ch == 3:
    ops = ['+', '-', '//', '*']

    for i in range(1, 6):
        num1 = random.randint(1000, 10000)
        num2 = random.randint(1000, 10000)
        operator = random.choice(ops)
        print(num1, operator, num2)
        sol = int(input("Enter your solution : "))
        ans = eval(str(num1) + operator + str(num2))
        if sol == ans:
            print("CORRECT\n")
            score += 1
        else:
            print("INCORRECT\n")

else:
    print("Invalid Choice")
    ch = int(input("\nPlease TRY Again : "))

print("_"*50)
print("Your Score : ", score, "out of", 5)
