def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list to prevent ZeroDivisionError
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Example of improved error handling
try:
    result = 10/0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
    print("Returning 0")
    result = 0
print(f"Result is: {result}") 