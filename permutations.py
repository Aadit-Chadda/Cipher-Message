# How does a permutation grow

from itertools import permutations
my_list = [1,2,3]

list_of_permutations = permutations(my_list)
count = 0
for permutation in list_of_permutations:
    print(permutation)
    count += 1
print("No. of objects: ", len(my_list))
print("No. of permutations: ", count)
