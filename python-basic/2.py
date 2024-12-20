def reverse_words_order_and_swap_cases(sentence):
    r = []
    for w in sentence.split(" ")[::-1]:
        for l in list(w):
            if l.isupper():
                r.append(l.lower())
            else:
                r.append(l.upper())
        r.append(" ")
    return "".join(r)
print(reverse_words_order_and_swap_cases("cOdInG IS AWEsome"))
