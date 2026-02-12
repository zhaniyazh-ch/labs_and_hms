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