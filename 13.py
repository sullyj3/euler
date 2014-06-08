numbers_file = open("13")
num_list = [ int(num[:51]) for num in numbers_file.readlines() ]
print(num_list)
print(len(str(num_list[0])))

total = sum(num_list)
print(total)
print(str(total)[:10])

