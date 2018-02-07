# Import
from productivity_function import pieces_produced

# Input
hour = int(input("Enter an hour of the day, in 24-hour format: "))
workers = int(input("Enter the number of workers: "))

# Function call
total_pieces = pieces_produced(hour, workers)

# Output
print("The total number of pieces produced is: {}".format(total_pieces))