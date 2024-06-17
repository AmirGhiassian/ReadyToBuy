from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pywhatkit as whatsapp
import sys
from time import sleep
# The variable that holds the main driver we will communicate with.
driver = WebDriver.chrome()

# Saving the number of arguments so that we can do error checking.
num_args = len(sys.argv)

# This variable will keep the current price and check if the price has changed by using the class name
# and finding it on the page using selenium.
saved_price = 0

def remove_text(text):
    cleaned_text = ""
    for currency in currency_list:
        
# This function will start the checking process.
def start_check(phone_number, message, url, class_name, price, interval):
    driver.get(url)
    try:
        page_price = int(driver.find_element(By.CLASS_NAME, class_name).text.lower()..replace("CAD")replace("$", "").replace(",", ""))
    except ValueError:
        print("ERROR: The price on the page is not a number!")
        return
    

# The function that sends the message to the user.
def send_whatsapp_message(phone_number, message):
    # This function will send a message to the user using the pywhatkit library, here is how it works:
    # sendwhatmsg_instantly(phone_no: str, message: str, wait_time: int = 15, tab_close: bool = False, close_time: int = 3) -> None
    whatsapp.sendwhatmsg_instantly(phone_number, message, 0, 0)


    
# The error checking depending on how many arguments are passed to the program. If the user gives no parameters, the help menu pops up.
# If the user gives less than 6 parameters, the program will tell the user that they are missing arguments.
# If the user gives more than 6 parameters, the program will tell the user that they have too many arguments.
if num_args == 0:
    print('''ReadyToBuy: A tool that will send you a message when a price on a online store goes on sale!\n
          Usage: python main.py [phone_number] [message] [url] [class_name] [price] [interval]\n
          Please note that the price will be appeneded at the end of the message\n''')
elif num_args < 6:
    print("ERROR: You are missing arguments!")
elif num_args > 6:
    print("ERROR: Too many arguments!")
else:
    start_check(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])



