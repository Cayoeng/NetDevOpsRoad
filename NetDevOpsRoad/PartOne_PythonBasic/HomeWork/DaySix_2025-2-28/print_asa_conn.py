def print_asa_connections(asa_dict):
    """
    Print ASA connections in a formatted manner.

    Parameters:
    asa_dict (dict): A dictionary containing parsed ASA connection information.
    """
    print("\nConnection Analysis Results:\n")
    format_str = "{:<24} | {:<24} | {:<8} | {}"
    header = "Source IP:Port".ljust(24) + " | " + "Destination IP:Port".ljust(24) + " | " + "Bytes".ljust(
        8) + " | Flags"
    print(header)
    print("-" * 80)

    for key, value in asa_dict.items():
        src_ip = key[0]
        src_port = key[1]
        dst_ip = key[2]
        dst_port = key[3]

        print(format_str.format(
            f"{src_ip}:{src_port}",
            f"{dst_ip}:{dst_port}",
            value[0],
            value[1]
        ))
