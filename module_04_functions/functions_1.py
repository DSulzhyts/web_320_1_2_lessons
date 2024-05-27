def with_tax(value, tax_percentage):
    total = value + value * tax_percentage / 100
    return total


my_total = with_tax(10000, 10)
print(f"Сумма с налогом {my_total}")

price = 60000
nds = 20

my_total_salary = with_tax(price, nds)
print(f"Сумма с налогом {my_total_salary}")

