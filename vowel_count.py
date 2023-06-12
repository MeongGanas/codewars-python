def get_count(sentence):
    return sum(1 for i in sentence if i.lower() in "aiueo")


print(get_count("oakfoek"))
