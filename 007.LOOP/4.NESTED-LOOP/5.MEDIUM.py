# Print this pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
for i in range(1,5):
    for j in range(1,i+1):  # (1,i+1)  
        print(f'{j}',end=" ")
    print()    
# (1,i+1) cauz, 
# if only i then make no sence as i in a single value so u cant loop a single int value
# if range(i) then it also take the 0 and print form 0 then 1 then 2 and so on 
# when we specify it to range(1,i+1) then the range staart form 1 and ends before i+1 before value 
# eg if i = 2
# then the range is range(1,3) and the print will be 1,2 only as 3 will be ignored
