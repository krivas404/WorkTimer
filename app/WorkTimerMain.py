import time
import sys
import datetime

def main():

    TIME_TRANSLATE_CONST = 60
    """
    Constant which is the amount of seconds in minute and minutes in hour
    Needs for translate seconds -> minutes, and minutes -> hours
    """

    def start_program(input_from_kboard):
        """
        :param input_from_kboard:
        :return:
        """
        if input_from_kboard == 1:
                # "q" or "Q":
            print("Вы остановили программу.")
            # flag = False
            sys.exit()
        else:
            now = datetime.datetime.now().strftime('%H:%M:%S')
            print(f"Начало выполнения программы: {now}.")
            flag = True
        return flag

    def time_counter_for_work(time_for_work, seconds=0, minutes=0, hours=0):
        """Time counter for working time wich count minutes to the end of time_for_work and on"""
        for second in range(time_for_work):
            time.sleep(60)
            seconds += 60
            if second % 500 == 0:
                minutes += 5



            print(f"Прошло {i / 60} минут ")


    input_from_kboard = str(input("Введите любую клавишу для начала или введите 'Q' для остановки:"))
    print("input:", input_from_kboard)
    flag = start_program(input_from_kboard)
    print("flag:", f'{flag}')

    while flag:

        seconds = 0
        minutes = seconds // TIME_TRANSLATE_CONST
        hours = minutes // TIME_TRANSLATE_CONST

        time_for_work = 52 * TIME_TRANSLATE_CONST
        time_for_rest = 18 * TIME_TRANSLATE_CONST


if __name__ == '__main__':
    main()