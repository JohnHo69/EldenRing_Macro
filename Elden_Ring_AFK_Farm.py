import keyboard
import time
import ctypes
import threading

exit_signal = threading.Event()

def reset_exit_signal():
    exit_signal.clear()

def set_exit_signal():
    exit_signal.set()

def turn(direction, angle):
    time.sleep(0.1)
    seconds = (angle * 1.53) / 360
    keyboard.press(direction)
    time.sleep(seconds)
    keyboard.release(direction)

def main_loop():
    time.sleep(2)
    while not exit_signal.is_set():
        #corner
        turn("j",30)
        keyboard.press("w")
        time.sleep(2)
        turn("l",20)
        keyboard.press("r")
        time.sleep(0.05)
        keyboard.release("r")
        time.sleep(3)
        keyboard.release("w")
        turn("l",180)
        #run
        turn("j",10)
        keyboard.press("w")
        time.sleep(1.5)
        keyboard.press("f")
        time.sleep(0.05)
        keyboard.release("f")
        time.sleep(1.5)
        keyboard.press("space")
        time.sleep(0.05)
        keyboard.release("space")
        time.sleep(8)
        turn("j",35)
        time.sleep(2.5)
        turn("l",200)
        time.sleep(0.5)
        keyboard.press("space")
        time.sleep(0.05)
        keyboard.release("space")
        turn("l",10)
        time.sleep(1.5)
        keyboard.release("w")
        #grace 
        time.sleep(2)
        keyboard.press("g")
        time.sleep(0.1)
        keyboard.release("g")
        time.sleep(1)
        keyboard.press("d")
        time.sleep(0.05)
        keyboard.release("d")
        time.sleep(0.5)
        #tp
        keyboard.press("e")
        time.sleep(0.05)
        keyboard.release("e")
        time.sleep(1)
        keyboard.press("e")
        time.sleep(0.05)
        keyboard.release("e")
        time.sleep(7)

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
        print("Pause")
