guests_count = 0
with open('guests.txt', 'r', encoding='utf-8') as guests:
    for guest in guests:
        if len(guest) > 1:
            print(guest.strip())
            guests_count += 1

print(f"Количество гостей: {guests_count}")

with open('guests.txt', 'r', encoding='utf-8') as guests:
    guests_list = guests.readlines()
    print(guests_list)
    new_guests_count = len(guests_list)

print(''.join(guests_list))
print(f"Количество гостей: {new_guests_count}")