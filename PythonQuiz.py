print("Welcome to my python quiz!")
play = input("Do you want to play? (y/n): ").upper()

if play != "Y":
    quit()

score = 0

print("Question 1: What is the function of print in python? ")
print("A. To print \nB. To display \nC. Trick question. There's no print in python.")
answer = input("Enter answer to Question 1: ").upper()
if answer == "B":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

print("Question 2: Which symbol is used when writing comments?")
print("A. # \nB. @ \nC. $")
answer = input("Enter answer to Question 2: ").upper()
if answer == "A":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

print("Question 3: Which of the following is a string? ")
print("A. '21' \nB. Hello \nC. Both A and B ")
answer = input("Enter answer to Question 3: ").upper()
if answer == "A":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT")

print("Question 4: How can the integer 21 be converted into a string?")
print("A. By adding quotation marks \nB. That's impossible \nC. string(21)")
answer = input("Enter answer to Question 4: ").upper()
if answer == "C":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

print("Question 5: Given the variable x = 5, how can you display the value of x?")
print("A. By writing the value \nB. print(x) \nC. Print(x)")
answer = input("Enter answer to Question 5: ").upper()
if answer == "B":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

print("Question 6: Which of the following is a list?")
print("A. {'a', 'b'} \nB. ('a', 'b') \nC. ['a', 'b']")
answer = input("Enter answer to Question 6: ").upper()
if answer == "C":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

print("Question 7: Which of the following is true about lists?")
print("A. They are unchangeable \nB. They only group related data \nC. None")
answer = input("Enter answer to Question 7: ").upper()
if answer == "C":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

print("Question 8: Python is a case sensitive language")
print("A. True \nB. False \nC. It depends")
answer = input("Enter answer to Question 8: ").upper()
if answer == "A":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

print("Question 9: The != sign means:")
print("A. That does not exist \nB. Not equal to \nC. Exclamation")
answer = input("Enter answer to Question 9: ").upper()
if answer == "B":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

print("Question 10: What is the difference between lists and tuples?")
print("A. List is another name for tuple \nB. Tuples are unchangeable \nC. Only one allows duplicates")
answer = input("Enter answer to Question 10: ").upper()
if answer == "B":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT")

print(f"You got {score} questions correct.")
if score == 10:
    print("You are a python Mastermind!".upper())
else:
    print("Better luck next time :)".upper())