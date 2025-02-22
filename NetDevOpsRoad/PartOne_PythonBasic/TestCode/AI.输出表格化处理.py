def print_table(data):
    # Split into lines and remove empty lines
    lines = [line.strip() for line in data.strip().split('\n') if line.strip()]

    # Find column positions by looking at the header line
    positions = []
    current_pos = 0
    header_line = lines[0]

    # Find positions where columns start
    while current_pos < len(header_line):
        while current_pos < len(header_line) and header_line[current_pos] == ' ':
            current_pos += 1
        if current_pos < len(header_line):
            positions.append(current_pos)
            while current_pos < len(header_line) and header_line[current_pos] != ' ':
                current_pos += 1

    # Extract headers and rows using positions
    def split_line(line):
        result = []
        for i in range(len(positions)):
            start = positions[i]
            end = positions[i + 1] if i + 1 < len(positions) else None
            field = line[start:end].strip() if end else line[start:].strip()
            result.append(field)
        return result

    headers = split_line(lines[0])
    rows = [split_line(line) for line in lines[1:]]

    # Calculate column widths
    widths = []
    for i in range(len(headers)):
        column = [row[i] for row in rows]
        width = max(len(headers[i]), max(len(x) for x in column))
        widths.append(width)

    # Print table
    header = ' | '.join(f'{h:<{w}}' for h, w in zip(headers, widths))
    print(header)
    print('-' * len(header))

    # Print data rows
    for row in rows:
        print(' | '.join(f'{c:<{w}}' for c, w in zip(row, widths)))


# Example data
data = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.1.2.1                -   000c.2908.3b71  ARPA   GigabitEthernet2
Internet  192.168.109.101         -   000c.2908.3b67  ARPA   GigabitEthernet1
Internet  192.168.109.102        71   000c.2991.b75b  ARPA   GigabitEthernet1
Internet  192.168.109.129         0   000c.2900.9051  ARPA   GigabitEthernet1
"""

# Print table
print_table(data)