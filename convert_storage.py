def convert_storage(value, from_unit, to_unit):
    units = {
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3,
        'TB': 1024 ** 4
    }

    if from_unit not in units or to_unit not in units:
        return "Đơn vị không hợp lệ. Vui lòng chọn từ KB, MB, GB, or TB. (Chữ Hoa)"

    result = value * units[from_unit] / units[to_unit]
    return result

def print_table(value, from_unit, converted_values):
    print(f"Chuyển đổi {value} {from_unit} to:")
    print("{:<10}{}".format("Đơn vị", "Giá trị Chuyển đổi "))
    print("-" * 25)
    for unit, converted_value in converted_values.items():
        print("{:<10}{:.2f}".format(unit, converted_value))

# Example usage:
value = float(input("Nhập vào giá trị: "))
from_unit = input("Nhập vào giá trị nguồn (KB, MB, GB, TB): ")

units = ['KB', 'MB', 'GB', 'TB']
converted_values = {}
for unit in units:
    if unit != from_unit:
        converted_value = convert_storage(value, from_unit, unit)
        converted_values[unit] = converted_value

print_table(value, from_unit, converted_values)
