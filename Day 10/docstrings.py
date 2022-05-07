def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "ERROR: You didn't provide your name"
    formated_f = f_name.title()
    formated_l = l_name.title()
    return f"Result: {formated_f} {formated_l}"


format_name()
