def calculate_pyramid_height(number_of_block: int) -> int:
    height = 0
    number = number_of_block
    i = 1

    while number >= i * i:
        number -= i * i
        height += 1
        i += 1

    return height
