""" Given  an  image  represented  by  an  NxN  matrix, 
    where  each  pixel  in  the  image  is  4 bytes, 
    write a method to rotate the image by 90 degrees
    
    Can you do this in place? """

def polywhirl (morpheus):
    # My solution: reverse the matrix and then reflect across the diagonal.

    n = len(morpheus[0])

    for x in morpheus:
        x.reverse()

    left_x = 0
    original_left_y = n - 1
    left_y = original_left_y
    original_right_x = 0
    right_x = original_right_x
    right_y = n - 1
    lower_turns = n

    for extra_turns in range(0, n):
        for turns in range(0, lower_turns):
            temp = morpheus[right_x][right_y]
            morpheus[right_x][right_y] = morpheus[left_x][left_y]
            morpheus[left_x][left_y] = temp
            left_y -= 1
            right_x += 1
        left_x += 1
        right_y -= 1
        lower_turns -= 1
        original_right_x += 1
        right_x = original_right_x
        original_left_y -= 1
        left_y = original_left_y
        
    return morpheus

polywhirl(neo)
