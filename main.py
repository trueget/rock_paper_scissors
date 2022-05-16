import random
print('Игра в камень, ножницы, бумага! Введи на клавиатуре!')
b = ['бумага', 'папир','бум','papir','pap','map','б','b']
k = ['камень', 'камушек', 'stone', 'кам', 'к', 'k','колодец', 'кол']
n = ['ножницы','ножници','нож','н','n','scissors']


while True:
    ran_ch = random.choice(['бумага', 'камень', 'ножницы'])
    my_ch = input()
    if my_ch == 'stop' or my_ch == 'Стоп' or my_ch == 'стоп':
        print('До свидания!')
        break
    elif my_ch not in b and my_ch not in k and my_ch not in n:
        print('вы ввели непонятный символ!')
    else:
        if ran_ch in b:
            if my_ch in b:
                print(f'ничья - компьютер выбрал {ran_ch}')
            elif my_ch in k:
                print(f'вы проиграли - компьютер выбрал {ran_ch}')
            elif my_ch in n:
                print(f'вы выиграли - компьютер выбрал {ran_ch}')
        elif ran_ch in k:
            if my_ch in b:
                print(f'вы выиграли - компьютер выбрал {ran_ch}')
            elif my_ch in k:
                print(f'ничья - компьютер выбрал {ran_ch}')
            elif my_ch in n:
                print(f'вы проиграли - компьютер выбрал {ran_ch}')
        elif ran_ch in n:
            if my_ch in b:
                print(f'вы проиграли - компьютер выбрал {ran_ch}')
            elif my_ch in k:
                print(f'вы выиграли - компьютер выбрал {ran_ch}')
            elif my_ch in n:
                print(f'ничья - компьютер выбрал {ran_ch}')
        else:
            print('компьютер вас не понял', ran_ch, my_ch)
