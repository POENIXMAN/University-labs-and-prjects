def special_sum(numX,numY):
    '''(num)-> num
    This function sums to number and outputs the result
    in a very interesting way

    >>>special_sum(3,4)
    Your sum is 7
    >>>special_sum(9,4)
    Your sum is 20
    '''
    sum = numX+numY
    if sum in range(10,19):
        sum = 20
        return print(f'Your sum is {sum}')
    else:
        return print(f'Your sum is {sum}')


special_sum(9,4)

def cat_dog(str):
    '''(string)->bool
    This function returns 'True' if string has 
    the same repetition of cats and dogs

    >>>cat_dog('catdog')

    True
    >>>cat_dog('catcat')

    False
    '''
    answer = str.count('cat') == str.count("dog")
    if answer is True:
        return print('True')
    else:
        return print('False')

        



cat_dog('1cat1cadodog')