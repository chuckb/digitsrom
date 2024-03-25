# Ben Eater's breadboard 8-bit computer hex display ROM binary file generator.
# If you have a ROM programmer, this will produce a file you can load into
# your programmer without having to program the Arduino. A 2K file is written for
# the 28C16 ROM chip provided in the kit.

# Assuming you have an array of hex bytes as strings to display each base 10 numerical digit
hex_bytes_array = ['7e', '30', '6d', '79', '33', '5b', '5f', '70', '7f', '7b']

# File path to write the binary data
file_path = 'rom.bin'

def write_unsigned(file):
  for i in range(256):
    # Write the ones digits to the file
    file.write(bytes.fromhex(hex_bytes_array[i % 10]))
  for i in range(256):
    # Write the tens digits to the file
    file.write(bytes.fromhex(hex_bytes_array[int(i / 10) % 10]))
  for i in range(256):
    # Write the hundreds digits to the file
    file.write(bytes.fromhex(hex_bytes_array[int(i / 100) % 10]))
  for i in range(256):
    # Write the thousands digit to the file (blank in this case)
    file.write(bytes.fromhex('00'))

def write_signed(file):
  # Write signed integers in order of their unsigned binary representations
  for i in range(128):
    # Write the ones digits to the file for positive integers
    file.write(bytes.fromhex(hex_bytes_array[i % 10]))
  for i in range(-128, 0):
    # Write the ones digits to the file for positive integers
    file.write(bytes.fromhex(hex_bytes_array[abs(i) % 10]))
  for i in range(128):
    # Write the tens digits to the file for positive integers
    file.write(bytes.fromhex(hex_bytes_array[int(i / 10) % 10]))
  for i in range(-128, 0):
    # Write the tens digits to the file for positive integers
    file.write(bytes.fromhex(hex_bytes_array[abs(int(i / 10)) % 10]))
  for i in range(128):
    # Write the hundreds digits to the file for positive integers
    file.write(bytes.fromhex(hex_bytes_array[int(i / 100) % 10]))
  for i in range(-128, 0):
    # Write the hundreds digits to the file for positive integers
    file.write(bytes.fromhex(hex_bytes_array[abs(int(i / 100)) % 10]))
  for i in range(128):
    # Write the sign for positive integers (blank)
    file.write(bytes.fromhex('00'))
  for i in range(-128, 0):
    # Write the sign for negative integers
    file.write(bytes.fromhex('01')) # This should be segment g on the 7-segment display

# Open the file in binary write mode
with open(file_path, 'wb') as file:
  write_unsigned(file)
  write_signed(file)

print("Binary data has been written to the file:", file_path)
