import re

def validate_password(password):
    pattern = r"""
        ^
        (?=.*[A-Z])
        (?=.*[a-z])
        (?=.*\d)
        (?=.*[@$!%*?&])
        .{8,}
        $
    """

    # Using regex modifiers
    match = re.search(
        pattern,
        password,
        re.IGNORECASE | re.MULTILINE | re.DOTALL | re.VERBOSE
    )

    if match:
        print("Strong Password")
    else:
        print("Weak Password")


# Input
password = input()
validate_password(password)