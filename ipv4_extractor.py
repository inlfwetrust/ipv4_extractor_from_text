import re

REGEX_V = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')  # regex for extracting values from the text x.x.x.x

text = "Hello 192.168.1.1 World, with 1.1.1.1 exmples, from 300.1.1.1 not IPs, to -8.8.8.8 Google.Google, 1.1.1.-400"  # example text

def is_octet_valid(list_with_octets) -> bool:
    """
    Take a list with octets and check for a valid IP range
    return True or False
    """
    for octet in list_with_octets.split('.'):
        if int(octet) > 256:
            return False
    return True    


def get_valid_ips(from_text) -> list:
    """
    Take a str(text) as input, and return a [list] with valid IPv4 IPS
    """
    return [x for x in re.findall(pattern=REGEX_V, string=from_text) if is_octet_valid(x)]  # check if it is a valid IPv4 range


def main():
    print(get_valid_ips(text))


if __name__ == '__main__':
    main()