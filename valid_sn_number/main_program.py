# Import:
from valid_sn_functions import valid_sn_file

# Opening files:
sn_file = open("serial_number.txt", "r", encoding="utf-8")
valid_output = open("output_valid.txt", "w", encoding="utf-8")
invalid_output = open("output_invalid.txt", "w", encoding="utf-8")

# Function call:
valid_sn_file(sn_file, valid_output, invalid_output)

# Closing files:
sn_file.close()
valid_output.close()
invalid_output.close()