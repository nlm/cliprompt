import re

def yes_no(value):
    if re.match(r'^[Yy]([Ee][Ss])?$', value):
        return True
    elif re.match(r'^[Nn]([Oo])?$', value):
        return False
    else:
        raise ValueError
