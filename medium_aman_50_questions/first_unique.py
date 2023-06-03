from operator import le


def first_unique(value):
    count_dict = {}
    for i in value:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    for j in count_dict:
        if count_dict[j] == 1:
            return j


value = 'amankharwal'
print(first_unique(value))
