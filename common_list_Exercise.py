# common_list:
def common_list(l1,l2):
    common = []
    for i in l1:
        if i in l2:
            common.append(i)
    return common

print(common_list([1, 2, 3, 4, 5, 6, 7] , [1, 3, 5, 7]))