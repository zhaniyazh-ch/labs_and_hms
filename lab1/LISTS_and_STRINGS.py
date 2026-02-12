#LISTS and STRINGS
def analyze_text(text):
    vowels = set("aeiouаеёиоуыэюя")
    clean_text = ""
    for ch in text.lower():
        if ch.isalpha():
            clean_text += ch
        else:
            clean_text += " "
            unique_vowels = set()
    for ch in clean_text:
        if ch in vowels:
            unique_vowels.add(ch)
    words = clean_text.split()
    result_words = []
    seen = set()
    for w in words:
        if len(w) >= 5 and w[0] == w[-1] and w not in seen:
            seen: result_words.append(w)
            seen.add(w)
    return [len(unique_vowels), " ".join(result_words)]
text = "Aiym said that:we was going to the cinema!"
print(analyze_text(text))#1
process_string = lambda s: " ".join(
    filter(
        lambda w: len(w) % 2 == 0,
        map(
            lambda w: w[::-1],
            filter(
                lambda w: not any(ch.isdigit() for ch in w),
                s.split()
            )
        )
    )
)
text = "hello world546 python code73 data"
result = process_string(text)
print(result)#2
import string
def top_k_words(text, k):
    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, "")
    words = text.split()
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return [w for w, c in sorted_words[:k]]
text = "Salem alem, kun zhainap tyr bugin"
print(top_k_words(text, 3))#3
p_words = lambda s: " ".join(
    map(
        lambda w: w.lower(),
        filter(
            lambda w: sum(ch.isupper() for ch in w) == 1 and
                      not w[0].isupper() and
                      not w[-1].isupper(),
            s.split()
        )
    )
)
text = "heLlo World TesTing teSt"
print(p_words(text))#4
def compress_text(text):
    if not text:
        return ""
    result = []
    i = 0
    while i < len(text):
        count = 1
        char = text[i]
        while i + count < len(text) and text[i + count].lower() == char.lower():
            count += 1
        if count == 1:
            result.append(char)
        else:
            result.append(char + str(count))
        i += count
    return "".join(result)
print(compress_text("aaBBcDDD"))
print(compress_text("HelloooOO"))#5
filter_words = lambda s: list(
    filter(
        lambda w: len(w) >= 4 and
                  all(ch.isalpha() for ch in w) and
                  len(set(w.lower())) == len(w),
        s.split()
    )
)
text = "Bilmim ne zhazuga boladu 576"
print(filter_words(text))#6
import string
def palindrome_words(text):
    for p in string.punctuation:
        text = text.replace(p, "")
    words = text.lower().split()
    palindromes = []
    for w in words:
        if len(w) >= 3 and w == w[::-1]:
            if w not in palindromes:
                palindromes.append(w)
    palindromes.sort(key=lambda x: (-len(x), x))
    return palindromes
text = "Anna went to kayak race, level was high, wow!"
print(palindrome_words(text))#7
process_text = lambda s: " ".join(
    map(
        lambda w: (
            "VOWEL" if w[0].lower() in "aeiou" and not any(ch.isdigit() for ch in w)
            else "CONSONANT" if w[0].isalpha() and not any(ch.isdigit() for ch in w)
            else w
        ),
        s.split()
    )
)
text = "nege zhazu kerek"
print(process_text(text))#8
def alternate_case_blocks(text, n):
    result = []
    i = 0
    block_num = 0
    while i < len(text):
        block = text[i:i+n]
        if block_num % 2 == 0:
            result.append(block.upper())
        else:
            result.append(block.lower())
        i += n
        block_num += 1
    return "".join(result)
print(alternate_case_blocks("abcdefghijklmno", 3))#9
count_words = lambda s: sum(
    1 for w in s.split()
    if any(ch.isdigit() for ch in w) and
       not w[0].isdigit() and
       len(w) >= 5
)
text = "abc12 word5 test1234 9start hello123"
print(count_words(text))#10
def common_unique_chars(s1, s2):
    result = []
    seen = set()
    for ch in s1:
        if ch == " " or ch.isdigit():
            continue
        if ch in s2 and ch not in seen:
            result.append(ch)
            seen.add(ch)
    return "".join(result)
print(common_unique_chars("Hello World123", "Hold Well"))#11
process_words = lambda s: list(
    filter(
        lambda w: len(w) > 3 and
                  w[0].lower() == w[-1].lower() and
                  w.lower() != w[::-1].lower(),
        s.split()
    )
)
text = "anna abca test level noon abba"
print(process_words(text))#12
def replace_every_nth(text, n, char):
    result = []
    count = 0
    word = ""
    for ch in text:
        if ch == " ":
            result.append(word)
            result.append(" ")
            word = ""
            count = 0
        else:
            word += ch
            count += 1
            if count % n == 0 and len(word) >= 3 and not ch.isdigit():
                word = word[:-1] + char
    result.append(word)
    return "".join(result)
print(replace_every_nth("hello world 12a", 2, "*"))#13
filter_words = lambda s: ",".join(
    filter(
        lambda w: len(set([ch.lower() for ch in w if ch.isalpha()])) > 3 and
                  all(w.lower().count(v) <= 1 for v in "aeiou"),
        s.split()
    )
)
text = "hello abcd unique queue test"
print(filter_words(text))#14
def word_pattern_sort(text):
    words = text.split()
    groups = {}
    for w in words:
        l = len(w)
        if l not in groups:
            groups[l] = []
        groups[l].append(w)
    result = []
    for length in sorted(groups.keys()):
        group = groups[length]
        group.sort(key=lambda w: (-sum(ch.lower() in "aeiou" for ch in w), w))
        result.extend(group)
    return result
text = "apple banana cat dog elephant igloo"
print(word_pattern_sort(text))#15
def transform_list(nums):
    result = []
    for num in nums:
        if num < 0:
            continue
        elif num % 2 == 0:
            result.append(num ** 2)
        elif num % 2 == 1 and num > 10:
            result.append(sum(int(d) for d in str(num)))
        else:
            result.append(num)
    return result
print(transform_list([-5, 2, 3, 11, 14, 7]))#16
filter_nums = lambda lst: list(
    map(
        lambda x: x**2,
        filter(
            lambda x: ((x % 3 == 0 or x % 5 == 0) and
                       x % 15 != 0 and
                       len(str(abs(x))) % 2 == 1),
            lst
        )
    )
)
print(filter_nums([3, 5, 15, 123, 50, 7, 555]))#17
def flatten_and_filter(lst):
    result = []
    def flatten(sublist):
        for item in sublist:
            if isinstance(item, list):
                flatten(item)
            elif isinstance(item, int):
                if item > 0 and item % 4 != 0 and len(str(item)) > 1:
                   result.append(item)
    flatten(lst)
    return sorted(result)
print(flatten_and_filter([1, [12, -5, [8, 33, [44, 55]]], 7]))#18
common_even = lambda a, b: [x for x, y in zip(a, b) if x == y and x % 2 == 0]
print(common_even([2, 4, 6, 7], [2, 5, 6, 7]))#19
def max_subarray_sum(nums, k):
    max_sum = None
    for i in range(len(nums) - k + 1):
        sub = nums[i:i+k]
        if all(x > 0 for x in sub):
            s = sum(sub)
            if max_sum is None or s > max_sum:
                max_sum = s
    return max_sum
print(max_subarray_sum([1, 2, 3, -1, 4, 5], 3))
print(max_subarray_sum([0, -2, 3], 2))#20
filter_strings = lambda lst: [w.upper() for w in lst if w.isalpha() and len(w) > 4 and len(set(w.lower())) == len(w)]
print(filter_strings(["hello", "world", "apple", "unique", "abcde"]))#21
def group_by_parity_and_sort(nums):
    evens = []
    odds = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    evens.sort()
    odds.sort()
    return evens + odds
print(group_by_parity_and_sort([5, 2, 8, 3, 7, 4]))#22
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
filter_nums = lambda lst: [lst[i] for i in range(len(lst))
                           if is_prime(i) and lst[i] % 2 == 1 and lst[i] > sum(lst)/len(lst)]
print(filter_nums([1, 15, 7, 9, 20, 11]))#23
def longest_increasing_sublist(nums):
    if not nums:
        return []
    longest = []
    current = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current.append(nums[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [nums[i]]
    if len(current) > len(longest):
        longest = current
    return longest
print(longest_increasing_sublist([1, 2, 3, 1, 2, 3, 4]))#24
filter_lists = lambda lst: [sum(sub)/len(sub) for sub in lst
                            if len(sub) >= 3 and sum(sub) % 2 == 0]
print(filter_lists([[1, 2, 3], [4, 6, 8], [5, 5, 5], [10, 20]]))#25
def remove_duplicates_keep_last(nums):
    seen = set()
    result = []
    for num in reversed(nums):
        if num not in seen:
            seen.add(num)
            result.insert(0, num)
    return result
print(remove_duplicates_keep_last([1, 2, 3, 2, 4, 3, 5]))#26
top5_sorted = lambda lst: sorted(lst, key=lambda w: (-len(w), w))[:5]
print(top5_sorted(["apple", "banana", "pear", "kiwi", "strawberry", "melon", "fig"]))#27