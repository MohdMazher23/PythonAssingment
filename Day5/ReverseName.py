input_data=input("ENTER YOUR NAME: ")
def my_reverse(name):
    reverse_name=name[-1::-1]
    print("Before Reverse Operation \n",input_data)
    print("After Reverse Operation \n",reverse_name)

my_reverse(input_data)

#OUTPUT
"""
ENTER YOUR NAME: MOHD MAZHER UDDIN
Before Reverse Operation
 MOHD MAZHER UDDIN
After Reverse Operation
 NIDDU REHZAM DHOM
"""