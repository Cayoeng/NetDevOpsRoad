import copy

l1 = [4,5,7,1,3,9,0]

l2 = copy.deepcopy(l1)

l2.sort()

for i in range(len(l1)):
    print(l1[i],l2[i])