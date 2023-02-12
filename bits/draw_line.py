def draw_line(screen, w, x1, x2, y):
    base = w // 8 * y
    start = x1 // 8
    end = x2 // 8
    start_mask = 0xff >> x1 % 8
    end_mask = (-1 << (8 - (x2 % 8 + 1))) & 0xff
    for i in range(w // 8):
        j = base + i
        if i < start or i > end:
            screen[j] = 0
        elif i > start and i < end:
            screen[j] = 0xff
        else:
            if start == end:
                screen[j] = start_mask & end_mask
            else:
                if i == start:
                    screen[j] = start_mask
                else:
                    screen[j] = end_mask
    return screen

w = 40
h = 5
screen = [0] * (w // 8 * h)
print(draw_line(screen, w, 3, 5, 0))


