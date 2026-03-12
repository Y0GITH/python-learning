# Write a function that takes a number as input and returns whether the value is positive or negative.
def check(a):
    if a > 0:
        return "POSITIVE"
    else:
        return "NEGATIVE"
    
print(" the number is ",check(3))
print(" the number is ",check(-3))