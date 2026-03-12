# 🔹 4️⃣ enumerate() — Rank Sales Agents
# You have a list of sales by agents.
#     sales = [4500, 3800, 5200, 6100, 4700]
# Task:
#     Using enumerate(), print:
#         Agent 1 → 4500
#         Agent 2 → 3800
#         Agent 3 → 5200
#         ...
# Agent numbering should start from 1.
sales = [4500, 3800, 5200, 6100, 4700]
for i,sale in enumerate(sales, start=1):
    print(f'Agent {i} -> {sale}')