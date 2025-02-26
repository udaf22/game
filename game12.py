import streamlit as rt


def check(h):
    count_simbol=0
    count_upper=0
    count_down=0
    count_uper=0
    count_ddown=0
    for simbol in h:
        if simbol in '!@#$%^&*()_-+={}[]/\|><~:;':
            count_simbol +=1
        if simbol in 'йцукенгшщзхъёфывапролджэячсмитьбю':
            count_down +=1
        if simbol in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ':
            count_upper +=1
        if simbol in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            count_uper +=1
        if simbol in 'qwertyuiopasdfghjklzxcvbnm':
            count_ddown +=1
    if len(h) <10:
        rt.markdown(':violet[в пароле должно быть 10 букв]')
    elif len(h) >25:
        rt.markdown(':rainbow[в пароле должно быть меньше 25 букв]')
    elif '@#$%' in h:
        rt.markdown(':purple[в пароле должны быть символы @#$%]')
    elif 'АБВГД' in h:
        rt.markdown(':magenta[должны быть первые заглавные буквы алфавита]')
    elif 'эюя' in h:
        rt.markdown(':cyan[последние три буквы алфавита]')
    elif 'опрст' in h:
        rt.markdown(':white[нет]')
    elif 'abcd' in h:
        rt.markdown(':black[первые 4 буквы в англ алфавите]')
    elif '250' not in h:
        rt.markdown(':orange[сколько будет 5*50?]')
    elif count_ddown+count_uper  ==0:
        rt.markdown(':green[где английский?]')
    elif  '8anf' not in h:
        rt.markdown(':blue[enter capcha]')
        rt.image('af.jpg')
    else:
        rt.markdown(':blue[ты сделал надёжный пароль]')
        rt.image('ghj.jpg')

rt.markdown('# :blue[добро пожаловать в password game]')
s =rt.text_input('Enter Password', max_chars=55 )
check(s)