def solution(text, ending):
    # return ending in text[-len(ending):]
    return text.endswith(ending)


print(solution("abcbcc", "cc"))
