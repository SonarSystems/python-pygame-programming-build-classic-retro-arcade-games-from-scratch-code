def rects_overlap(a, b):
    return (a.left < b.right and a.right > b.left and
            a.top < b.bottom and a.bottom > b.top)
