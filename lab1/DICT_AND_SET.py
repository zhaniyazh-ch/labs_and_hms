def invert_unique(d):
    result = {}
    for k, v in d.items():
        if v not in result:
            result[v] = []
        if k not in result[v]:
            result[v].append(k)
    return result
print(invert_unique({"a": 1, "b": 2, "c": 1, "d": 2, "e": 3}))#1
filter_set = lambda s: {x for x in s
                        if x > sum(s)/len(s) and
                        x % 2 == 1 and
                        x % 5 != 0}
print(filter_set({1, 3, 5, 7, 9, 11, 15}))#2
def merge_dicts_sum(d1, d2):
    result = {}
    for k in d1:
        result[k] = d1[k]
    for k in d2:
        if k in result:
            result[k] += d2[k]
        else:
            result[k] = d2[k]
    return result
print(merge_dicts_sum({"a": 1, "b": 2}, {"b": 3, "c": 4}))#3
def filter_sets(sets_list):
    result = []
    for s in sets_list:
        if len(s) > 3 and all(x >= 0 for x in s) and any(x % 2 == 0 for x in s):
            result.append(s)
    return result
print(filter_sets([{1, 2, 3, 4}, {5, -1, 6}, {7, 9, 11}, {8, 10, 12, 14}]))#4
top5_keys = lambda d: sorted(d.keys(), key=lambda k: (-d[k], k))[:5]
print(top5_keys({"apple": 5, "banana": 3, "pear": 5, "kiwi": 2, "melon": 4, "fig": 1}))#5
def deep_sum(d):
    total = 0
    for v in d.values():
        if isinstance(v, int) or isinstance(v, float):
            total += v
        elif isinstance(v, list):
            for x in v:
                total += x
        elif isinstance(v, dict):
            total += deep_sum(v)
    return total
print(deep_sum({"a": 5, "b": [1, 2], "c": {"d": 3, "e": [4, 5]}}))#6