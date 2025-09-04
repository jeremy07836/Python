a_string = "this is\na string split\t\tand tabbed"
print(a_string)
print(repr(a_string)[1:-1])

raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)
print(repr(b_string)[1:-1])

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

# double up on backslash if a string ends with one
# error_string = r"this string ends with \"
error_string = r"this string ends with \\"
print(error_string)
