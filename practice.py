def even_generator(limit):
    for n in range(limit + 1):
        if n % 2 == 0:
            yield n

for number in even_generator(10):
    print(number)
