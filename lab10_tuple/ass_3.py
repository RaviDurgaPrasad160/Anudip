# 3.Write a Python program to calculate the sum of the numbers in a given tuple.
#  Input:
#  tuples_list = [(1, 2), (3, 4), (5, 6)]

# In question only do sum of the numbers in a given tuple
tuples_list = [(1, 2), (3, 4), (5, 6)]

total_sum = []

for tup in tuples_list:
    total_sum.append(sum(tup))
    print(sum(tup))

print("The sum of the numbers in the given tuple list is:", total_sum)


# to do sum of all values in the given list
# I am comment this below code because not asked the sum of values in the list


# tuples_list = [(1, 2), (3, 4), (5, 6)]
# total_sum = 0
# for tup in tuples_list:
#     total_sum += sum(tup)
# print("The sum of the numbers in the given tuple list is:", total_sum)

