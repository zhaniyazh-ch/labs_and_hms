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