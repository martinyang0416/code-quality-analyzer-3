def validIPAddress(IP):
    # Check for IPv4
    if '.' in IP:
        parts = IP.split('.')
        if len(parts) != 4:
            return "Neither"
        for part in parts:
            # Check if part is a valid numeric string and has no leading zeros
            if not part.isdigit() or (len(part) > 1 and part[0] == '0') or len(part) == 0:
                return "Neither"
            num = int(part)
            if num < 0 or num > 255:
                return "Neither"
        return "IPv4"
