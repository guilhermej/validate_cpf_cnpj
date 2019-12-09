import re
import logging


def validate_cnpj(cnpj):
    try:
        cnpj = str(cnpj)
    except:
        logging.exception("CNPJ must be a string")
        return False

    cnpj = re.sub('[^0-9]', '', cnpj)
    if not cnpj or len(cnpj) != 14:
        return False

    # Take the first 12 numbers to generate the last 2 verification digits
    calculated_cnpj = cnpj[:12]

    # Calculate first validation digit
    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_1 = 0
    for i, number in enumerate(prod):
        result = number * int(calculated_cnpj[i])
        sum_1 += result

    rest1 = sum_1 % 11
    if rest1 < 2:
        first_digit = 0
    else:
        first_digit = 11 - rest1

    calculated_cnpj += str(first_digit)

    # Calculate second validation digit
    prod_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_2 = 0
    for i, number in enumerate(prod_2):
        result = number * int(calculated_cnpj[i])
        sum_2 += result

    rest2 = sum_2 % 11
    if rest2 < 2:
        second_digit = 0
    else:
        second_digit = 11 - rest2

    calculated_cnpj += str(second_digit)

    # Returns clean CNPJ string if is valid
    if calculated_cnpj == cnpj:
        return calculated_cnpj

    return False
