import string
def analyze_students(data):
    def has_digits(s):
        return any(ch.isdigit() for ch in s)
    def sum_digits(num):
        return sum(int(d) for d in str(num) if d.isdigit())
    def is_palindrome(word):
        return word == word[::-1]
    vowels = set("aeiou")
    students = []
    for st in data:
        if not has_digits(st["name"]):
            st["name"] = st["name"].title()
            students.append(st)
    for st in students:
        processed = []
        for g in st["grades"]:
            if g <= 0:
                continue
            if g % 2 == 1 and g < 10:
                processed.append(sum_digits(g))
            elif g % 2 == 0 and g >= 10:
                processed.append(g ** 2)
            else:
                processed.append(g)
        st["processed_grades"] = processed
    all_words_per_student = []
    all_vowels = set()
    for st in students:
        text = " ".join(st["comments"]).lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = set(text.split())
        valid_words = {w for w in words if len(w) >= 4 and not is_palindrome(w)}
        all_words_per_student.append(valid_words)
        for w in valid_words:
            all_vowels |= {ch for ch in w if ch in vowels}
        st["words"] = valid_words
    word_counts = {}
    for words in all_words_per_student:
        for w in words:
            word_counts[w] = word_counts.get(w, 0) + 1
            word_counts = {w: c for w, c in word_counts.items() if c >= 2}
            word_counts = dict(sorted(word_counts.items(), key=lambda x: (-x[1], x[0])))
            students_by_avg = sorted(
                students,
                key=lambda s: (
                    - (sum(s["processed_grades"]) / len(s["processed_grades"]) if s["processed_grades"] else 0),
                    s["name"])
            )
            students_by_avg = [s["name"] for s in students_by_avg]
            students_by_name_length = {}
            for st in students:
                l = len(st["name"])
                if l not in students_by_name_length:
                    students_by_name_length[l] = []
                if st["name"] not in students_by_name_length[l]:
                    students_by_name_length[l].append(st["name"])
            return {
                "students": [{"name": s["name"], "processed_grades": s["processed_grades"]} for s in students],
                "word_counts": word_counts,
                "all_vowels": all_vowels,
                "students_by_avg": students_by_avg,
                "students_by_name_length": students_by_name_length
            }
        students_data = [
            {"name": "Alice123", "grades": [12, 9, 15, 8],
             "comments": ["Good work", "excellent effort", "Needs Improvement"]},
            {"name": "Bob", "grades": [25, 9, 0, -3], "comments": ["Good job", "Needs improvement"]}
        ]
        result_students = analyze_students(students_data)
        print("Результат анализа студентов:")
        print(result_students)