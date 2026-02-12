def invert_unique(d):
    result = {}
    for k, v in d.items():
        if v not in result:
            result[v] = []
        if k not in result[v]:
            result[v].append(k)
    return result
print(invert_unique({"a": 1, "b": 2, "c": 1, "d": 2, "e": 3}))#1