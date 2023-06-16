def solution(s):
    return ''.join(" " + i if i.isupper() else i for i in s)


print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))
print(solution(""))
