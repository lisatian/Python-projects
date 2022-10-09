This program calculates a manufacturing company's total output in any given hour, given assumptions of the manufacturer's worker productivity throughout the day.

The user is prompted to input an hour of the day (24-hr format) and the number of workers present at that hour. The program will display the total number of pieces that the company can produce within the hour.

Given assumptions:
- between hours of 6am and 10pm -- produce 30 pieces/hour/worker
- between hours of 10am and 2pm -- produce 40 pieces/hour/worker
- between hours of 2pm and 6pm -- produce 35 pieces/hour/worker

main_program.py handles the user input and calls productivity_function.py to calculate the total number of pieces produced in any given hour.

A sample file, testing.txt, is provided to show the automation in use when given example user inputs.
