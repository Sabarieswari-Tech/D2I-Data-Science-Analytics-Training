def length_of_last_word(s):
    words = s.split()

    if len(words) == 0:
        return 0

    return len(words[-1])


s = " Embedded Python "

print("Length of last word:", length_of_last_word(s))