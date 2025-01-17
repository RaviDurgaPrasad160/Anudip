# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers. 

import random

rand_num_list = []

for _ in range(5):
    rand_num_list.append(random.randint(1, 100))

print(rand_num_list) 

result_1 = max(rand_num_list)
print(f'maximun of 5 random numbers {result_1}')

result_2 = min(rand_num_list)
print(f'minimum of 5 random numbers {result_2}')
