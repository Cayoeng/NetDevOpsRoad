port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
print(f'Original list:\n{port_list}')

print('\nSorted list:')
sorted_list = sorted(port_list, key=lambda x: [int(part) for part in x.split()[1].split("/")])

print(sorted_list)