def generate_hashtag(s):
    # your code here
    res = ["#"] + [i.title() for i in s.split(" ")]
    return False if len(s) < 1 or len(''.join(res)) > 140 else ''.join(res)


print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong'))
