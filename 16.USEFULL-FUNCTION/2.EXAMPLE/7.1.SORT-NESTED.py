# sorting a nested list 
# before sorting it zip and rank them in last
names = ['anu','ram','sam','zah']
marks= [12,14,10,20]
data = list(zip(names,marks))
sorted_data = sorted(data,key=lambda x: x[1],reverse=True)
for rank,(name,mark) in enumerate(sorted_data,start=1):
    print(f'Rank - {rank}, Name - {name}, Marks - {mark}')