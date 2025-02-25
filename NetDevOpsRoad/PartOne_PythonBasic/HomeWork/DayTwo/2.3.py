str1 = 'Python'

print(str1)
print('-'*(len(str1)+1))
str2 = 'Python' + '-'

print(str2)
print('-'*(len(str1)+1))

str2_strip = str2[1:]
print(str2_strip)
print('-'*(len(str1)+1))

str3 = str2_strip + str1[0]
print(str3)
print('-'*(len(str1)+1))

str4 = str3 + 'y'
print(str4)