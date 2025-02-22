from kamene.all import ICMP, IP, sr1


def ping_once(target_ip):
    """
    Send one ICMP request to the target IP and display ICMP packet header details.

    Args:
        target_ip (str): IP address to send the ICMP request to.
    """
    print(f"Sending a single ICMP request to {target_ip}...")

    try:
        # Create an ICMP packet
        packet = IP(dst=target_ip) / ICMP()

        # Display ICMP packet header details for the request
        print("\nICMP Request Header:")
        print(packet.display())

        # Send the packet and wait for the response
        response = sr1(packet, timeout=1, verbose=0)

        if response is not None:
            print("\nResponse received!")
            # Display ICMP packet header details for the response
            print("\nICMP Response Header:")
            print(response.display())
        else:
            print(f"No response from {target_ip}.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    target_ip = input("Please input the target you want to send an ICMP request to: ")
    ping_once(target_ip)