# enter the weight in kilo or in pounds and get the output in opposit to entered
weight = int(input(f'Enter your weight : '))
measure = input(f"kilo is 'K' and pounds is 'P' : ").upper()
if measure == "K":
    weight_scaled = weight * 4.5
    print(f'The wight is {weight_scaled} pounds')
elif measure == "P":
    weight_scaled = weight / 4.5
    print(f'The wight is {weight_scaled} kilo')
elif (measure != "K" or "P") and (weight != int ):
    print(f'invalid input, set it correctly.')