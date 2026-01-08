def calculate_pyramid_height(number_of_block:int) ->int:
    height=0
    number=number_of_block
    i=1
    while number>0:
        number=number-i
        i +=1
        height +=1
        

    

    return height
