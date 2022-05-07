# Functions with Outputs

#   def my_function():
#   result = 3 * 2 OR return 3 * 2
#   return result
#   output = my_function()

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "ERROR: You didn't provide your name"
    formated_f = f_name.title()
    formated_l = l_name.title()
    return f"Result: {formated_f} {formated_l}"


# formatted = format_name("jedae", "LISBON")
# print(formatted)

print(format_name(input("What's your first name?"), input("What's your last name?")))
