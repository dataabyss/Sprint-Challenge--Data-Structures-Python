import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# def repeats(x, y):
#     for name1, name2 in x, y:
#         if name1 != name2:
#             return
#         else:
#             duplicates.append(x)
#             repeats(x,y)

# def repeats(x, y):
#     for x in x, y: # if
#         if x != y:
#             return
#         else:
#             duplicates.append(x)
#             repeats(x,y)

# def repeats(x, y):
#     for item1 in x:
#         for item2 in y:
#             if item1 == item2:
#                 duplicates.append(item1)
#             else:
#                 repeats(x, y)

# def repeats(a, b):
#     a_set = set(names_1)
#     b_set = set(names_2)

#     if (a_set & b_set):
#         duplicates.append(a_set)
#     else:
#         repeats(a,b)

def repeats(x, y):
    dup_values = [duplicates.append(elem) for elem in x if elem in y]
    return dup_values

repeats(names_1, names_2)

end_time = time.time()
print (f"\n{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds\n")
print(f'The runtime for the starter code was O(n)\n')

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
