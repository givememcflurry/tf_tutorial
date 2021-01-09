import random as rd


# True-False Percentage
def tfp(input_list):
    whole = len(input_list)
    true_pick = input_list.count(1)
    percent = true_pick / whole
    return percent


# Make Random List
def mrl(input_count, input_whole):
    output_list = []
    i = j = 0

    while i < input_count:
        output_list.append(1)
        i = i + 1

    while j < (input_whole - input_count):
        output_list.append(0)
        j = j + 1

    rd.shuffle(output_list)
    return output_list
