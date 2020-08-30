import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v3(number):
    '''The random value will be generated between min and max values. 
    After each unsuccessful prediction attempt we narrow down the 'randint' range by adjusting the min and max
    values'''

    min = 1 
    max = 101
    count = 0

    while True:
        count+=1
        predict = np.random.randint(min,max)
        if number > predict: 
            min = predict # no need to check values less than current "predict" in future
        elif number < predict: 
            max = predict # no need to check values greater than current "predict" in future
        else: break
    return(count) # выход из цикла, если угадали

score_game(game_core_v3)