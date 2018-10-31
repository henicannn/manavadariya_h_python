def greetings ():
    print("Hello from the greetings function")


# the greetings function just says hello
# invoke or call the function
greetings()


def greetingsWithArgs(msg):
    # print the msg variable
    print("now we're saying", msg, "from another function")


greetingsWithArgs("Hey..!!!, Ssup..!!!")
greetingsWithArgs("Something completely different.")
greetingsWithArgs("Running it again.")

# variables and scope
myNumberVariable = 10


# returning values from the functions (very powerful)
def someMath(num1=2, num2=4):
    global myNumberVariable

    myNumberVariable = num1 + num2
    return num1 + num2


sum = someMath()
print("We are doing some math and getting", sum)

sum = someMath(10, 15)
print("another math operation with", sum, "as the result")

# variables and scope
myNumberVariable = 10