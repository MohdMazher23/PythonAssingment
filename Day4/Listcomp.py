
list_even=[i for i in range(1,21) if i%2==0]
print("Even Numbers")
print(list_even)

list_odd=[i for i in range(1,21) if i%2!=0]
print("Odd Numbers")
print(list_odd)

list_sqr=[i*i for i in range(1,21)]
print("Square OF")
print(list_sqr)

list_cube=[i*i*i for i in range(1,21)]
print("Cube Of")
print(list_cube)

#OUTPUT
"""
Even Numbers
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Odd Numbers
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Square OF
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
Cube Of
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000]
"""