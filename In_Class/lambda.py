even = lambda x: x % 2 == 0

print(even(5))

nums = [4, 7, 10, 15, 20, 30, 35]

evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)