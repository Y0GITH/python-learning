# Take total website visits and number of conversions as input and calculate the conversion rate (%) rounded to 2 decimals.
total_website_visits = int(input("Enter the total website visits : "))
number_of_conversions = int(input("Enter the total number of conversions : "))
conversion_rate = ((number_of_conversions/total_website_visits)*100)
print("conversion rate is ",conversion_rate,"%")