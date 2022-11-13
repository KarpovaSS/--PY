import random
def get_unique_list_numbers(start=-10, stop=10,size=15 ) -> list[int]:
    list_ = []

    while len(list_) < size:
        random_num = random.randint(start, stop)
        if random_num not in list_:
            list_.append(random_num)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
