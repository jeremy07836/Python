data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]

# print(ord("a"))
# print(ord("b"))
# print(ord("z"))


def simple_hash(s: str) -> int:
    """A ridiculously simple hashing function"""
    bash_hash = ord(s[0])
    return bash_hash % 10


def get(k: str) -> str:
    """Return the value for a key, or None if the key does not exist"""
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    # h = hash(key)         # python hash function
    print(key, h)
    keys[h] = key
    values[h] = value

print(keys)
print(values)
print()
value = get("lemon")
# value = get("banana")     # same as lemon
print(value)
