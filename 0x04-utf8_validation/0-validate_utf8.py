#!/usr/bin/python3
"""
Checks if data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """Validate data set for UTF encoding"""
    bytes_number = 0

    for byte in data:
        """Extract 8 lsb ie value of 1= 2^0"""
        byte = byte & 0xFF

        if bytes_number == 0:
            if byte >> 7 == 0b0:
                bytes_number = 0
            elif byte >> 5 == 0b110:
                bytes_number = 1
            elif byte >> 4 == 0b1110:
                bytes_number = 2
            elif byte >> 3 == 0b11110:
                bytes_number = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes_number -= 1

    return bytes_number == 0
