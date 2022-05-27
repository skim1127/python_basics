# Print greeting to the user
def hello():
    print("Hello User!")
hello()

# Take three arguments and return it in a list
def pack(item_one, item_two, item_three):
    return([item_one, item_two, item_three])
print(pack("cellphone", "book", "laptop"))

"""
Accept a list of any length, and print a series of 
strings that say "First I eat ___" for first item,
then "Next I eat ___" for the rest of the items.
"""
def eat_lunch(first_arg, *rest_args):
    print(f"First, I eat the {first_arg}")
    for item in rest_args:
        print(f"Next, I eat the {item}")

eat_lunch("Apple", "Pizza", "Brownie", "Cake")