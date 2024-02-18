from collections import deque


def polyndrome(text):
    d = deque()
    for word in text.lower().replace(" ", ""):
        d.append(word)

    is_polyndrome = True
    for _ in range(len(d) // 2):
        if d.pop() != d.popleft():
            is_polyndrome = False
            break

    return is_polyndrome


print(polyndrome("Я несу гусеня"))
print(polyndrome("Козак з казок"))
print(polyndrome("Уже лисі ліси Лежу"))
print(polyndrome("І що сало Ласощі"))
print(polyndrome("abcba"))
print(polyndrome("4545"))
