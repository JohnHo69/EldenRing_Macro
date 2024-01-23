import keyboard
import time
import ctypes
import threading
import os

exit_signal = threading.Event()

def sleep(duration, get_now=time.perf_counter):
    now=get_now()
    end=now + duration
    while(now<end):
        now= get_now()

def reset_exit_signal():
    exit_signal.clear()

def set_exit_signal():
    exit_signal.set()

def turn(direction, angle):
    sleep(0.1)
    seconds = (angle * 1.53) / 360
    keyboard.press(direction)
    sleep(seconds)
    keyboard.release(direction)

def main_loop():
    i=0
    seconds=0
    minutes=0
    hours=0
    while not exit_signal.is_set():
        i+=1
        start=time.time()
        #corner
        keyboard.press("w")
        turn("j",30)
        sleep(0.05)
        sleep(2)
        keyboard.press("r")
        sleep(0.05)
        keyboard.release("r")
        turn("l",20)
        sleep(7)
        keyboard.release("w")
        turn("l",170)
        #run
        turn("j",3)
        keyboard.press("w")
        sleep(1.5)
        #gargoyle jump
        keyboard.press("f")
        sleep(0.05)
        keyboard.release("f")
        sleep(1.5)
        keyboard.press("space")
        sleep(0.05)
        keyboard.release("space")
        turn("l",3)
        sleep(1.75)
        turn("j",10)
        #midle of the road
        sleep(7.75)
        turn("j",70) 
        turn("l",100)
        sleep(0.3)
        turn("l",70)
        sleep(0.05)
        turn("l",70)
        keyboard.press("space")
        sleep(0.05)
        keyboard.release("space")
        turn("l",60)
        sleep(1)
        keyboard.press("space")
        sleep(0.05)
        keyboard.release("space")
        turn("l",50)
        keyboard.release("w")
        #grace 
        sleep(4)
        keyboard.press("g")
        sleep(0.1)
        keyboard.release("g")
        sleep(1)
        keyboard.press("d")
        sleep(0.02)
        keyboard.release("d")
        sleep(0.5)
        #tp
        keyboard.press("e")
        sleep(0.05)
        keyboard.release("e")
        sleep(0.5)
        keyboard.press("e")
        sleep(0.05)
        keyboard.release("e")
        sleep(5.5)
        end=time.time()
        seconds+=end-start
        minutes=seconds/60
        if (minutes>60):
            minutes-=minutes
            hours+=1
        os.system('cls')
        print("Run      ->",i)

        print("Run Time ->",hours,"h", round(minutes,2), "m")

        print("Runes    ->",i*1950)

if __name__ == "__main__":
    kernel32 = ctypes.windll.kernel32
    kernel32.SetThreadPriority(kernel32.GetCurrentThread(), 31)
    timer = kernel32.CreateWaitableTimerA(ctypes.c_void_p(), True, ctypes.c_void_p())
    delay = ctypes.c_longlong(int(0.25 * 10000))
    kernel32.SetWaitableTimer(timer, ctypes.byref(delay), 0, ctypes.c_void_p(), ctypes.c_void_p(), False)
    kernel32.WaitForSingleObject(timer, 0xffffffff)
    while True:
        reset_exit_signal()
        keyboard.wait('F8')
        print("Start")

        main_thread = threading.Thread(target=main_loop)
        main_thread.start()

        keyboard.wait('F8')

        set_exit_signal()
        main_thread.join()
        print("\nPause")
