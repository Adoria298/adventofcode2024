import functools
from pprint import pprint

# get lists from file
lines = []
with open("day1_input.txt", "r") as in_file:
    lines = in_file.readlines()

list1 = []
list2 = []
for line in lines:
    nums = line.split()
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))

list1, list2 = sorted(list1), sorted(list2)

pprint(list1); pprint(list2) # prove to myself the lists are sorted

# challenge 1: calculate distance between the two lists
distances = []

for index, i in enumerate(list1):
    distances.append(max(i, list2[index])-min(i,list2[index]))
    print(distances[index]) # prove to myself there are no negative numbers

print(f"Total distance = {sum(distances)}")

# challenge 2: calculate similarity of the two lists

similarities = []

@functools.cache
def count_instances(element, listx):
    count = 0
    if element not in listx:
        return count
    for i in listx:
        if element == i:
            count += 1
    return count

list2 = tuple(list2) # to allow caching

for i in list1:
    if i not in list2:
        continue 
    similarities.append(i*count_instances(i, list2))

print(f"Similarities: {sum(similarities)}")


