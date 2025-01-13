# medium

# overcomplicated, one pass counting the number of every color also works


def sort_colors(colors):
    # sort an array of colors to red, white, blue order
    red, white, blue = 0, 0, len(colors) - 1  # pointers

    while white <= blue:  # this is also a tricky condition
        # color checking: red 0, white 1, blue 2
        if colors[white] == 0:
            if colors[red] != 0:
                # swap red and white
                colors[red], colors[white] = colors[white], colors[red]

            red += 1
            white += 1
        elif colors[white] == 1:
            white += 1
        else:  # colors[white] == 2
            if colors[blue] != 2:
                # swap white and blue
                colors[white], colors[blue] = colors[blue], colors[white]

            blue -= 1  # this is the tricky part to move blue only

    return colors
