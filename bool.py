# Ask for first and second numbers from the user before we define anything
# Additionally, sure to handle exceptions correctly with the "while True:"
# This makes it so the script doesn't crash when you 
while True:
    try:
        num1 = int(input("Please enter your first number: "))
        break
    except ValueError:
        print('You have to use an integer. Try again: ')

# Same as above, except for the second input from the user
while True:
    try:
        num2 = int(input("Please enter your second number: "))
        break
    except ValueError:
        print('You have to use an integer. Try again: ')


#Create the comparison function that denotes what the assignment asked for
def comparison(a, b):
    if a > b:
        return 1 #print 1 if a is greater than b
    elif a == b:
        return 0 #print 0 if a = b
    else:
        return -1 #print -1 for everything else, which is a > b

# print the results of the user input's compare function
print('If your first number is greater than your second number')
print('then print 1. If your first number is less than your second')
print('number, then print -1. If your first number is equal to your')
print('second number, then print 0 \n', comparison(num1, num2))

# print out the results of the arguments given in the assignment
print('Test per the assignment a > b while a = 5 and b = 2:', comparison(5, 2))
print('Test per the assignment a < b while a = 2 and b = 5:', comparison(2, 5))
print('Test per the assignment a = b while a = 3 and b = 3:', comparison(3, 3))
