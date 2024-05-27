my_list = [i * i for i in range(11) if i % 2 == 0]
print(my_list)

square_list = []
for i in range(11):
    if i % 2 == 0:
        square_list.append(i * i)
print(square_list)

customers = ["Bob", "Joe", "Anna", "Bob", "Nick"]
customers_filtered = [customer for customer in customers if customer != 'Bob' and customer != 'Joe']
print(customers_filtered)

customers = ["Bob", "Joe", "Anna", "Bob", "Nick"]
customers_filtered_1 = []

for customer in customers:
    if customer != "Bob" and customer != "Joe":
        customers_filtered_1.append(customer)

print(customers_filtered_1)

product_list = [x * y for x in range(1, 4) for y in range(1, 4)]
print(product_list)

product_list_1 = []
for x in range(1, 4):
    for y in range(1, 4):
        product_list_1.append(x * y)

print(product_list_1)
