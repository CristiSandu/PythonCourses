#  Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below. 


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
   # print(num)
    try:
        n = float(num)
    except:
        print('Invalid input')
        continue
    if largest is None :
        largest = n
    if smallest is None :
        smallest = n    

    if n > largest :
        largest = n
    elif n < smallest :
        smallest = n

print("Maximum", int(largest))
print("Minimum", int (smallest))
