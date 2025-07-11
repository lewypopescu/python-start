picture = [

    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0,],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0 ,0 ,1 ,1 ,0 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0]

    ]

pixels_go = "*"
pixels_no_go = " "

for row in picture:
    for pixel in row:
        if pixel == 1:
            print(pixels_go, end="")
        else:
            print(pixels_no_go, end="")
    print()
