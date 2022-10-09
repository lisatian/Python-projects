This program scans a file containing serial numbers, and separates the valid and invalid serial numbers into two new files.

The valid serial number format is: "SN/_nnnn-nnn_", where _n_ represents a digit.

**main_program.py** handles file opening and closing, while **valid_sn_functions.py** performs the logic used to check serial numbers against the valid format and separates numbers into two new files.

A sample file, **serial_number.txt**, is provided as an input example. The serial numbers in that file get segregated by the program into **output_valid.txt** and **output_invalid.txt**. 
