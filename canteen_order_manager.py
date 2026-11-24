#Activity 2 – School Canteen Order Manager
order = []

for i in range(1,6):
    order.append(input(f"Enter Order {i}: "))
original = order




print(f"""Original Orders:
{original} """)


order.append(input("Enter additional order: "))

print(f"""Updated Orders:
{order}""")
order.insert(0, input("Enter priority order: "))

print(f"""Updated Orders:
{order}""")

search = input("Search for an order: ")
print(f"""Number of Occurrences: {order.count(search)}""")
