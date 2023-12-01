# Used to import aux_tools
import sys
sys.path.append('..')
from aux_tools import file2arra

values = file2arra.file2array('./input.txt')

digits_dict = {
    "one" : "o1e",
    "two" : "t2o",
    "three" : "t3e",
    "four" : "f4r",
    "five" : "f5e",
    "six" : "s6x",
    "seven" : "s7n",
    "eight" : "e8t",
    "nine" : "n9e"
}

total_sum = 0
for calibration in values:
    for string_number, int_number in digits_dict.items():
        calibration = calibration.replace(string_number, int_number)
    numbers = []
    for param in calibration:
        try:
            int(param)
            numbers.append(param)
        except:
            continue
    final_val = int(numbers[0])*10 + int(numbers[-1])
    total_sum += final_val
print(total_sum)