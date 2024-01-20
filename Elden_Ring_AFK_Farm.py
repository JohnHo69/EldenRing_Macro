import keyboard
import time
import ctypes

#give priority to minimize time.sleep inaccuracy
kernel32 = ctypes.windll.kernel32
kernel32.SetThreadPriority(kernel32.GetCurrentThread(), 31)
timer = kernel32.CreateWaitableTimerA(ctypes.c_void_p(), True, ctypes.c_void_p())
delay = ctypes.c_longlong(int(.25 * 10000))
kernel32.SetWaitableTimer(timer, ctypes.byref(delay), 0, ctypes.c_void_p(), ctypes.c_void_p(), False)
kernel32.WaitForSingleObject(timer, 0xffffffff)

def turn(direction,angle):
    seconds=(angle*1.53)/360
    keyboard.press(direction)
    time.sleep(seconds)
    keyboard.release(direction)

time.sleep(2)
while(1):
    #corner
    turn("j",30)
    keyboard.press("w")
    time.sleep(2)
    turn("l",20)
    keyboard.press("r")
    time.sleep(0.05)
    keyboard.release("r")
    time.sleep(4)
    keyboard.release("w")
    turn("l",170)

    #run
    keyboard.press("w")
    time.sleep(3)
    keyboard.press("space")
    time.sleep(0.05)
    keyboard.release("space")
    time.sleep(9)
    turn("j",30)
    time.sleep(2)
    turn("l",200)
    time.sleep(0.5)
    keyboard.press("space")
    time.sleep(0.05)
    keyboard.release("space")
    time.sleep(1.5)
    keyboard.release("w")

    #ver pedra nas costas
    keyboard.press("s")
    turn("j",180)
    time.sleep(0.5)
    keyboard.release("s")
    time.sleep(0.5)
    
    #grace
    keyboard.press("g")
    time.sleep(0.1)
    keyboard.release("g")
    keyboard.press("d")
    time.sleep(0.37)
    keyboard.release("d")
    keyboard.press("s")
    time.sleep(0.18)
    keyboard.release("s")
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

exit(1)
