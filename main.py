# PYTHON STUDENT REVIEWER - LESSON 1 BASIC PYTHON SYNTAX
print("===== PYTHON STUDENT REVIEWER =====")

# Student Information
student_name = input("Enter your name: ")
student_age = input("Enter your age: ")
print("Welcome", student_name, ", Age:", student_age)

# Lesson Selection
print("Choose your lesson:")
print("1 - Lesson 1 Basic Python Syntax")
print("2 - Lesson 2 Conditional Statements in Python")
print("3 - Lesson 3 Logical Operators")
print("4 - Lesson 4 Introduction to Iteration and loops")
choice = input("Enter lesson number: ")

# LESSON 1 BASIC PYTHON SYNTAX
if choice == "1":
    print("===== LESSON 1: BASIC PYTHON SYNTAX =====")
    print("1. VARIABLES & VARIABLE DECLARATION")
    print("A variable stores data inside the program, assigned using the = sign")
    print("Syntax Sample:")
    print('''name = "Maria"
    age = 20
    grade = 89.
    is_enrolled = True''')
    
    print("="*100)
    print("2. FOUR BASIC PYTHON DATA TYPES")
    print("int = whole numbers, float = decimal numbers, str = text, bool = True or False")
    
    print("="*100)
    print("3. PRINT() / OUTPUT VARIABLES")
    print("Meaning: print() displays values on the screen")
    print("Syntax Sample:")
    print('''a = "I"
    b = "LOVE"
    c = "CCST"
    print(a, b, c)
    print(a + b + c)''')
    
    print("="*100)
    print("4. ARITHMETIC OPERATORS & EXPRESSIONS")
    print("Meaning: Operators perform mathematical calculations, Python uses PEMDAS")
    print("Syntax Sample:")
    print('''a = 10
    b = 5
    result = a + b
    print("The result is:", result)''')

    print("="*100)
    print("5. INPUT() FUNCTION & TYPE CONVERSION")
    print("Meaning: input() accepts user data; we convert string input into int or float")
    print("Syntax Sample:")
    print('''name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    grade = float(input("Enter your final grade: "))
    print(f"Student: {student_name}, Age: {student_age}, Final Grade: {grade}")''')

    # QUIZ START
    print("START QUIZ! Choose the correct letter (A‑D)")
    score = 0

    # Q1
    print("Q1: Which data type stores whole numbers?")
    print("   A) str")
    print("   B) int")
    print("   C) float")
    print("   D) bool")
    ans1 = input("Your answer (A/B/C/D): ").upper()
    if ans1 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q2
    print("Q2: Which symbol is used for assignment in Python?")
    print("   A) +")
    print("   B) =")
    print("   C) *")
    print("   D) /")
    ans2 = input("Your answer (A/B/C/D): ").upper()
    if ans2 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q3
    print("Q3: What does print() do?")
    print("   A) Stores data")
    print("   B) Displays output")
    print("   C) Accepts input")
    print("   D) Converts type")
    ans3 = input("Your answer (A/B/C/D): ").upper()
    if ans3 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q4
    print("Q4: What is the result of 10 % 3?")
    print("   A) 1")
    print("   B) 3")
    print("   C) 0")
    print("   D) 13")
    ans4 = input("Your answer (A/B/C/D): ").upper()
    if ans4 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q5
    print("Q5: Which data type holds True or False?")
    print("   A) int")
    print("   B) str")
    print("   C) bool")
    print("   D) float")
    ans5 = input("Your answer (A/B/C/D): ").upper()
    if ans5 == "C":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: C")

    # Q6
    print("Q6: What is the result of 2 ** 3?")
    print("   A) 5")
    print("   B) 6")
    print("   C) 8")
    print("   D) 9")
    ans6 = input("Your answer (A/B/C/D): ").upper()
    if ans6 == "C":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: C")

    
    print("Q7: What is the default data type of value from input()?")
    print("   A) int")
    print("   B) str")
    print("   C) float")
    print("   D) bool")
    ans7 = input("Your answer (A/B/C/D): ").upper()
    if ans7 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q8
    print("Q8: Which operator is floor division?")
    print("   A) /")
    print("   B) //")
    print("   C) %")
    print("   D) **")
    ans8 = input("Your answer (A/B/C/D): ").upper()
    if ans8 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q9
    print("Q9: grade = 89.5 is an example of which data type?")
    print("   A) float")
    print("   B) int")
    print("   C) str")
    print("   D) bool")
    ans9 = input("Your answer (A/B/C/D): ").upper()
    if ans9 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q10
    print("Q10: PEMDAS stands for the order of what?")
    print("   A) Variables")
    print("   B) Operations")
    print("   C) Data")
    print("   D) Input")
    ans10 = input("Your answer (A/B/C/D): ").upper()
    if ans10 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # FINAL SCORE
    print("QUIZ FINISHED! YOUR SCORE IS", score, "/10")


# LESSON2 CONDITIONAL STATEMENTS
elif choice == "2":
    print("===== LESSON 2: CONDITIONAL STATEMENTS IN PYTHON =====")

    print("1. INTRODUCTION TO CONDITIONAL STATEMENTS")
    print("- A conditional statement lets the program make decisions. It checks if a condition is True or False before running a block of code.")
    print("Basic Syntax:")
    print('''if condition:
    statement''')
    print("Syntax Sample:")
    print('''age = 18
    if age >= 18:
       print("You are an adult.")''')
    
    print("="*100)
    print("2. RELATIONAL / COMPARISON OPERATORS")
    print("- Relational operators compare two values. The result will always be True or False.")
    print("List of Operators:")
    print(" == Equal to")
    print(" != Not equal to")
    print(" > Greater than")
    print(" < Less than")
    print(" >= Greater than or equal to")
    print(" <= Less than or equal to")
    print("Syntax Sample:")
    print('''score = 85
    print(score >= 75)''')
    
    print("="*100)
    print("3. THE IF STATEMENT")
    print("- The if statement runs the indented code block ONLY when the condition is True. If the condition is False, it skips that block.")
    print("Syntax Sample:")
    print('''age = 20
    if age >= 18:
       print("You are an adult.")''')
    
    print("="*100)
    print("4. THE IF‑ELSE STATEMENT")
    print("- If‑else gives an alternative action when the if condition is False. Only one block will run, either if or else.")
    print("Syntax Sample:")
    print('''score = 65
    if score >= 75:
       print("Passed")
    else:
       print("Failed")''')

    print("="*100)
    print("5. THE IF‑ELIF‑ELSE STATEMENT")
    print("- Elif is used when there are many conditions to check. Python checks conditions from top to bottom and runs the FIRST condition that becomes True.")
    print("Syntax Sample:")
    print('''score = 85
    if score >= 90:
         print("Excellent")
    elif score >= 80:
         print("Very Good")
    elif score >= 75:
         print("Passed")
    else:
    print("Failed")''')
    
    print("="*100)
    print("6. NESTED CONDITION IN PYTHON")
    print("- A nested condition means placing one condition inside another condition. The inner condition will only be checked if the outer condition is True.")
    print("Syntax Sample:")
    print('''gender = input("Enter gender (M/F): ")
    age = int(input("Enter age: "))
    if gender == "M":
        if age >= 21:
          print("You are a MALE DEBUTANT.")
        else:
            print("You are a male, but not a debutant yet.")
    else:
        if age >= 18:
          print("You are a FEMALE DEBUTANT.")
        else:
          print("You are a female, but not a debutant yet.")''')

    # QUIZ START
    print("START QUIZ! Choose the correct letter (A‑D)")
    score = 0

    # Q1
    print("Q1: What does a conditional statement allow a program to do?")
    print("   A) Store variables")
    print("   B) Make decisions based on True or False")
    print("   C) Print text only")
    print("   D) Accept input")
    ans1 = input("Your answer (A/B/C/D): ").upper()
    if ans1 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q2
    print("Q2: Which operator means equal to?")
    print("   A) =")
    print("   B) ==")
    print("   C) >")
    print("   D) <")
    ans2 = input("Your answer (A/B/C/D): ").upper()
    if ans2 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q3
    print("Q3: Which operator means greater than or equal to?")
    print("   A) >")
    print("   B) <")
    print("   C) >=")
    print("   D) <=")
    ans3 = input("Your answer (A/B/C/D): ").upper()
    if ans3 == "C":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: C")

    # Q4
    print("Q4: When will the if block run?")
    print("   A) When condition is True")
    print("   B) When condition is False")
    print("   C) Always runs")
    print("   D) Never runs")
    ans4 = input("Your answer (A/B/C/D): ").upper()
    if ans4 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q5
    print("Q5: What is the purpose of else?")
    print("   A) It runs when if condition is True")
    print("   B) It runs when if condition is False")
    print("   C) It checks another condition")
    print("   D) It stops the program")
    ans5 = input("Your answer (A/B/C/D): ").upper()
    if ans5 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q6
    print("Q6: What does elif stand for?")
    print("   A) Else if")
    print("   B) End if")
    print("   C) Equal if")
    print("   D) Exit if")
    ans6 = input("Your answer (A/B/C/D): ").upper()
    if ans6 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q7
    print("Q7: What is a nested condition?")
    print("   A) Two separate if statements")
    print("   B) One condition placed inside another condition")
    print("   C) Only using else")
    print("   D) Comparing numbers")
    ans7 = input("Your answer (A/B/C/D): ").upper()
    if ans7 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q8
    print("Q8: What is the result of 10 >= 10?")
    print("   A) True")
    print("   B) False")
    print("   C) 10")
    print("   D) 0")
    ans8 = input("Your answer (A/B/C/D): ").upper()
    if ans8 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q9
    print("Q9: Which symbol means less than or equal to?")
    print("   A) <")
    print("   B) >")
    print("   C) <=")
    print("   D) >=")
    ans9 = input("Your answer (A/B/C/D): ").upper()
    if ans9 == "C":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: C")

    # Q10
    print("Q10: Python checks elif conditions in what order?")
    print("   A) Bottom to top")
    print("   B) Top to bottom")
    print("   C) Random order")
    print("   D) Only the last condition")
    ans10 = input("Your answer (A/B/C/D): ").upper()
    if ans10 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # FINAL SCORE
    print("QUIZ FINISHED! YOUR SCORE IS", score, "/10")

# LESSON 3 LOGICAL OPERATORS
if choice == "3":
    print("===== LESSON 3: LOGICAL OPERATORS =====")

    print("1. WHAT ARE LOGICAL OPERATORS?")
    print("Meaning: Logical operators combine or reverse conditions inside a Python program. They are commonly used together with if, elif, and else statements. Python has three logical operators: and, or, not.")
    print("Three Logical Operators:")
    print(" and Both conditions must be True")
    print(" or At least one condition must be True")
    print(" not Reverses the result of a condition")
    print("Syntax Sample:")
    print('''age = 20
    if age >= 18 and age <= 60:
       print("Allowed")''')
    
    print("="*100)
    print("2. THE AND OPERATOR")
    print("Meaning: The and operator returns True ONLY when ALL conditions are True. If one condition becomes False, the whole statement becomes False.")
    print("Syntax Sample:")
    print('''age = 20
    has_id = True
    if age >= 18 and has_id:
       print("You are allowed to enter.")
    else:
       print("You are not allowed to enter.")''')
    
    print("="*100)
    print("3. THE OR OPERATOR")
    print("Meaning: The or operator returns True when AT LEAST ONE condition is True. It will only return False when both conditions are False.")
    print("Syntax Sample:")
    print('''day = "Saturday"
    if day == "Saturday" or day == "Sunday":
       print("It's the weekend!")
    else:
       print("It's a regular school day.")''')
    
    print("="*100)
    print("4. THE NOT OPERATOR")
    print("Meaning: The not operator reverses the result of a condition. True becomes False, and False becomes True.")
    print("Syntax Sample:")
    print('''is_raining = False
    if not is_raining:
       print("You can go outside.")
    else:
       print("Bring an umbrella.")''')

    # QUIZ START
    print("START QUIZ! Choose the correct letter (A‑D)")
    score = 0

    # Q1
    print("Q1: What is the purpose of logical operators in Python?")
    print("   A) Combine or reverse conditions")
    print("   B) Store numbers only")
    print("   C) Print text")
    print("   D) Create variables")
    ans1 = input("Your answer (A/B/C/D): ").upper()
    if ans1 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q2
    print("Q2: Which logical operator requires BOTH conditions to be True?")
    print("   A) and")
    print("   B) or")
    print("   C) not")
    print("   D) equal")
    ans2 = input("Your answer (A/B/C/D): ").upper()
    if ans2 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q3
    print("Q3: Which logical operator returns True if AT LEAST ONE condition is True?")
    print("   A) and")
    print("   B) or")
    print("   C) not")
    print("   D) minus")
    ans3 = input("Your answer (A/B/C/D): ").upper()
    if ans3 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q4
    print("Q4: Which logical operator reverses the result of a condition?")
    print("   A) and")
    print("   B) or")
    print("   C) not")
    print("   D) plus")
    ans4 = input("Your answer (A/B/C/D): ").upper()
    if ans4 == "C":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: C")

    # Q5
    print("Q5: What will be the result of True and True?")
    print("   A) True")
    print("   B) False")
    print("   C) 0")
    print("   D) 100")
    ans5 = input("Your answer (A/B/C/D): ").upper()
    if ans5 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q6
    print("Q6: What will be the result of True or False?")
    print("   A) True")
    print("   B) False")
    print("   C) 5")
    print("   D) 0")
    ans6 = input("Your answer (A/B/C/D): ").upper()
    if ans6 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q7
    print("Q7: What will be the result of not False?")
    print("   A) True")
    print("   B) False")
    print("   C) 10")
    print("   D) 1")
    ans7 = input("Your answer (A/B/C/D): ").upper()
    if ans7 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q8
    print("Q8: Which statement is TRUE for the and operator?")
    print("   A) Both conditions must be True")
    print("   B) Only one condition needs to be True")
    print("   C) It always reverses the value")
    print("   D) It works only for numbers")
    ans8 = input("Your answer (A/B/C/D): ").upper()
    if ans8 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q9
    print("Q9: Which of these is NOT a Python logical operator?")
    print("   A) and")
    print("   B) or")
    print("   C) not")
    print("   D) equal")
    ans9 = input("Your answer (A/B/C/D): ").upper()
    if ans9 == "D":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: D")

    # Q10
    print("Q10: If day == 'Saturday' or day == 'Sunday', when will the condition become False?")
    print("   A) When day is Monday")
    print("   B) When day is Saturday")
    print("   C) When day is Sunday")
    print("   D) When day is weekend")
    ans10 = input("Your answer (A/B/C/D): ").upper()
    if ans10 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # FINAL SCORE
    print("QUIZ FINISHED! YOUR SCORE IS", score, "/10")
    
# LESSON 4 INTRODUCTION TO ITERATION AND LOOPS
if choice == "4":
    print("===== LESSON 4: INTRODUCTION TO ITERATION AND LOOPS =====")
    print("1. WHAT IS ITERATION AND LOOPS")
    print("Meaning: Iteration means repeating a block of code many times using a loop. Loops automate repetitive tasks so programmers do not need to write the same code repeatedly. Python uses two main loops: while loop and for loop.")
    
    print("="*100)
    print("2. WHILE LOOP")
    print("Meaning: While loop repeats code as long as the condition remains True.")
    print("Syntax Sample:")
    print('''i = 1
    while i <= 5:
       print(i)
       i = i + 1''')
    
    print("="*100)
    print("3. FOR LOOP USING RANGE()")
    print("Meaning: For loop repeats code for every item inside a sequence such as range, list, or string.")
    print("Syntax Sample:")
    print('''for i in range(1,6):
    print(i)''')

    print("4. FOR LOOP USING LIST")
    print("Syntax Sample:")
    print('''friends = ["Anna","Ben","Carla"]
    for name in friends:
        print("Hello",name)''')
    
    print("="*100)
    print("5. BREAK STATEMENT")
    print("Meaning: Break stops the loop immediately once the condition is met.")
    print("Syntax Sample:")
    print('''for i in range(1,10):
    if i == 5:
        break
    print(i)''')
    
    print("="*100)
    print("6. CONTINUE STATEMENT")
    print("Meaning: Continue skips the current iteration and moves to the next loop cycle.")
    print("Syntax Sample:")
    print('''for i in range(1,6):
    if i == 3:
        continue
    print(i)''')

    print("START QUIZ! Choose the correct letter (A‑D)")
    score = 0

    # Q1
    print("Q1: What does iteration mean?")
    print("   A) Stopping a program")
    print("   B) Repeating a block of code")
    print("   C) Creating a variable")
    print("   D) Printing text")
    ans1 = input("Your answer (A/B/C/D): ").upper()
    if ans1 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q2
    print("Q2: Which loop runs while a condition stays True?")
    print("   A) while loop")
    print("   B) for loop")
    print("   C) if statement")
    print("   D) else statement")
    ans2 = input("Your answer (A/B/C/D): ").upper()
    if ans2 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q3
    print("Q3: Which function is commonly used inside a for‑loop to generate numbers?")
    print("   A) input()")
    print("   B) print()")
    print("   C) range()")
    print("   D) type()")
    ans3 = input("Your answer (A/B/C/D): ").upper()
    if ans3 == "C":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: C")

    # Q4
    print("Q4: Which loop is best for going through every item in a list?")
    print("   A) while")
    print("   B) for")
    print("   C) if")
    print("   D) elif")
    ans4 = input("Your answer (A/B/C/D): ").upper()
    if ans4 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q5
    print("Q5: What does the break keyword do?")
    print("   A) Skips one iteration")
    print("   B) Prints a message")
    print("   C) Restarts the program")
    print("   D) Stops the loop completely")
    ans5 = input("Your answer (A/B/C/D): ").upper()
    if ans5 == "D":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: D")

    # Q6
    print("Q6: What does the continue keyword do?")
    print("   A) Skips the current iteration and proceeds to the next loop")
    print("   B) Ends the program")
    print("   C) Always makes the condition True")
    print("   D) Creates an infinite loop")
    ans6 = input("Your answer (A/B/C/D): ").upper()
    if ans6 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    # Q7
    print("Q7: What will range(1,6) generate?")
    print("   A) 1 2 3 4 5 6")
    print("   B) 0 1 2 3 4 5")
    print("   C) 1 2 3 4 5")
    print("   D) 6 5 4 3 2 1")
    ans7 = input("Your answer (A/B/C/D): ").upper()
    if ans7 == "C":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: C")

    # Q8
    print("Q8: An infinite loop happens when ________")
    print("   A) The loop stops after 5 runs")
    print("   B) We use the break statement")
    print("   C) The condition becomes False")
    print("   D) The condition always stays True")
    ans8 = input("Your answer (A/B/C/D): ").upper()
    if ans8 == "D":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: D")

    # Q9
    print("Q9: Choose the correct syntax for a while‑loop")
    print("   A) while condition")
    print("   B) while condition:")
    print("   C) while(condition)")
    print("   D) while {condition}")
    ans9 = input("Your answer (A/B/C/D): ").upper()
    if ans9 == "B":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: B")

    # Q10
    print("Q10: Why do programmers use loops?")
    print("   A) To repeat tasks automatically")
    print("   B) To make the program run slower")
    print("   C) To delete variables")
    print("   D) To stop the program immediately")
    ans10 = input("Your answer (A/B/C/D): ").upper()
    if ans10 == "A":
        print("CORRECT!")
        score = score + 1
    else:
        print("WRONG! Correct Answer: A")

    print("QUIZ FINISHED! YOUR SCORE IS", score, "/10")

elif choice == "1":
    print("Paste the full Lesson 1 here")

elif choice == "2":
    print("Paste the full Lesson 2 here")

elif choice =="3":
     print("Paste the full lesson 3 here")

else:
    print("Invalid selection, please restart the program and choose 1,2,3, or 4")

print("=",*50)
