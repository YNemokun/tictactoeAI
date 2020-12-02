def get_min_key(dict):
    # get first key and value
    min_key = next(iter(dict))
    min_value = dict[min_key]
    for key in dict:
        if dict[key] < min_value:
            min_key = key
            min_value = dict[key]

    return min_key


def get_max_key(dict):
    # get first key and value
    max_key = next(iter(dict))
    max_value = dict[max_key]
    for key in dict:
        if dict[key] > max_value:
            max_key = key
            max_value = dict[key]

    return max_key


# dict = {
#     "key1": "val1",
#     "key2": "val2",
#     "key3": 3,
#     "key4": 3.1415,
#     "key5": True,
# }
#
# print(dict)
#
# for key in dict:
#     print(key, ":", dict[key])
#
# print("")
# for (k, v) in dict.items():
#     print(k, "-", v)
#
# print("\n\nmoves....")
#
# moves = {
#     1: 78,
#     2: 45,
#     3: 45,
#     6: 35,
#     7: -34
# }
#
# for k in moves:
#     print(k, " : ", moves[k])
#
# min = get_min_key(moves)
#
# print("")
# print(min)
#
# print(get_max_key(moves))
