# Количество человек
num_people = 5000

# Открываем файл для записи
with open('raffle_numbers.txt', 'w') as file:
    # Генерируем номера и записываем их в файл
    for i in range(1, num_people + 1):
        # Форматируем номер с ведущими нулями
        number = f"{i:04d}"
        # Записываем строку в файл
        file.write(f"{number} {number}\n")

print(f"Номера для розыгрыша записаны в файл 'raffle_numbers.txt'.")