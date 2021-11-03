import string
from ie import IE

try:
    item_value = input("Input value of item: ")

    if item_value == "":
        raise IE(item_value, "Price can't be blank")

    if any([letter in item_value for letter in string.ascii_lowercase]):
        raise IE(item_value, "Please enter only digits")

    item_value = int(item_value)

    if item_value <= 0:
        raise IE(item_value, "Price is can't be less or equal to zero ")
    print(f"Item value is {item_value}")

except IE as error:
    print(error)
