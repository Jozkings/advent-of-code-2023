from typing import Dict

FILE_NAME = 'input1.in'

str_numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
MAX_LENGTH = max([len(key) for key in str_numbers.keys()])

res1 = 0   #first part
res2 = 0   #second part


def word_number(word: str, dicto: Dict[str, str]) -> str:
    for i in range(MAX_LENGTH+1):
        digit = word[len(word)-i:]
        if digit in dicto:
            return dicto[digit]
    return ''


with open(FILE_NAME, 'r') as file:
    for line in file:
        value = line.strip()
        all_digits = ''
        number_digits = ''
        letters = ''
        for val in value:
            if '1' <= val <= '9':
                number_digits += val
                all_digits += val
            else:
                letters += val
                digit = word_number(letters, str_numbers)
                if digit:
                    all_digits += digit
        res1 += int(number_digits[0] + number_digits[-1])
        res2 += int(all_digits[0] + all_digits[-1])


print(res1)
print(res2)
