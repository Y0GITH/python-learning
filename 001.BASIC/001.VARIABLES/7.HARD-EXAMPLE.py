# A dataset contains:
# Total website visits = 18,000
# Number of conversions = 1,260
# Using variables, calculate and store the conversion rate (%) rounded to 2 decimal places.
Total_website_visits = 18000
Number_of_conversions = 1260
conversion_rate = (Number_of_conversions/Total_website_visits)*100
conversion_rate = round(conversion_rate,2)
print("conversion_rate is ",conversion_rate,"%")