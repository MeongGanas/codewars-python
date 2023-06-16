def bouncing_ball(h, bounce, window):
    # your code
    if h > 0 and (bounce > 0 and bounce < 1) and window < h:
        count = 1
        h = h * bounce
        while h > window:
            h *= bounce
            count += 2
        return count
    return -1


print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(30, 0.66, 1.5))
