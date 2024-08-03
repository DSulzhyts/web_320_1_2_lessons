# def get_order_total_summ(order_total, country):
#     total = 0
#
#     for items_price_quant in order_total.values():
#         total += items_price_quant[0] * items_price_quant[1]
#
#     if country == "RU":
#         total += total * 0.2  # НДС
#     elif country == "KZ":
#         total += total * 0.12  # KZ ҚҚС
#     elif country == "UAE":
#         total += total * 0.05  # UAE VAT
#
#     return total


def get_order_total_summ(order_total, country):
    total = 0

    for items_price_quant in order_total.values():
        total += items_price_quant[0] * items_price_quant[1]

    total += total * get_tax_amount(country)
    return total


def get_tax_amount(country):
    if country == "RU":
        return 0.2  # НДС
    elif country == "KZ":
        return 0.12  # KZ ҚҚС
    elif country == "UAE":
        return 0.05  # UAE VAT


order_1 = {
    "Тормозные колодки": [100, 10],
    "Диск сцепления": [250, 4],
    "Фильтр масляный": [20, 50]
}

print(get_order_total_summ(order_1, "RU"))
print(get_order_total_summ(order_1, "KZ"))
print(get_order_total_summ(order_1, "UAE"))
