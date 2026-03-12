# no make a list of 1 to 10
# num = []
# for i in range(1,10):
#     num.append(i)
# print(num)    
num = [n for n in range(11)]
print(num)

# to add only even number 
# num = []
# for i in range(10):
#     if i%2==0:
#         num.append(i)
# print(num)        
num = [n for n in range(10) if n%2==0 ]
print(num)

# make a nested loop of number and its identity
# data = []
# for n in range(6):
#     data.append((n, "even" if n%2==0 else "odd"))
# print(data) 
data = [(n,'even' if n%2==0 else 'odd') for n in range(6)]
print(data)
