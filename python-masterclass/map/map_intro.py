# from typing import Any, Callable, cast
import timeit
from statistics import mean, stdev

text = "what have the romans ever done for us"

def upper_comp() -> list[str]:
    capitals = [char.upper() for char in text]
    return capitals


def upper_map() -> list[str]:
    # use map
    # map_capitals = list(map(str.upper, text))     # This give a warning message
    map_capitals = list(map(lambda s: s.upper(), text))     # lambda is a one-liner def
    return map_capitals


def split_comp() -> list[str]:
    words = [word.upper() for word in text.split(' ')]
    return words


def split_map() -> list[str]:
    # use map
    # type: ignore just suppresses the warning
    map_words = list(map(str.upper, text.split(' ')))   # type: ignore[arg-type]
    return map_words


# cast is another way to remove the warning, although it requires importing typing
# for x in map(cast(Callable[[Any], str], str.upper), text.split(' ')):
#     print(x)

if __name__ == "__main__":
    print(upper_comp())
    print(upper_map())
    print(split_comp())
    print(split_map())
    print("Timeit Repeat Function:")
    list1 = timeit.repeat("upper_comp()", setup="from __main__ import upper_comp", number=10000)
    list2 = timeit.repeat("upper_map()", setup="from __main__ import upper_map", number=10000)
    list3 = timeit.repeat("split_comp()", setup="from __main__ import split_comp", number=10000)
    list4 = timeit.repeat("split_map", setup="from __main__ import split_map", number=10000)
    print(mean(list1), stdev(list1))
    print(mean(list2), stdev(list2))
    print(mean(list3), stdev(list3))
    print(mean(list4), stdev(list4))
