import sys

N = int(input())
available_numbers = [3, 5, 7]


def search_shichigosan_numbers(limit: int, shichigosan_numbers: dict, current_digit: int) -> list:
    limit_digit = len(str(limit))

    if current_digit == MIN_DIGIT:
        numbers = []
        for a in available_numbers:
            for b in available_numbers:
                for c in available_numbers:
                    if a != b and b != c and c != a:
                        number = int(f"{a}{b}{c}")
                        if number <= limit:
                            numbers.append(str(number))
        shichigosan_numbers[current_digit] = set(numbers)

        if limit_digit == 3:
            return shichigosan_numbers
        else:
            return search_shichigosan_numbers(limit, shichigosan_numbers, current_digit + 1)
    else:
        numbers = []
        for shichigosan_number in shichigosan_numbers[current_digit - 1]:
            for new_digit_number in available_numbers:
                for insert_place in range(len(shichigosan_number) + 1):
                    new_number = list(shichigosan_number)
                    new_number.insert(insert_place, str(new_digit_number))
                    new_number = int(''.join(new_number))
                    if new_number <= limit:
                        numbers.append(str(new_number))
        shichigosan_numbers[current_digit] = set(numbers)
        if limit_digit == current_digit:
            return shichigosan_numbers
        else:
            return search_shichigosan_numbers(limit, shichigosan_numbers, current_digit + 1)


MIN_DIGIT = 3

if len(str(N)) < 3:
    print(0)
    sys.exit()

numbers = search_shichigosan_numbers(N, {}, MIN_DIGIT)
count = 0
for n in range(MIN_DIGIT, len(str(N)) + 1):
    count += len(numbers[n])
print(count)
