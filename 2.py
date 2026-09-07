def input_numbers():
    '''

    :param x: enter a number
    :return: valid two numbers
    '''
    while True:
        try:
            x = int(input('enter a number: '))
        except ValueError as e:
            print('invalid input', e)
        else:
            return x
x = input_numbers()
y = input_numbers()







