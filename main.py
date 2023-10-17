import random as r

# Задання значень елементам масиву
my_array = []
for i in range(5):
    # Беру менший проміжок щоб можна було зручніше тестувати
    my_array.append([r.randint(1, 60) for j in range(5)])

# Виведення масиву в консоль як матриці
print("Двовимірний масив:")
for row in my_array:
    print(row)

print()


# Функція для суми чисел кожної колонки
def sum_columns(array):
    rows = len(array)
    cols = len(array[0])

    column_sums = [0] * cols

    for col in range(cols):
        for row in range(rows):
            column_sums[col] += array[row][col]

    return column_sums

print("Сума чисел у кожній колонці:")
print(sum_columns(my_array))
print()

# Сортування
column_sums = sum_columns(my_array)
sorted_columns = sorted(range(5), key=lambda a: column_sums[a])
sorted_array = [[row[i] for i in sorted_columns] for row in my_array]
print("Відсортований масив:")
for row in sorted_array:
    print(row)
