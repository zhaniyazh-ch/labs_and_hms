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