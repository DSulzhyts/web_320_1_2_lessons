items_sum = 0
items_count = 0
row_index = 0

with open(r'test_path_2\shopping.txt', encoding='utf-8') as file:
    for item in file:
        row_index += 1
        if item.count(':') == 2:
            temp_data = item.strip().split(':')
        elif item.count('|') == 2:
            temp_data = item.strip().split('|')
        else:
            print(f"В ряду {row_index} есть ошибка!!!!")
            continue
        item_data, quantity, price = temp_data
        items_count += 1
        items_sum += float(price) * float(quantity)

print(f"В списке {items_count} покупок, на сумму {items_sum} рублей!")






