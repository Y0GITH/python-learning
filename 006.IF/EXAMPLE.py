# price of a house is $1M. 
# if buyer has goodcredit, 
#   they need to put down 10%
# otherwise 
#   they need to put down 20% 

price = 1000000
credit = input("enter the credit rating : ").upper()
if credit == "GOOD":
    down_pay = price * 0.10
else:
    down_pay = price * 0.20
print(f'the down payment is ${round(down_pay)}'.title())
