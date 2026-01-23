def conv_2_deci(x: str):             ###TC=o(len),SC=o(1)###
    deci_num = 0
    power = 0
    index = len(x) - 1
    while index >= 0:
        num = int(x[index]) * (2 ** power)
        deci_num += num
        index -= 1
        power += 1
    return deci_num
print(conv_2_deci("1101"))
