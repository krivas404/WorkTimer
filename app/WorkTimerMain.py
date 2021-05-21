import time
import sys
import datetime

def main():

    TIME_TRANSLATE_CONST = 60
    """
    Constant which is the amount of seconds in minute and minutes in hour
    Needs for translate seconds -> minutes, and minutes -> hours
    """

    def stop_program():
        print("Вы остановили программу.")
        sys.exit()

    def start_program(input_from_kboard):
        """
        Check input from keyboard and exit program if input == q or Q, else keep executing
        """
        if input_from_kboard == "q":
            stop_program()
        elif input_from_kboard == "Q":
            stop_program()
        else:
            now = datetime.datetime.now().strftime('%H:%M:%S')
            print(f"Начало выполнения программы: {now}.")

    def time_counter_for_work(time_for_work, seconds=0, minutes=0, hours=0):
        """Time counter for working time wich count minutes to the end of time_for_work and on"""
        for second in range(time_for_work + 1):
            time.sleep(1)
            seconds += 1
            if seconds % 300 == 0:
                minutes += 5
                print(f"Прошло минут: {minutes}")
            if seconds == time_for_work:
                print(f"Прошло минут: {time_for_work / TIME_TRANSLATE_CONST}")


    def time_counter_for_rest(time_for_rest, seconds=0, minutes=0, hours=0):
        """Time counter for working time wich count minutes to the end of time_for_work and on"""
        for second in range(time_for_rest + 1):
            time.sleep(1)
            seconds += 1
            if seconds % 300 == 0:
                minutes += 5
                print(f"Прошло минут: {minutes}")
            if seconds == time_for_work:
                print(f"Прошло минут: {time_for_rest / TIME_TRANSLATE_CONST}")


    input_from_kboard = str(input("Введите любую клавишу для начала или введите 'Q' для остановки:"))
    print("input:", input_from_kboard)
    flag = start_program(input_from_kboard)
    print("flag:", f'{flag}')


    while True:

        seconds = 0
        minutes = seconds // TIME_TRANSLATE_CONST
        hours = minutes // TIME_TRANSLATE_CONST

        time_for_work = 52 * TIME_TRANSLATE_CONST
        time_for_rest = 18 * TIME_TRANSLATE_CONST

        time_counter_for_work(time_for_work)
        time_counter_for_rest(time_for_rest)


if __name__ == '__main__':
    main()