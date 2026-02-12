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
symmetric_even = lambda a, b: {x for x in a ^ b if x % 2 == 0}
print(symmetric_even({1, 2, 4, 6}, {2, 3, 6, 8}))#7
def sort_dict_by_value_length(d):
    items = list(d.items())
    items.sort(key=lambda kv: (len(kv[1]), kv[0]))
    return items
print(sort_dict_by_value_length({"a": "apple", "b": "kiwi", "c": "banana"}))#8
def common_elements_all(sets_list):
    if not sets_list:
        return set()
    common = sets_list[0].copy()
    for s in sets_list[1:]:
        common &= s
    return common
print(common_elements_all([{1, 2, 3}, {2, 3, 4}, {3, 2, 5}]))#9
filter_dict = lambda d: {k: sorted([x for x in v if x % 2 == 1])
                         for k, v in d.items() if any(x % 2 == 1 for x in v)}
print(filter_dict({"a": [1, 2, 3], "b": [4, 6], "c": [7, 9]}))#10
def group_by_length(words):
    result = {}
    for w in words:
        l = len(w)
        if l not in result:
            result[l] = []
        if w not in result[l]:
            result[l].append(w)
    return result
print(group_by_length(["apple", "pear", "banana", "pear", "kiwi"]))#11
filter_strings = lambda s: {w for w in s if w.isalpha() and len(w) > 4 and len(set(w.lower())) == len(w)}
print(filter_strings({"hello", "world", "apple", "unique", "abcde"}))#12
def invert_dict_strict(d):
    counts = {}
    for v in d.values():
        counts[v] = counts.get(v, 0) + 1
    result = {}
    for k, v in d.items():
        if counts[v] == 1:
            result[v] = k
    return result
print(invert_dict_strict({"a": 1, "b": 2, "c": 1, "d": 3}))#13
def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    sorted_nums = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    top_k = [num for num, _ in sorted_nums[:k]]
    return set(top_k)
print(top_k_frequent([1, 2, 2, 3, 3, 3, 4], 2))#14
filter_dict = lambda d: {k: v for k, v in d.items() if v >= sum(d.values())/len(d) and v % 2 == 1}
print(filter_dict({"a": 1, "b": 2, "c": 5, "d": 7}))#15
def update_counts(d, items):
    for item in items:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d
print(update_counts({"apple": 2, "banana": 1}, ["apple", "orange", "banana", "apple"]))#16
set_op = lambda a, b, c: (a & b) - c
print(set_op({1, 2, 3}, {2, 3, 4}, {3}))#17
def sort_dict_by_value_sum(d):
    items = []
    for k, v in d.items():
        items.append((k, sum(v)))
    items.sort(key=lambda x: (-x[1], x[0]))
    return items
print(sort_dict_by_value_sum({"a": [1, 2], "b": [3, 4], "c": [5]}))#18
def filter_by_digit_sum(nums):
    result = set()
    for num in nums:
        if num % 2 == 1:
            digit_sum = sum(int(d) for d in str(abs(num)))
            if digit_sum % 2 == 0:
                result.add(num)
    return result
print(filter_by_digit_sum({11, 23, 35, 40, 7}))#19