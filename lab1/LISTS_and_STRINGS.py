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