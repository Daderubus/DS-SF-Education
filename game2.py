"""Gues a number"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Random guess a number

    Args:
        number (int, optional): guessed number. Defaults to 1.

    Returns:
        int: counts
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
        
    return(count)

#print(f'Counts : {random_predict(10)}')


def score_game(random_predict) -> int:
    """Mean value of counts for 1000 attempts

    Args:
        random_predict ([type]): function

    Returns:
        int: mean value of attempts
    """
    
    count_list = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = 1000)
    
    for number in random_array:
        count_list.append(random_predict(number))
    
    score = int(np.mean(count_list))
    print(f'You algorithm guess a number for {score} counts')
    return score

#RUN
score_game(random_predict)

