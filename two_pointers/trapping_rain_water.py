# hard


def rain_water(heights):
    # find out max height on two sides
    max_height_left, max_height_right = 0, 0
    left, right = 0, len(heights) - 1

    while left < right:
        if heights[left] > max_height_left:
            max_height_left = heights[left]

        if heights[right] > max_height_right:
            max_height_right = heights[right]

        left += 1
        right += 1

    water_level = min(max_height_left, max_height_right)

