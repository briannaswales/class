def is_consecutive(a_list):
    # sorts list
    sorted_list = sorted(a_list)
    #loops +1
    range_list = list(range(min(a_list), max(a_list) + 1))
    #
    if sorted_list == range_list:
        print("True")
    else:
        print("False")


list2 = 11, 12, 13, 14
is_consecutive(list2)
