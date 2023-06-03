def third_max(list_val):
    list_val.sort(reverse=True)
    new_list = []
    for i in list_val:
        if i not in new_list:
            new_list.append(i)
    return new_list[2]
print(third_max([1,2,3,4,4]))