#!/bin/python

a = 5
b = 10

# Equals
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

# Not Equals
if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")

# Less than
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

# Less than or equal to
if a <= b:
    print("a is less than or equal to b")
else:
    print("a is neither less than nor equal to b")

# Greater than
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Greater than or equal to
if a >= b:
    print("a is greater than or equal to b")
else:
    print("a is neither greater than nor equal to b")



# elif Exercise
x = 10

# Check if x is greater than or equal to 20
if x >= 20:
    print("x is greater than or equal to 20")
    
# Check if x is less than or equal to 15
elif x < 15:
    print("x is less than 15 ")


# With Else

# Check if x is greater than or equal to 20
if x >= 20:
    print("x is greater than or equal to 20")
    
# If x is not greater than or equal to 20, check if x is greater than or equal to 15
elif x >= 15:
    print("x is greater than or equal to 15 but less than 20")
    
# If both the above conditions are not met, print a message
else:
    print("x is less than 15")


#### Stretch Goals
a = 5
b = 10

## If Statement with 2 conditions and "AND" operator

# Check if both a is less than 7 and b is greater than 8
if a < 7 and b > 8:
    print("Both conditions are true")
else:
    print("At least one condition is false")


## If Statement with 2 conditions and "OR" operator
# Check if either a is less than 3 or b is greater than 15
if a < 3 or b > 15:
    print("At least one condition is true")
else:
    print("Both conditions are false")


# Nested Statement
x = 15
# Check if x is greater than 10
if x > 10:
    print("x is greater than 10")
    
    # Check if x is greater than 20
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is not greater than 20")
else:
    print("x is not greater than 10")


# Pass Condition
x = 5
# Check if x is greater than 10
if x > 10:
    print("x is greater than 10")
else:
    # Use pass to do nothing if the condition is not met
    pass






