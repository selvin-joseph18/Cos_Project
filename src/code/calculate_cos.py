'''
Python program to calculate Cosine of an angle
'''
import math
import logging
logging.basicConfig(filename='My_config.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='w')

def calculate_cos(angle):
    '''
    Function to calculate Cosine of an angle
     '''

    try:
        res = math.cos(angle)
        return res
    except TypeError as type_error:
        logging.error(type_error.message)


    # else:
    #     print('cosine of angle{} is {}'.format(angle,res))



