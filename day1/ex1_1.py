# Used to import aux_tools
import sys
sys.path.append('..')
from aux_tools import file2arra

values = file2arra.file2array('./input.txt')

total_sum = 0

for calibration in values:
    numbers = []
    for param in calibration:
        try:
            int(param)
            numbers.append(param)
        except:
            continue

    total_sum += int(numbers[0])*10 + int(numbers[-1])

print(total_sum)