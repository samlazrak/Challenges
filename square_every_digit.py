def square_digits(num):
    numbers = [int(x) for x in str(num)]
    numbers_squared = []
    for x in numbers:
      numbers_squared.append(x*x)
    numbers_concat = ''
    for x in numbers_squared:
      numbers_concat = numbers_concat+str(x)
    return int(numbers_concat)

test.assert_equals(square_digits(9119), 811181)
