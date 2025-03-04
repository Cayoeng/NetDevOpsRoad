list1 = ['aaa', 111, (4,5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4,5)]

print('\n方案一'+'-'*32)
for item in list1:
    if item in list2:
        print(f"{item} in list1 and list2")
    else:
        print(f"{item} only in list1")

print('\n方案二'+'-'*32)
def compare_list(list1, list2):
    for item in list1:
        if item in list2:
            print(f"{item} in list1 and list2")
        else:
            print(f"{item} only in list1")

compare_list(list1, list2)