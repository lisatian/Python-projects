This project scans a file of serial numbers and separates the valid and invalid serial numbers into two new files.

Valid serial numbers are of the format: "SN/nnnn-nnn", where n represents a digit.

The main_program.py handles the original file opening and closing, while valid_sn_functions.py performs the logic used to check serial numbers against the valid format and to separate them into two new files.

A sample file, serial_number.txt is provided as an example to show that, when run through the functions, the serial numbers in that file get segregated into new files: output_valid.txt and output_invalid.txt. 
