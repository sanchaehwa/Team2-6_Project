import time
import threading
from datetime import datetime

# 타이머 기능 구현
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # 현재 타이머 시간 출력
        time.sleep(1)
        t -= 1
    print("Timer Completed!")


# 메인 함수
def main():

  try:
        print("\n\n Select mode (1. Stopwatch, 2. Timer): ", end="")
        mode = input()


        if mode == '1':
#            stopwatch() 구현 필요
        elif mode == '2':
            try:
                t = int(input("Enter time in seconds: "))
                countdown(t)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        else:
            print("Invalid mode selected.")
  except KeyboardInterrupt: 
        print("\nShutdown by user")


if __name__ == "__main__":
    main()