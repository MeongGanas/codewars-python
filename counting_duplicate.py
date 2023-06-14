def duplicate_count(text):
    # Your code goes here
    text = text.lower()
    return len(set([i for i in text if text.count(i) > 1]))


print(duplicate_count("abcde"))
print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))
print(duplicate_count("Indivisibilities"))
print(duplicate_count("aA11"))
print(duplicate_count("ABBA"))
