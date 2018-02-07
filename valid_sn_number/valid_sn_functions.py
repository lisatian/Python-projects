def valid_sn(possible_sn):
    """
    ------------------------------------------------------- 
    Determines whether or not the given string, 
        possible_sn, is a valid serial number.
    Use: result = valid_sn(possible_sn)
    ------------------------------------------------------- 
    Preconditions:
        possible_sn - a possible serial number (str)
    Postconditions:
        returns: 
        True if possible_sn is a valid serial number or 
            False otherwise (bool)
    -------------------------------------------------------
    """
    if (len(possible_sn) == 11) and (possible_sn[0:3] == "SN/") and (possible_sn[3:7].isdigit() == True) and (possible_sn[7] == "-") and (possible_sn[8:].isdigit() == True):
        result = True
    else:
        result = False

    return result


def valid_sn_file(sn_file, valid_output, invalid_output):
    """
    ------------------------------------------------------- 
    Given sn_file, which contains serial numbers, this
        function calls the valid_sn function to determine
        whether or not each serial number in file is valid. 
        It then prints all valid serial numbers to valid_output
        and all invalid serial numbers to invalid_output.
    Use: valid_sn_file(sn_file, valid_output, invalid_output)
    ------------------------------------------------------- 
    Preconditions:
        sn_file - file containing list of serial numbers 
            (file handle of an opened file)
        valid_output - empty file for holding valid serial 
            numbers (file handle of an opened file)
        invalid_output - empty file for holding invalid serial 
            numbers (file handle of an opened file)
    Postconditions:
        prints all valid serial numbers to valid_output and 
            prints all invalid serial numbers to invalid_output
    -------------------------------------------------------
    """
    sn_file.seek(0)
    valid_output.seek(0)
    invalid_output.seek(0)

    for line in sn_file:
        result = valid_sn(line.strip())
        if result == True:
            print("{}".format(line.strip()), file=valid_output)
        else:
            print("{}".format(line.strip()), file=invalid_output)

    return
