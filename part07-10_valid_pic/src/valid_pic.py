from datetime import datetime


def is_it_valid(pic: str) -> bool:
    dob = pic[:6]
    century_marker = pic[6]
    personal_identifier = pic[7:10]
    control_character = pic[10]
    control_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    markers = {"+": "18", "-": "19", "A": "20"}
    # length validation
    if len(pic) != 11:
        return False
    # century marker validation
    if century_marker not in ("+", "-", "A"):
        return False
    # control character validation
    if control_character != control_string[int(dob + personal_identifier) % 31]:
        return False
    # date of birth validation
    try:
        day = int(dob[:2])
        month = int(dob[2:4])
        year = int(markers[century_marker] + dob[4:])
        date = datetime(year, month, day)
    except ValueError:
        return False

    return True
