def my_generator():
    for num in range(50):
        yield num ** num

total = list(my_generator())
print(total)

for big_num in my_generator():
    print(big_num)