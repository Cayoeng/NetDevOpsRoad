import re

def parse_asa_connections(asa_conn):
    """
    Parse ASA connections and extract relevant information.

    Parameters:
    asa_conn (str): A string containing ASA connection information.

    Returns:
    dict: A dictionary where each key is a tuple of source IP, source port, destination IP, and destination port,
          and the corresponding value is another tuple containing the number of bytes and flags.
    """
    asa_dict = {}
    for conn in asa_conn.split('\n '):
        re_result = re.match(
            r'TCP \S+ (\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5}) \S+ (\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5}), idle \d+:\d+:\d+, bytes (\d+), flags (\S+)',
            conn)
        if re_result:
            asa_dict[(re_result.group(1), re_result.group(2), re_result.group(3), re_result.group(4))] = (
            re_result.group(5), re_result.group(6))
    return asa_dict
