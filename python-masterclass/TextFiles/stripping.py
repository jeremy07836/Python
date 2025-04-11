def remove_prefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]    # Return a copy


def remove_suffix(string: str, suffix: str) -> str:
    # if suffix='' should not call string[:-0]
    if suffix and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]    # Return a copy


filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

# chars = "'"
# chars = "'Twas"
# chars = "'Twasebv"
chars = "' Twasebv"
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

for character in first:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

for character in first[::-1]:   # process backwards
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

# twas_removed = first.removeprefix("'Twas")
twas_removed = remove_prefix(first, "'Twas")
print(twas_removed)
# toves_removed = first.removesuffix("toves")
toves_removed = remove_suffix(first,"toves")
print(toves_removed)
