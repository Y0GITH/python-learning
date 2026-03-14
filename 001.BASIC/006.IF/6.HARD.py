# A website gives a discount only if:
#   + user is a member, and
#   + purchase amount ≥ 1000 OR coupon applied
# Write the full if condition.
purchase_amount = int(input(f'Total Purchase : '))
membership_status = input(f'are u a member [yes or no] : ').upper()
if ( purchase_amount >= 1000 ) and ( membership_status == "YES" ):
    bill_amount = purchase_amount * 0.95
else:
    bill_amount = purchase_amount    
print(f'the bill amount is ${round(bill_amount)}')        