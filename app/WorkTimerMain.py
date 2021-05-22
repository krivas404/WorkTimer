import time
import sys
import datetime


def main():
    TIME_TRANSLATE_CONST = 60
    """
    Constant which is the amount of seconds in minute and minutes in hour
    Needs for translate seconds -> minutes, and minutes -> hours
    """

    def exit_program():
        print("You stopped the program.")
        sys.exit()

    def start_program(input_from_kboard):
        """Check input from keyboard and exit program if input equals 'q' or 'Q', else keep executing"""
        if input_from_kboard == "q":
            exit_program()
        elif input_from_kboard == "Q":
            exit_program()
        else:
            now = datetime.datetime.now().strftime('%H:%M:%S')  # Current time
            print(f"Start program at: {now}.")

    def time_counter_for_work(time_for_work, seconds=0, minutes=0, hours=0):
        """Time counter for working time which count minutes to the end of time_for_work and on"""
        print("Start work time")
        for second in range(time_for_work + 1):
            time.sleep(1)
            seconds += 1
            if seconds % 300 == 0:
                minutes += 5
                print(f"Minutes of work passed: {minutes}")
            if seconds == time_for_work:
                print(f"Minutes of work passed: {time_for_work / TIME_TRANSLATE_CONST}\nWork is over!")

    def time_counter_for_rest(time_for_rest, seconds=0, minutes=0, hours=0):
        """Time counter for working time which count minutes to the end of time_for_work and on"""
        print("Start rest time")
        for second in range(time_for_rest + 1):
            time.sleep(1)
            seconds += 1
            if seconds % 300 == 0:
                minutes += 5
                print(f"Minutes of rest passed: {minutes}")
            if seconds == time_for_work:
                print(f"Minutes of rest passed: {time_for_rest / TIME_TRANSLATE_CONST}\nRest is over!")

    input_from_kboard = str(input("Input any key for start or 'q' for quit:"))
    print("input:", input_from_kboard)
    start_program(input_from_kboard)

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