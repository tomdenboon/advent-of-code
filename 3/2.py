def bitArrayToInteger(arr):
    result = 0
    for i in range(len(arr)):
        index = len(arr) - (i+1)
        if arr[index] == '1':
            result += 2**i
    return result


def add_number_co(one_count, number_count, current_bit):
    if one_count < number_count/2 and current_bit:
        return True
    elif one_count >= number_count/2 and not current_bit:
        return True
    return False


def add_number_oxygen(one_count, number_count, current_bit):
    if one_count >= number_count/2 and current_bit:
        return True
    elif one_count < number_count/2 and not current_bit:
        return True
    return False


def rating(numbers, type):
    i = 0
    while len(numbers) > 1 and i < len(numbers[0]):
        new_numbers = []
        bit_at = []
        for number in numbers:
            if number[i] == '1':
                bit_at.append(1)
            else:
                bit_at.append(0)
        one_count = bit_at.count(1)
        for j in range(len(bit_at)):
            if type == 'CO' and add_number_co(one_count, len(numbers), bit_at[j]):
                new_numbers.append(numbers[j])
            elif type != 'CO' and add_number_oxygen(one_count, len(numbers), bit_at[j]):
                new_numbers.append(numbers[j])
        numbers = new_numbers
        i += 1
    return numbers[0]


file = open('input')
numbers = []
for line in file:
    numbers.append(line.strip())

print(bitArrayToInteger(rating(numbers, 'OXYGEN'))
      * bitArrayToInteger(rating(numbers, 'CO')))
