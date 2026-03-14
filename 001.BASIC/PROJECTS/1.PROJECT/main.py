import data
import analytics_engine

engine = analytics_engine.RetailAnalytics(data.transactions)

engine.generate_report()

print("\nTotal Revenue:", engine.total_revenue())

print("\nHigh Revenue Transactions:")
print(engine.high_revenue_transactions())

print("\nCategory Revenue:")
print(engine.category_revenue())

print("\nProduct Ranking:")
engine.rank_products()