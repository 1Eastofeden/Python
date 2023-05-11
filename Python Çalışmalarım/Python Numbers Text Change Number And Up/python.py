
text = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}

first_number_str = input("Enter the first number: ")
second_number_str = input("Enter the second number: ")

if first_number_str in text and second_number_str in text:
    first_number = text[first_number_str]
    second_number = text[second_number_str]
    result = first_number + second_number
    print("Result: ", result)
else:
    print("Invalid input!")
