# Create analytics.py with class SalesReport
# Methods:
#     total()
#     average()
# Import class, create object, calculate metrics.
import analytics
data = [1200, 800, 600, 400]
sales_data = analytics.Analytics(data)
print(f'Total sales : {sales_data.total()}')
print(f'Average sales : {sales_data.average()}')
