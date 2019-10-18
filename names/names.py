import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# 7.1s 64 duplicates /  O(n^2)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# duplicates = []
# hashed_names = {}

# returning 32
# for name in names_1 and names_2:
#     if hashed_names.get(name):
#         duplicates.append(name)
#     else:
#         hashed_names[name] = True


# return 64
# for name in names_1:
#     hashed_names[name] = True
# for name in names_2:
#     if name in hashed_names:
#         duplicates.append(name)
duplicates = []
bst = BinarySearchTree(names_1[0])

for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
