import re


def to_camel_case(text):
    text = re.split(r"-|_", text)
    return text[0] + ''.join([i.capitalize() for i in text if text.index(i) > 0])


print(to_camel_case("the-stealth-warrior"))
