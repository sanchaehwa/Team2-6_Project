import time
import threading
from datetime import datetime
'''# 현재 시간 표시
def display_time():
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\r {now}", end="")
        time.sleep(1) '''
# 스탑워치 기능 구현    
def stopwatch():
    print("스톱워치 Start : Enter , End : Control+C")
    input()  # 시작을 위한 Enter 입력
    print('Start')
    starttime = time.time()
    lasttime = starttime
    lapnumber = 1


    try:
        while True:
            input()  # 랩 기록을 위한 Enter 입력
            laptime = round(time.time() - lasttime, 2)
            totaltime = round(time.time() - starttime, 2)
            print(f'Lap {lapnumber}: {totaltime}초 (Lap Time: {laptime}초)')
            lasttime = time.time()  # 마지막 시간 업데이트
            lapnumber += 1
    except KeyboardInterrupt:
        print('\n\nEnd of Stopwatch')


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
  '''  time_thread = threading.Thread(target=display_time, daemon=True)
    time_thread.start()'''
  try:
        print("\n\n Select mode (1. Stopwatch, 2. Timer): ", end="")
        mode = input()


        if mode == '1':
            stopwatch()
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