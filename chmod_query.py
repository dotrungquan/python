def chmod_to_octal(chmod):
    permissions = {'r': 4, 'w': 2, 'x': 1}
    octal = 0
    for i in range(0, len(chmod), 3):
        chunk = chmod[i:i+3]
        value = 0
        for char in chunk:
            if char in permissions:
                value += permissions[char]
        octal = octal * 10 + value
    return str(octal)

def octal_to_chmod(octal):
    permissions = {0: '---', 1: '--x', 2: '-w-', 3: '-wx', 4: 'r--', 5: 'r-x', 6: 'rw-', 7: 'rwx'}
    chmod = ''
    octal = str(octal)
    for digit in octal:
        chmod += permissions[int(digit)]
    return chmod

def convert_chmod(chmod):
    if chmod.isdigit():
        octal = int(chmod)
        return octal_to_chmod(octal)
    else:
        return chmod_to_octal(chmod)

# Example usage:
input_chmod = input("Enter a Chmod or octal: ")
converted_chmod = convert_chmod(input_chmod)
print("Converted Chmod: ", converted_chmod)
