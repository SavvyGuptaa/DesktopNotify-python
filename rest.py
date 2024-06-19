from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
        title ="TAKE A BREAK!!",
        message = "drink some water",
        timeout=5)
        time.sleep(20)  

# to run python file in background >>pythonw file.py
