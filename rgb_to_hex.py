def rgb(*args):
    # your code here :)
    def calculate(rgb):
        a = [int(rgb/16), int(float("0." + str(rgb/16).split(".")[1]) * 16)]
        for i in a:
            if i >= 10:
                res.append(chr(i+55))
            else:
                res.append(str(i))
    res = []
    for rgb in args:
        if rgb > 0:
            if rgb > 255:
                rgb = 255
            calculate(rgb)
        else:
            rgb = 0
            calculate(rgb)
    return ''.join(res)

# def rgb(r, g, b):
#     def round(x): return min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))


print(rgb(-20, 275, 125))
