import pyautogui as pg
import time
print("First Open your WhatsApp Web.")
user_input=input("Enter message :")
mass_num=int(input("Number of messages :"))
print("Now go to your WhatsApp Web and click in message box.")
print("Wait for sometime and see the magic.")
time.sleep(10)
for i in range(mass_num):
    pg.write(user_input)
    pg.press('enter')
print("Thank You for using this application")
