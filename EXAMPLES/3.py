# unpacking a list and removing the brackets.
apple = [1,2,3,4]
a,b,*c = apple
print(a)
print(b)
d= ", ".join(map(str,c))
print(d)