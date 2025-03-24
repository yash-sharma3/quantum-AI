import speech_recognition as sr
# Import QRCode from pyqrcode 
import pyqrcode
import pygetwindow as gw
from barcode import EAN13 
from pynput.keyboard import Key,Controller
import webbrowser
import pyautogui
from colorama import Fore,init,Style
import threading
from docx import Document
import psutil
from GoogleNews import GoogleNews
import winsound
from PIL import Image
import urllib.parse
import phonenumbers
from phonenumbers import timezone
import google.generativeai as genai
from phonenumbers import geocoder
from phonenumbers import carrier
from deep_translator import GoogleTranslator
from requests import get
import ctypes
import speedtest
from time import sleep
import pyqrcode 
import queue
import png
import winshell
import pyttsx3
import pyjokes
from playsound import playsound
import time
from bs4 import BeautifulSoup
import os
import subprocess as sp
import requests
import wikipedia
import pywhatkit as kit  
import smtplib
from datetime import date
from pprint import pprint
import datetime
from datetime import datetime
import random
from pygame import mixer
mixer.init()
from rich.progress import track
import sys
import pyfiglet 


#########################################################################################################################################################

def process_data():
    for step in track(range(100), description="Processing..."):
        time.sleep(0.1)  # Simulate a task taking time

process_data()

#########################################################################################################################################################






#########################################################################################################################################################

def design_welcome_screen():
        result = pyfiglet.figlet_format("WELCOME Dr. Yash Sharma", font = "slant" ) 
        print(result) 

#########################################################################################################################################################








#########################################################################################################################################################

# Open the file in read mode
with open('enter your file path', 'r') as file:
    # Read the password
    password = file.read().strip()

a= input("Enter the password: ")

if a == password:
    print("Correct Password")
else:
    print("Wrong Password")
    sys.exit()

#########################################################################################################################################################


design_welcome_screen()


#########################################################################################################################################################


# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')

# Configure engine properties
engine.setProperty('rate', 170)  # Set speaking rate
engine.setProperty('volume', 1.0)  # Set volume level
engine.setProperty('voice', engine.getProperty('voices')[0].id)  # Set voice to female


def speak(text):
    """Speak the given text using the text-to-speech engine."""
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 180)  # Adjust speaking rate for subsequent calls


"""




engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 170)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
speech_queue = queue.Queue()

def process_speech():
    while True:
        text = speech_queue.get()
        if text is None:  # Stop signal
            break
        engine.say(text)
        engine.runAndWait()
        engine.setProperty('rate', 180)

# Start a separate thread for speech synthesis
speech_thread = threading.Thread(target=process_speech, daemon=True)
speech_thread.start()

def speak(text):
    speech_queue.put(text)  # Add text to the queue
    
"""

#########################################################################################################################################################







#########################################################################################################################################################

import MySQLdb

db = MySQLdb.connect("localhost","Name","password", "Database name")
cursor = db.cursor()

sql= f"""INSERT INTO yash_db.jarvis_access (Accessed_at, Time) VALUES
        ('Accessed', CURRENT_TIMESTAMP)
        """

cursor.execute(sql)
db.commit()
print("Successfull Data has recorded in the DataBase")
# disconnect from server
db.close()
# prepare a cursor object using cursor() method
cursor = db.cursor()

#########################################################################################################################################################









# Mail Checker

#########################################################################################################################################################


import imaplib
import email
import threading

# Your Email Credentials
EMAIL_USER = "Enter your email"
EMAIL_PASS = "Enter your email-app password"
IMAP_SERVER = "imap.gmail.com"

# Track Seen Emails
seen_emails = set()

print("📧 Email checker started ")

# Function to Get Email Content & Attachments
def get_email_content_and_attachments(msg):
    content = ""
    attachments = []

    for part in msg.walk():
        content_type = part.get_content_type()
        filename = part.get_filename()

        # Extract plain text content
        if content_type == "text/plain" and not filename:
            content = part.get_payload(decode=True).decode(errors="ignore")

        # Check for attachments
        if filename:
            attachments.append(filename)

    return content.strip(), attachments

# Function to Check for New Emails
def check_email():
    global seen_emails
    while True:
        try:
            mail = imaplib.IMAP4_SSL(IMAP_SERVER)
            mail.login(EMAIL_USER, EMAIL_PASS)
            mail.select("inbox")

            result, data = mail.search(None, "UNSEEN")  # Get Unread Emails
            mail_ids = data[0].split()

            new_mails = [mail_id for mail_id in mail_ids if mail_id not in seen_emails]

            for mail_id in new_mails:
                result, msg_data = mail.fetch(mail_id, "(RFC822)")
                raw_email = msg_data[0][1]
                msg = email.message_from_bytes(raw_email)

                sender = msg["From"]
                subject = msg["Subject"]
                body, attachments = get_email_content_and_attachments(msg)

                print("----------------------------------------------------------------------------------------------------------------------------------------------------")


                print("")
                print(f"\n📧 New Email from: {sender}\n🔹 Subject: {subject}\n📜 Message:\n{body}")
                print("")

                print("----------------------------------------------------------------------------------------------------------------------------------------------------")

                winsound.Beep(700,1000)
                
                

                # Print Attachments
                if attachments:
                    print("📎 Attachments:")
                    print("Attachments are there in email")
                    for attachment in attachments:
                        print(f"   - {attachment}")
                        speak(f"   - {attachment}")

                print("-" * 50)

                seen_emails.add(mail_id)  # Mark Email as Seen

            mail.logout()
        except Exception as e:
            print("Error checking email:", str(e))

        time.sleep(3)  # Check emails every 3 seconds





#########################################################################################################################################################











# Whatsapp message using Twillio


#########################################################################################################################################################

from twilio.rest import Client

def sendmessage(message):
    account_sid = 'Enter your Acount sid'
    auth_token = 'Enter your Auth Token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='Twillio phone number',
    body=f'{message}',
    to='whatsapp:+91+your phone number'
    )

    print(message.sid)

#########################################################################################################################################################










#########################################################################################################################################################

# Function to execute commands
import sys



def execute_command(command):
    if 'open' in command:
        # Logic to open software
        software_name = command.split('open')[1].strip()
        os.system(f'start {software_name}')  # Windows-specific command to open software

    elif 'restart'in command:
        speak("Restarting the system")
        os.system("shutdown /r /t 1")
        

    elif 'shut down' in command:
        speak("shuting down the system")
        # Logic to shut down PC
        os.system("shutdown /s /t 1")  # Windows-specific command to shut down PC

#########################################################################################################################################################







# Enhanced Battery Alert

#########################################################################################################################################################

def jarvis_battery_alert(threshold, interval):
    # Get the battery information
    battery = psutil.sensors_battery()

    if battery is not None:
        battery_percent = battery.percent
        # Check if the battery level is below the threshold and if it's not plugged in
        if battery_percent < threshold and not battery.power_plugged:
            print(f"Jarvis: Warning! Battery is low at {battery_percent}%")
            winsound.Beep(1000, 1000)  # frequency=1000 Hz, duration=1000 ms
            speak(f"Battery is low at {battery_percent}%")
            sendmessage(f"Battery is low at {battery_percent}%")
        else:
            print(f"Jarvis: Battery is at {battery_percent}%. Everything is good.")

    else:
        print("Jarvis: No battery information available.")

    # Schedule the next battery check after the specified interval
    threading.Timer(interval, jarvis_battery_alert, [threshold, interval]).start()

# Example usage: Monitor battery every 60 seconds with a threshold of 20%
threshold = 20
interval =300
jarvis_battery_alert(threshold, interval)

#########################################################################################################################################################








# Full Battery Alert

#########################################################################################################################################################

def full_battery_alert(threshold, interval):
    # Get the battery information
    battery = psutil.sensors_battery()

    if battery is not None:
        battery_percent = battery.percent
        # Check if the battery level is below the threshold and if it's not plugged in
        if battery_percent==threshold and battery.power_plugged:
            print(f"Sir battery is fully charged , please plug it out")
            speak(f"Sir battery is fully charged , please plug it out")
            sendmessage(f"Sir battery is fully charged , please plug it out")
        else:
            pass

    else:
        print("Jarvis: No battery information available.")

    # Schedule the next battery check after the specified interval
    threading.Timer(interval, full_battery_alert, [threshold, interval]).start()

# Example usage: Monitor battery every 60 seconds with a threshold of 20%
threshold = 100
interval =300
full_battery_alert(threshold, interval)

#########################################################################################################################################################











#########################################################################################################################################################

def takeCommand():

    r = sr.Recognizer()
    r.dynamic_energy_threshold=True
    r.energy_threshold=100
    r.dynamic_energy_adjustment_damping=0.03
    r.dynamic_energy_ratio=1.5
    r.pause_threshold=0.4
    r.operation_timeout = None
    r.non_speaking_duration=0.5
	
    with sr.Microphone() as source:
		
        print(Fore.LIGHTGREEN_EX + "Listening..." ,end="" , flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        print("",end="",flush=True)
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10, phrase_time_limit=3)

    try:
        print("\r"+Fore.LIGHTYELLOW_EX + "Recognizing..." ,end="" , flush=True)
        command = r.recognize_google(audio,language="hi-IN")
        if command:
            command = translate_hindi_to_english(command).lower()
        print(f"\r"+Fore.BLUE + "You said:", command)

    
    except sr.WaitTimeoutError:

        print("\r"+"Listening timed out. No speech detected.")

    except Exception as e:
        print(e) 
        print("\r"+"Unable to Recognize your voice.") 
        return "None"

    return command
	
#########################################################################################################################################################











#########################################################################################################################################################

import datetime

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")  

    speak(f"sir current time is"+ datetime.datetime.now().strftime("%H:%M") )
    speak(f"Hi i am Jarvis. Please tell me how can I help you")

#########################################################################################################################################################





def translate_hindi_to_english(txt):
    translated_text = GoogleTranslator(source="hi", target="en").translate(txt)
    return translated_text





keyboard = Controller()

# Main loop
# Start Email Checker in a Separate Thread
email_thread = threading.Thread(target=check_email, daemon=True)
email_thread.start()
wishMe()
hi_count = 0


init(autoreset=True)

while True:
    try:
        

        r = sr.Recognizer()
        r.dynamic_energy_threshold = True  # Auto-adjusts sensitivity
        r.energy_threshold = 100  # Lowered to detect quieter speech
        r.pause_threshold = 0.2  # Waits for you to finish speaking
        r.non_speaking_duration = 0.1  # Allows short pauses without stopping
        r.dynamic_energy_adjustment_damping = 0.03
        r.dynamic_energy_ratio = 1.5
            

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            print(Fore.LIGHTGREEN_EX + "Listening..." ,end="" , flush=True)
            print(Style.RESET_ALL,end="",flush=True)
            print("",end="",flush=True)
                
                    
            audio = r.listen(source,timeout=15, phrase_time_limit=2)

        print("\r"+Fore.LIGHTYELLOW_EX + "Recognizing..." ,end="" , flush=True)

        command = r.recognize_google(audio,language="hi-IN")
        if command:
            command = translate_hindi_to_english(command).lower()
            print(f"\r"+Fore.BLUE + "You said:", command)
                    
                    
                    






            #threading part


#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################



#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################




        
        paths = {

                        'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
                        'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
                        'calculator': "C:\\Windows\\System32\\calc.exe",
}
        


# Book Search

#########################################################################################################################################################
#########################################################################################################################################################


        def search_books(query):
            try:
                url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
                response = requests.get(url).json()
                if 'items' in response:
                    books = response['items'][:5]
                    book_list = []
                    for book in books:
                        book_title = book['volumeInfo']['title']
                        book_authors = ", ".join(book['volumeInfo']['authors']) if 'authors' in book['volumeInfo'] else "Unknown author"
                        book_list.append(f"{book_title} by {book_authors}")
                    return "\n".join(book_list)
                else:
                    return "No books found."
            except Exception as e:
                return f"Error fetching books: {e}"
            
#########################################################################################################################################################
#########################################################################################################################################################







# Amazon Search
            
#########################################################################################################################################################
#########################################################################################################################################################


        def search_amazon( query):
            try:
                base_url = "https://www.amazon.com/s"
                params = {'k': query}
                response = requests.get(base_url, params=params)
                soup = BeautifulSoup(response.content, 'html.parser')
                result = soup.find('span', {'class': 'a-color-base'}).text.strip()
                return f"Top result on Amazon for {query}: {result}"
            except Exception as e:
                return f"Error searching Amazon: {e}"
            
#########################################################################################################################################################
#########################################################################################################################################################








# Opening softwares


#########################################################################################################################################################
#########################################################################################################################################################

        #def open_camera():
           #sp.run('start microsoft.windows.camera:', shell=True)

        def open_calculator():
           sp.Popen(paths['calculator'])

        def open_cmd():
           os.system('start cmd')

        def open_discord():
           os.startfile(paths['discord'])
        
        def open_notepad():
           os.startfile(paths['notepad'])

        def open_chrome():
           os.startfile("C:\\Your file path\\OneDrive\\Desktop\\chrome.exe")


#########################################################################################################################################################
#########################################################################################################################################################










# Gemini Api requests

#########################################################################################################################################################
#########################################################################################################################################################

        genai.configure(api_key="Enter Your API key") # Get api on https://aistudio.google.com

        # Function to interact with Gemini
        def chat_with_gemini(prompt):
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content(prompt)
            return response.text
        
#########################################################################################################################################################
#########################################################################################################################################################









# Current Window

#########################################################################################################################################################
#########################################################################################################################################################

        def get_active_window_title():
            active_window = gw.getActiveWindow()
            print(f"Active window: {active_window}")
            speak(f"Sir currently you are on {active_window}")

#########################################################################################################################################################
#########################################################################################################################################################








# Riddle

#########################################################################################################################################################
#########################################################################################################################################################
            
        def get_riddle():
            try:
                url = "https://api.funtranslations.com/translate/riddle/api"
                response = requests.get(url).json()
                riddle = response['contents']['riddle']
                answer = response['contents']['answer']
                return f"Riddle: {riddle}\nAnswer: {answer}"
            except Exception as e:
                return f"Error fetching riddle: {e}"
            
#########################################################################################################################################################
#########################################################################################################################################################









# Weather Suggestion

#########################################################################################################################################################

        # Function to provide weather-based suggestions
        def wheather_suggestion():
            API_KEY = 'Enter your own api key'  # OpenWeatherMap API key
            CITY = 'Mumbai'  # Default city for weather check

            # Function to get weather data from OpenWeatherMap API
            def get_weather(city):
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
                response = requests.get(url)
                data = response.json()
                if data["cod"] == 200:  # Check if the API call was successful
                    weather_description = data["weather"][0]["description"]  # Extract weather description
                    temperature = data["main"]["temp"]  # Extract temperature in Celsius
                    return weather_description, temperature
                else:
                    return None, None  # Return None if the API call fails

            # Function to suggest whether to go out or not based on weather conditions
            def suggest_weather(weather_description, temperature):
                if "rain" in weather_description.lower() or "storm" in weather_description.lower():
                    suggestion = "It's better to stay inside as it's raining or stormy."
                    sendmessage(suggestion)  # Send the suggestion via WhatsApp
                elif temperature < 0:  # Check for extremely cold weather
                    suggestion = "It's too cold outside. It's better to stay inside."
                    sendmessage(suggestion)
                elif temperature > 35:  # Check for extremely hot weather
                    suggestion = "It's too hot outside. It's better to stay inside."
                    sendmessage(suggestion)
                else:
                    suggestion = "The weather seems fine. You can go out."
                    sendmessage(suggestion)
                return suggestion

            # Main function to fetch weather data and provide suggestions
            def main():
                weather_description, temperature = get_weather(CITY)  # Fetch weather data
                if weather_description and temperature:
                    print(f"Weather in {CITY}: {weather_description} with a temperature of {temperature}°C.")
                    speak(f"Weather in {CITY}: {weather_description} with a temperature of {temperature}°C.")
                    suggestion = suggest_weather(weather_description, temperature)  # Get weather suggestion
                    print(suggestion)
                    speak(suggestion)
                else:
                    print("Could not retrieve weather data. Please check the city name or API key.")
                    speak("Could not retrieve weather data. Please check the city name or API key.")

            if __name__ == "__main__":
                main()  # Execute the main function

#########################################################################################################################################################
#########################################################################################################################################################











# Volume Control


#########################################################################################################################################################
#########################################################################################################################################################

        from pynput.keyboard import Key,Controller
        from time import sleep
        keyboard = Controller()

        def volumeup():
            for i in range(5):
                pyautogui.press("volumeup")
                pyautogui.release("volumeup")
                sleep(0.1)
        def volumedown():
            for i in range(5):
                pyautogui.press("volumedown")
                pyautogui.release("volumedown")
                sleep(0.1)

        def volumefull():
            for i in range(10):
                pyautogui.press("volumeup")
                pyautogui.release("volumeup")
                
                sleep(0.1)

        def volumemute():
            for i in range(5):
                pyautogui.press("volumemute")
                pyautogui.release("volumemute")
                sleep(0.1)

#########################################################################################################################################################
#########################################################################################################################################################










# Advice

#########################################################################################################################################################
#########################################################################################################################################################

        # Function to fetch random advice from an API
        def get_random_advice():
            # Sending a GET request to the advice API and parsing the JSON response
            res = requests.get("https://api.adviceslip.com/advice").json()
            # Extracting and returning the advice from the response
            return res['slip']['advice']

#########################################################################################################################################################
#########################################################################################################################################################









# Search on Google , Youtube, Whatsapp Message

#########################################################################################################################################################
#########################################################################################################################################################


        def search_on_google(command):
            kit.search(command)

        def play_on_youtube(video):
            kit.playonyt(video)

        def send_whatsapp_message(number, message):
            kit.sendwhatmsg_instantly(f"+91{number}", message)


#########################################################################################################################################################
#########################################################################################################################################################











# Change Background

#########################################################################################################################################################
#########################################################################################################################################################

        def changebackground():
            """
            Function to change the desktop background wallpaper.
            """
            # Use ctypes to call the Windows API for changing the wallpaper
            ctypes.windll.user32.SystemParametersInfoW(
            20,  # SPI_SETDESKWALLPAPER: Changes the desktop wallpaper
            0,   # Reserved, must be 0
            "Location of wallpaper",  # Path to the new wallpaper image
            0    # Update the user profile with the new wallpaper
            )
            # Notify the user that the background has been changed
            speak("Background changed successfully")
#########################################################################################################################################################
#########################################################################################################################################################








# Get Defination

#########################################################################################################################################################
#########################################################################################################################################################

        def get_definition(word):
            try:
                url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
                response = requests.get(url).json()
                if isinstance(response, list):
                    meanings = response[0]['meanings']
                    definition = meanings[0]['definitions'][0]['definition']
                    return f"Definition of {word}: {definition}"
                else:
                    return "Word not found in the dictionary."
            except Exception as e:
                return f"Error fetching definition: {e}"

#########################################################################################################################################################
#########################################################################################################################################################







# Word Gess Game

#########################################################################################################################################################
#########################################################################################################################################################

        def wordgessgame():
            words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board']
 
            # Function will choose one random
            # word from this list of words
            word = random.choice(words)
            
            
            print("Guess the characters")
            speak("Guess the characters")
            
            guesses = ''
            
            # any number of turns can be used here
            turns = 12
            
            
            while turns > 0:
            
                # counts the number of times a user fails
                failed = 0
            
                # all characters from the input
                # word taking one at a time.
                for char in word:
            
                    # comparing that character with
                    # the character in guesses
                    if char in guesses:
                        print(char, end=" ")
            
                    else:
                        print("_")
            
                        # for every failure 1 will be
                        # incremented in failure
                        failed += 1
            
                if failed == 0:
                    # user will win the game if failure is 0
                    # and 'You Win' will be given as output
                    print("You Win")
                    speak("You Win")
            
                    # this print the correct word
                    print("The word is: ", word)
                    speak(f"The word is {word}")
                    break
            
                # if user has input the wrong alphabet then
                # it will ask user to enter another alphabet
                print()
                guess = input("guess a character:")
            
                # every input character will be stored in guesses
                guesses += guess
            
                # check input with the character in word
                if guess not in word:
            
                    turns -= 1
            
                    # if the character doesn’t match the word
                    # then “Wrong” will be given as output
                    print("Wrong")
                    speak("Wrong")
            
                    # this will print the number of
                    # turns left for the user
                    print("You have", + turns, 'more guesses')
                    speak(f"You have {turns} more guesses")

                    if turns == 0:
                       print("You Loose")
                       speak("You Loose")

#########################################################################################################################################################
#########################################################################################################################################################











# Rock Paper Scissors

#########################################################################################################################################################
#########################################################################################################################################################

        def rockpaperscissors():
            print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
            + "Rock vs Paper -> Paper wins \n"
            + "Rock vs Scissors -> Rock wins \n"
            + "Paper vs Scissors -> Scissor wins \n")

            speak('Winning rules of the game ROCK PAPER SCISSORS are :\n'
            + "Rock vs Paper -> Paper wins \n"
            + "Rock vs Scissors -> Rock wins \n"
            + "Paper vs Scissors -> Scissor wins \n")

            while True:

                print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

                # take the input from user
                speak("Enter your choice , enter in number 1, 2 or 3")
                choice = int(input("Enter your choice : "))

                # OR is the short-circuit operator
                # if any one of the condition is true
                # then it return True value

                # looping until user enter invalid input
                while choice > 3 or choice < 1:
                    choice = int(input('Enter a valid choice please ☺'))
                    break

                    # initialize value of choice_name variable
                # corresponding to the choice value
                if choice == 1:
                    choice_name = 'Rock'
                elif choice == 2:
                    choice_name = 'Paper'
                else:
                    choice_name = 'Scissors'

                    # print user choice
                print('User choice is \n', choice_name)
                print('Now its Computers Turn....')
                speak('Now its Computers Turn....')
                time.sleep(2)

                # Computer chooses randomly any number
                # among 1 , 2 and 3. Using randint method
                # of random module
                comp_choice = random.randint(1, 3)

                # looping until comp_choice value
                # is equal to the choice value
                while comp_choice == choice:
                    comp_choice = random.randint(1, 3)

                # initialize value of comp_choice_name
                # variable corresponding to the choice value
                if comp_choice == 1:
                    comp_choice_name = 'RocK'
                elif comp_choice == 2:
                    comp_choice_name = 'Paper'
                else:
                    comp_choice_name = 'Scissors'
                print("Computer choice is \n", comp_choice_name)
                speak(f"Computer choice is {comp_choice_name}")
                print(choice_name, 'Vs', comp_choice_name)
                speak(f"{choice_name} Vs {comp_choice_name}")
                time.sleep(2)
                # we need to check of a draw
                if choice == comp_choice:
                    print('Its a Draw', end="")
                    speak('Its a Draw')
                    result = "DRAW"
                # condition for winning
                if (choice == 1 and comp_choice == 2):
                    print('paper wins =>', end="")
                    speak('paper wins')
                    result = 'Paper'
                elif (choice == 2 and comp_choice == 1):
                    print('paper wins =>', end="")
                    speak('paper wins')
                    result = 'Paper'

                if (choice == 1 and comp_choice == 3):
                    print('Rock wins =>\n', end="")
                    speak('Rock wins')
                    result = 'Rock'
                elif (choice == 3 and comp_choice == 1):
                    print('Rock wins =>\n', end="")
                    speak('Rock wins')
                    result = 'RocK'

                if (choice == 2 and comp_choice == 3):
                    print('Scissors wins =>', end="")
                    speak('Scissors wins')
                    result = 'Scissors'
                elif (choice == 3 and comp_choice == 2):
                    print('Scissors wins =>', end="")
                    result = 'Rock'
                # Printing either user or computer wins or draw
                if result == 'DRAW':
                    print("<== Its a tie ==>")
                    speak("Its a tie")
                if result == choice_name:
                    print("<== You wins ==>")
                    speak("You win")
                else:
                    print("<== Computer wins ==>")
                    speak("Computer wins")
                ans= input(("Do you want to play again? (Y/N): ")).lower()
                # if user input n or N then condition is True
                if ans == 'n':
                    break
                elif ans == 'no':
                    break
                elif ans == 'No':
                    break
                if ans == 'N':
                    break
            # after coming out of the while loop
            # we print thanks for playing
            print("thanks for playing")
            speak("thanks for playing")

#########################################################################################################################################################
#########################################################################################################################################################






# Play Tic Tac Toe

#########################################################################################################################################################
#########################################################################################################################################################

        def playtictactoe():
            def print_board(board):
                for row in board:
                    print(" | ".join(row))
                    print("-" * 9)

            def check_win(board, player):
                # Check rows
                for row in board:
                    if all(cell == player for cell in row):
                        return True

                # Check columns
                for col in range(3):
                    if all(board[row][col] == player for row in range(3)):
                        return True

                # Check diagonals
                if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
                    return True

                return False

            def is_board_full(board):
                for row in board:
                    for cell in row:
                        if cell == ' ':
                            return False
                return True

            def tic_tac_toe():
                print("Welcome to Tic-Tac-Toe!")
                speak("Welcome to Tic-Tac-Toe!")
                print("Player 1 will be 'X', and Player 2 will be 'O'.")
                speak("Player 1 will be 'X', and Player 2 will be 'O'.")
                board = [[' ' for _ in range(3)] for _ in range(3)]
                current_player = 'X'
                
                while True:
                    print_board(board)
                    row = int(input(f"Player '{current_player}', enter the row (1-3): ")) - 1
                    col = int(input(f"Player '{current_player}', enter the column (1-3): ")) - 1
                    
                    if board[row][col] == ' ':
                        board[row][col] = current_player
                    else:
                        print("That cell is already taken. Try again.")
                        speak("That cell is already taken. Try again.")
                        continue
                    
                    if check_win(board, current_player):
                        print_board(board)
                        print(f"Player '{current_player}' wins! Congratulations!")
                        speak(f"Player '{current_player}' wins! Congratulations!")
                        break
                    elif is_board_full(board):
                        print_board(board)
                        print("It's a tie! No more spaces left.")
                        speak("It's a tie! No more spaces left.")
                        break
                    
                    current_player = 'O' if current_player == 'X' else 'X'
                
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again == "yes":
                    tic_tac_toe()
                else:
                    print("Thank you for playing Tic-Tac-Toe!")
                    speak("Thank you for playing Tic-Tac-Toe!")

            # Start the game
            tic_tac_toe()

#########################################################################################################################################################
#########################################################################################################################################################










# Facts

#########################################################################################################################################################
#########################################################################################################################################################

        def get_random_fact():
            try:
                response = requests.get("https://useless-facts.sameerkumar.website/api").json()
                fact = response['data']
                return f"Random fact: {fact}"
            except Exception as e:
                return f"Error fetching random fact: {e}"

#########################################################################################################################################################
#########################################################################################################################################################










# Timer

#########################################################################################################################################################
#########################################################################################################################################################
        
        
        def timer():
            def jarvis_timer(minutes):
                # Convert minutes to seconds
                delay_in_seconds = minutes * 60

                # Define the function to play the alarm sound
                def play_alarm():
                    print("Jarvis: Sir, time’s up!")
                    winsound.Beep(1000, 1000)  # frequency=1000 Hz, duration=1000 ms

                # Start the timer
                threading.Timer(delay_in_seconds, play_alarm).start()
                print(f"Timer is set for {minutes} minutes.")

            # Example usage
            minutes = int(input("Enter timer in minutes: "))
            jarvis_timer(minutes)
                
#########################################################################################################################################################
#########################################################################################################################################################








# Alarm

#########################################################################################################################################################
#########################################################################################################################################################


        def alarm():

            def set_alarm(alarm_time):
                # Get current time
                now = datetime.datetime.now()
                
                # Calculate the time difference in seconds
                time_difference = (alarm_time - now).total_seconds()
                
                # If the alarm time is in the past, add a day to set it for the next day
                if time_difference < 0:
                    alarm_time += datetime.timedelta(days=1)
                    time_difference = (alarm_time - now).total_seconds()
                
                # Set up the alarm
                threading.Timer(time_difference, play_alarm).start()
                print(f"Alarm is set for {alarm_time.strftime('%I:%M %p')}")

            def play_alarm():
                # Sound alarm with winsound.Beep
                print("Alarm ringing!")
                winsound.Beep(1000, 1000)  # frequency=1000 Hz, duration=1000 ms

            # Input target time (e.g., 1:30 AM)
            alarm_time_str = input("Enter alarm time (e.g., '1:30 AM'): ")

            # Convert input time to a datetime object
            alarm_time = datetime.datetime.strptime(alarm_time_str, "%I:%M %p")
            now = datetime.datetime.now()

            # Adjust alarm_time to today's date
            alarm_time = alarm_time.replace(year=now.year, month=now.month, day=now.day)

            # Set the alarm
            set_alarm(alarm_time)

#########################################################################################################################################################
#########################################################################################################################################################









# FLight 

#########################################################################################################################################################
#########################################################################################################################################################


        def check_flight_status( flight_number):
            try:
                api_key = "Enter Your Api Key" # https://aviationstack.com/signup/free visit here for api key
                url = f"http://aviation-edge.com/v2/public/flights?key={api_key}&flight_iata={flight_number}"
                response = requests.get(url).json()
                status = response[0]['status']
                departure = response[0]['departure']['airport']
                arrival = response[0]['arrival']['airport']
                return f"Flight {flight_number} status: {status}, Departure: {departure}, Arrival: {arrival}"
            except Exception as e:
                return f"Error checking flight status: {e}"

#########################################################################################################################################################
#########################################################################################################################################################







# Track Phone 


#########################################################################################################################################################
#########################################################################################################################################################

        #enter phone number along with country code
        #Example:+91 8897909599
        def trackphone():
            speak("Enter phone number with country code")
            number = input("Enter phone number with country code : ")
            
            # Parsing String to the Phone number
            phoneNumber = phonenumbers.parse(number)
            
            # printing the timezone using the timezone module
            timeZone = timezone.time_zones_for_number(phoneNumber)
            print("timezone : "+str(timeZone))
            
            # printing the geolocation of the given number using the geocoder module
            geolocation = geocoder.description_for_number(phoneNumber,"en")
            print("location : "+geolocation)
            
            # printing the service provider name using the carrier module
            service = carrier.name_for_number(phoneNumber,"en")
            print("service provider : "+service)

#########################################################################################################################################################
#########################################################################################################################################################












# Contacts info

#########################################################################################################################################################
#########################################################################################################################################################

        def AddContact():
            speak(f'sir, Enter the contact details')
            name = input("Enter the name :").lower()
            number = input("Enter the number :")
            NumberFormat = f'"{name}":"+91{number}"'
            ContFile = open("Contacts.txt", "a") 
            # Adding to the Data Base
            ContFile.write(f"{NumberFormat}\n")
            ContFile.close()
            speak(f'sir, Contact Saved Successfully')



        #Search Contact
        def SearchCont(name):
            with open("Contacts.txt","r") as ContactsFile:
                for line in ContactsFile:
                    # Now Matching for the name in each line
                    if name in line:
                        print("Name Match Found")
                        s = line.split("\"")
                        return s[1],s[3],True
            return 0,0,False
        



        #Display all contacts
        def Display():
            # Calling for Data
            ContactsFile = open("Contacts.txt","r")
            count=0
            for line in ContactsFile:
                count+=1
            ContactsFile.close()
            ContactsFile = open("Contacts.txt","r")
            speak(f"sir displaying the {count} contacts stored in our data base")    
            for line in ContactsFile:
                s = line.split("\"")
                print("Name: "+s[1])
                print("Number: "+s[3])
            ContactsFile.close()







        #search contact
        def NameIntheContDataBase(command):
            line = command
            # Spliting the number inside contact Database in Array
            line = line.split("number in contacts")[0]
            if("tell me" in line):
                name = line.split("tell me")[1]
                name = name.strip()
            else:
                name= line.strip()
            name,number,bo = SearchCont(name)
            # Matching The contact form Database
            if bo:
                print(f"Contact Match Found in our data base with {name} and the mboile number is {number}")
                speak(f"sir Contact Match Found in our data base with {name} and the mboile number is {number}")
            else:
                # if not found asking to add it or no
                speak("sir the name not found in our data base, shall I add the contact")
                AddOrNot = takeCommand()
                print(AddOrNot)
                if ("yes add it" in AddOrNot)or ("yeah" in AddOrNot) or ("yah" in AddOrNot):
                    AddContact()
                    speak(f'sir, Contact Saved Successfully')
                elif("no" in AddOrNot) or ("don't add" in AddOrNot):
                    speak('Ok sir')

#########################################################################################################################################################
#########################################################################################################################################################











# Generating Password

#########################################################################################################################################################
#########################################################################################################################################################

        def passward():
            import random 
            import array 

            # maximum length of password needed 
            # this can be changed to suit your password length 
            MAX_LEN = 12

            # declare arrays of the character that we need in out password 
            # Represented as chars to enable easy string concatenation 
            DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
            LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                                'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                                'z'] 

            UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                                'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
                                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                                'Z'] 

            SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
                    '*', '(', ')', '<'] 

            # combines all the character arrays above to form one array 
            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 

            # randomly select at least one character from each character set above 
            rand_digit = random.choice(DIGITS) 
            rand_upper = random.choice(UPCASE_CHARACTERS) 
            rand_lower = random.choice(LOCASE_CHARACTERS) 
            rand_symbol = random.choice(SYMBOLS) 

            # combine the character randomly selected above 
            # at this stage, the password contains only 4 characters but 
            # we want a 12-character password 
            temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 


            # now that we are sure we have at least one character from each 
            # set of characters, we fill the rest of 
            # the password length by selecting randomly from the combined 
            # list of character above. 
            for x in range(MAX_LEN - 4): 
                temp_pass = temp_pass + random.choice(COMBINED_LIST) 

                # convert temporary password into array and shuffle to 
                # prevent it from having a consistent pattern 
                # where the beginning of the password is predictable 
                temp_pass_list = array.array('u', temp_pass) 
                random.shuffle(temp_pass_list) 

            # traverse the temporary password array and append the chars 
            # to form the password 
            password = "" 
            for x in temp_pass_list: 
                    password = password + x 
                    
            # print out password 
            print(password) 
            speak(password)
 
#########################################################################################################################################################            
#########################################################################################################################################################
     






#########################################################################################################################################################            
#########################################################################################################################################################
        def create_document():

            # Create a new Document object
            doc = Document()

            speak("Sir what should be the file name")

            a = takeCommand()

            # Specify the location where you want to save the file
            file_path = f'path to\your file\Python\Word_file_Jarvis\{a}.docx'

            # Save the blank document to the specified location
            doc.save(file_path)

            print(f'Word file created at {file_path}')

#########################################################################################################################################################
#########################################################################################################################################################










# Getting the current Location

#########################################################################################################################################################
#########################################################################################################################################################

        def locaiton():
            speak("Wait sir, let me check")
            try:
                IP_Address = get('https://api.ipify.org').text
                print(IP_Address)
                url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
                print(url)
                geo_reqeust = get(url)
                geo_data = geo_reqeust.json()
                city = geo_data['city']
                state = geo_data['region']
                country = geo_data['country']
                tZ = geo_data['timezone']
                longitude = geo_data['longitude']
                latidute = geo_data['latitude']
                org = geo_data['organization_name']
                print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
                speak(f"sir i am not sure, but i think we are in {city} city of {state} state of {country} country")
                speak(f"and sir, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
            except Exception as e:
                speak("Sorry sir, due to network issue i am not able to find where we are.")
                pass

#########################################################################################################################################################
#########################################################################################################################################################












# IP Address

#########################################################################################################################################################
#########################################################################################################################################################

        {
  "ip": "117.214.111.199"
}
        def find_my_ip():
            ip_address = requests.get('https://api64.ipify.org?format=json').json() # Requesting IP address from JSON
            return ip_address["ip"]

#########################################################################################################################################################
#########################################################################################################################################################








# Software Control


#########################################################################################################################################################
#########################################################################################################################################################
        
        def close_notepad():
            from os import system
            system("taskkill/f /im Notepad++.exe")

        def close_chrome():
            from os import system
            system("taskkill/f /im chrome.exe")

        def close_cmd():
            from os import system
            system("taskkill/f /im cmd")

        def close_discord():
            from os import system
            system("taskkill/f /im discord.exe")

        def close_calculator():
            from os import system
            system("taskkill/f /im calc.exe")

#########################################################################################################################################################
#########################################################################################################################################################









# Wikipedia Search

#########################################################################################################################################################
#########################################################################################################################################################

        def search_on_wikipedia(command):
            results = wikipedia.summary(command, sentences=2)
            return results
        
#########################################################################################################################################################
#########################################################################################################################################################






# Internet Speed

#########################################################################################################################################################
#########################################################################################################################################################

        def InternetSpeed():
            speak("Wait a few seconds sir, checking your internet speed")
            
            try:
                st = speedtest.Speedtest()
                st.get_best_server()  # Ensure it selects the best server

                dl = st.download() / 1_000_000  # Convert to Mbps
                up = st.upload() / 1_000_000    # Convert to Mbps

                print(f"Download Speed: {dl:.2f} Mbps | Upload Speed: {up:.2f} Mbps")
                speak(f"Sir, we have {dl:.2f} megabytes per second downloading speed and {up:.2f} megabytes per second uploading speed")
            
            except speedtest.ConfigRetrievalError:
                print("Error: Could not retrieve speedtest configuration. Check your internet connection or try again later.")
                speak("Sir, I am unable to check the internet speed due to a connection issue.")
            
            except Exception as e:
                print(f"Unexpected error: {e}")
                speak("Sir, something went wrong while checking the internet speed.")

#########################################################################################################################################################
#########################################################################################################################################################









# Calculate Day & Shedule 

#########################################################################################################################################################
#########################################################################################################################################################

        def Cal_day():
            day = datetime.datetime.today().weekday() + 1
            Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
            
            return day_of_the_week

        #shedule function for remembering todays plans
        #NOTE For example I have declared my timetable you can declare anything you want
    
    
        def shedule():
            day = Cal_day().lower()
            speak("sir today's shedule is")
            Week = {"monday" : "sir from 9:00 to 9:50 you have Cultural class, from 10:00 to 11:50 you have mechanics class, from 12:00 to 2:00 you have brake, and today you have sensors lab from 2:00",
            "tuesday" : "sir from 9:00 to 9:50 you have English class, from 10:00 to 10:50 you have break,from 11:00 to 12:50 you have ELectrical class, from 1:00 to 2:00 you have brake, and today you have biology lab from 2:00",
            "wednesday" : "sir today you have a full day of classes from 9:00 to 10:50 you have Data structures class, from 11:00 to 11:50 you have mechanics class, from 12:00 to 12:50 you have cultural class, from 1:00 to 2:00 you have brake, and today you have Data structures lab from 2:00",
            "thrusday" : "sir today you have a full day of classes from 9:00 to 10:50 you have Maths class, from 11:00 to 12:50 you have sensors class, from 1:00 to 2:00 you have brake, and today you have english lab from 2:00",
            "friday" : "sir today you have a full day of classes from 9:00 to 9:50 you have Biology class, from 10:00 to 10:50 you have data structures class, from 11:00 to 12:50 you have Elements of computing class, from 1:00 to 2:00 you have brake, and today you have Electronics lab from 2:00",
            "saturday" : "sir today you have a full day of classes from 9:00 to 11:50 you have maths lab, from 12:00 to 12:50 you have english class, from 1:00 to 2:00 you have brake, and today you have elements of computing lab from 2:00",
            "sunday":"sir today is holiday but we can't say anything when they will bomb with any assisgnments"}
            if day in Week.keys():
                speak(Week[day])

#########################################################################################################################################################
#########################################################################################################################################################








# Temperature

#########################################################################################################################################################
#########################################################################################################################################################

        def temperature():
            try:
                # Get Public IP
                IP_Address = get('https://api.ipify.org').text

                # Get Geolocation Data
                url = f'https://get.geojs.io/v1/ip/geo/{IP_Address}.json'
                geo_request = get(url)
                geo_data = geo_request.json()

                # Extract City Name
                city = geo_data.get('city', 'Unknown Location')  

                if city == 'Unknown Location':
                    speak("Sorry, I couldn't determine your location.")
                    return

                # Search Temperature on Google
                search = f"temperature in {city}"
                url_1 = f"https://www.google.com/search?q={search}"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
                }
                r = get(url_1, headers=headers)  # Add headers to avoid being blocked
                data = BeautifulSoup(r.text, "html.parser")

                # Extract Temperature (Using more specific class)
                temp_element = data.find("div", class_="BNeawe iBp4i AP7Wnd")

                if temp_element:
                    temp = temp_element.text
                    speak(f"Current temperature in {city} is {temp}")
                    print(f"Current temperature in {city} is {temp}")
                else:
                    speak("Sorry, I couldn't fetch the temperature.")
                    print("Temperature data not found on the page.")

            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, I encountered an error while fetching the temperature.")


#########################################################################################################################################################
#########################################################################################################################################################











# News Function

#########################################################################################################################################################
#########################################################################################################################################################


        
        NEWS_API_KEY =("Enter your own News Api")
        def get_latest_news():
            news = GoogleNews()
            news.search("technology")  # Change the keyword for different topics
            results = news.result()
            speak(f"I'm reading out the latest news headlines, sir")

            main_heads_list = []

            for i, article in enumerate(results[:5], start=1):
                main_heads_list.append(f"{i}. {article['title']}")

            # Print all headlines
            print("\n".join(main_heads_list))

            # Speak all headlines
            speak("\n".join(main_heads_list))



#########################################################################################################################################################
#########################################################################################################################################################








# Typing Speed

#########################################################################################################################################################
#########################################################################################################################################################

        def ty_speed_test():
            # List of sentences for the typing test
            sentences = [
                "The quick brown fox jumps over the lazy dog.",
                "Pack my box with five dozen liquor jugs.",
                "How razorback-jumping frogs can level six piqued gymnasts!",
                "Crazy Fredrick bought many very exquisite opal jewels.",
                "We promptly judged antique ivory buckles for the next prize."
            ]

            # Function to calculate typing speed
            def typing_speed_test():
                sentence = random.choice(sentences)
                speak("Ok in 5 seconds a line will appear infront of you as it appears start typing")
                for i in range(1,6):
                    speak(i)
                    time.sleep(1)
                print("\nType the following sentence:\n")
                print(sentence)
                print()

                start_time = time.time()
                user_input = input()
                end_time = time.time()

                time_taken = end_time - start_time
                words_per_minute = (len(user_input.split()) / time_taken) * 60

                print("\nResults:")
                print(f"Time taken: {time_taken:.2f} seconds")
                print(f"Your typing speed is: {words_per_minute:.2f} words per minute")
                speak(f"Your typing speed is: {words_per_minute:.2f} words per minute")

                # Calculate accuracy
                accuracy = sum(1 for a, b in zip(sentence, user_input) if a == b) / len(sentence) * 100
                print(f"Accuracy: {accuracy:.2f}%")

            typing_speed_test()


#########################################################################################################################################################
#########################################################################################################################################################









# Morse Code

#########################################################################################################################################################
#########################################################################################################################################################

        def encode_morse_code():

        # Morse code dictionary
            MORSE_CODE_DICT = {
                'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
                '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
            }

            def text_to_morse_code(text):
                morse_code = ''
                for char in text.upper():
                    if char in MORSE_CODE_DICT:
                        morse_code += MORSE_CODE_DICT[char] + ' '
                    else:
                        morse_code += ' '  # For unrecognized characters, add a space
                return morse_code.strip()

            # Example usage
            if __name__ == "__main__":
                speak("Enter text to convert to Morse code")
                input_text = input("Enter text to convert to Morse code: ")
                morse_code = text_to_morse_code(input_text)
                print("Morse Code:", morse_code)








        def decode_morse_code():

            # Morse code dictionary for decoding
            MORSE_CODE_DICT = {
                '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
                '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
                '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
                '----.': '9', '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?',
                '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '/': ' '
            }

            def morse_code_to_text(morse_code):
                words = morse_code.split(' / ')
                decoded_text = ''
                for word in words:
                    for code in word.split():
                        if code in MORSE_CODE_DICT:
                            decoded_text += MORSE_CODE_DICT[code]
                        else:
                            decoded_text += '?'  # For unrecognized codes, add a question mark
                    decoded_text += ' '
                return decoded_text.strip()

            # Example usage
            if __name__ == "__main__":
                speak("Enter Morse code to convert to text")
                input_morse_code = input("Enter Morse code to convert to text: ")
                text = morse_code_to_text(input_morse_code)
                print("Text:", text)




#########################################################################################################################################################
#########################################################################################################################################################








# ASCII ART

#########################################################################################################################################################
#########################################################################################################################################################

            

        # Define the ASCII characters for grayscale levels
        ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

        def resize_image(image, new_width=100):
            width, height = image.size
            ratio = height / width / 1.65  # Adjust ratio for non-square pixels
            new_height = int(new_width * ratio)
            resized_image = image.resize((new_width, new_height))
            return resized_image

        def grayscale_image(image):
            return image.convert("L")

        def map_pixels_to_ascii(image, range_width=25):
            pixels = list(image.getdata())
            ascii_str = "".join([ASCII_CHARS[pixel // range_width] for pixel in pixels])
            return ascii_str

        def generate_ascii_art(image_path, new_width=100):
            image = Image.open(image_path)
            image = resize_image(image, new_width)
            image = grayscale_image(image)

            ascii_str = map_pixels_to_ascii(image)
            img_width = image.width
            ascii_art = "\n".join([ascii_str[index:index + img_width] for index in range(0, len(ascii_str), img_width)])

            return ascii_art

#########################################################################################################################################################
#########################################################################################################################################################









# QR Code 

#########################################################################################################################################################
#########################################################################################################################################################


        def create_qr_code():
                speak("sir please enter url")
                # String which represents the QR code 
                source = input("Enter Url: ")

                # Generate QR code 
                url = pyqrcode.create(source) 

                speak("Sir by which name you have to save it , sir")

                name = takeCommand()

                # Create and save the svg file naming "myqr.svg" 
                url.svg(f"your file path\Python\Jarvis\Qr_codes\{name}.svg", scale = 8) 

                # Create and save the png file naming "myqr.png" 
                url.png(f'your file path\Python\Jarvis\Qr_codes\{name}.png', scale = 6) 

                speak("sir successfully it is saved")

#########################################################################################################################################################
#########################################################################################################################################################









# Bar Code

#########################################################################################################################################################
#########################################################################################################################################################

        def generate_barcode():
            # Make sure to pass the number as string 
            number = int(input("Enter 12 digits Number:"))
            # Now, let's create an object of EAN13 
            # class and pass the number 
            my_code = EAN13(number)
            speak("sir what name you want it to be saved") 

            name = takeCommand()
            # Our barcode is ready. Let's save it. 

            my_code.save(f"your file path\Python\Jarvis\Barcode\{name}")

#########################################################################################################################################################
#########################################################################################################################################################













# Mail Function

#########################################################################################################################################################
#########################################################################################################################################################

        def send_mail(reciever_address,subject,body):

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Use SSL instead of TLS
            server.login('yash.innovater@gmail.com', 'avfz zdep ckog wxjv')

            message = f"Subject: {subject}\n\n{body}"

            server.sendmail("yash.innovater@gmail.com", reciever_address, message)
            print("Mail sent successfully!")

            server.quit()

#########################################################################################################################################################
#########################################################################################################################################################






#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################

#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################

#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################

#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################





# Exiting

#########################################################################################################################################################



# Sleep Function

        if "jarvis sleep" in command.lower():
            speak("ok Sir going to sleep")

            while True:
               command=takeCommand()
               if "wake up jarvis" in command.lower():
                   speak("i am back sir")
                   break
               if "wake up" in command.lower():
                   speak("i am back sir")
                   break
               if "get up" in command.lower():
                   speak("i am back sir")
                   break
               
        elif "you can go to sleep" in command.lower():
            speak("ok Sir going to sleep")

            while True:
               command=takeCommand()
               if "wake up jarvis" in command.lower():
                   speak("i am back sir")
                   break
               if "wake up" in command.lower():
                   speak("i am back sir")
                   break
               if "get up" in command.lower():
                   speak("i am back sir")
                   break

                



               
        elif "you sleep" in command.lower():
            speak("ok Sir going to sleep")

            while True:
               command=takeCommand()
               if "wake up jarvis" in command.lower():
                   speak("i am back sir")
                   break
               if "wake up" in command.lower():
                   speak("i am back sir")
                   break

               if "get up" in command.lower():
                   speak("i am back sir")
                   break



               
        elif "sleep jarvis" in command.lower():
            speak("ok Sir going to sleep")

            while True:
               command=takeCommand()
               if "wake up jarvis" in command.lower():
                   speak("i am back sir")
                   break
               if "wake up" in command.lower():
                   speak("i am back sir")
                   break

               if "get up" in command.lower():
                   speak("i am back sir")
                   break

        elif "sleep" in command.lower():
            speak("ok Sir going to sleep")

            while True:
               command=takeCommand()
               if "wake up jarvis" in command.lower():
                   speak("i am back sir")
                   break
               if "wake up" in command.lower():
                   speak("i am back sir")
                   break
               if "get up" in command.lower():
                   speak("i am back sir")
                   break



# Exiting Function

        elif 'exit' in command:
            speak("ok sir you can call me any time for your help")
            stop_thread = True      
            sys.exit()

            
        elif 'stop' in command:
            speak("ok sir you can call me any time for your help")
            stop_thread = True
            sys.exit()

        elif 'bye' in command:
            speak("ok sir you can call me any time for your help")
            stop_thread = True
            sys.exit()

#########################################################################################################################################################









# ascii art

#########################################################################################################################################################

        elif "ascii art" in command:
            speak("sir please enter image path")
            image_path = input("Enter Image path: ")  # Replace with your image file path
            ascii_art = generate_ascii_art(image_path)
            print(ascii_art)

#########################################################################################################################################################






# Type Speed Test

#########################################################################################################################################################

        elif "type speed test" in command:
            ty_speed_test()

        elif "typing speed test" in command:
            ty_speed_test()

        elif "typ speeding test" in command:
            ty_speed_test()

#########################################################################################################################################################









# Current_window

#########################################################################################################################################################
        elif "i am on which window" in command:
            get_active_window_title()

        elif "i am in which window" in command:
            get_active_window_title()

        elif "this on which window" in command:
            get_active_window_title()

        elif "which window" in command:
            get_active_window_title()
#########################################################################################################################################################










# Morse Code

#########################################################################################################################################################
        elif "convert to morse code" in command:
            encode_morse_code()

        elif "convert text to morse code" in command:
            encode_morse_code()

        elif "encode morse code" in command:
            encode_morse_code()





        elif "convert morse code to text" in command:
            decode_morse_code()

        elif "decode morse code" in command:
            decode_morse_code()
#########################################################################################################################################################









# QR code generate

#########################################################################################################################################################
        elif 'create QR'in command:
            create_qr_code()

        elif 'generate QR'in command:
            create_qr_code()
#########################################################################################################################################################









# Bar code

#########################################################################################################################################################
        elif 'bar code'in command:
            generate_barcode()
#########################################################################################################################################################









# Battery Functions

#########################################################################################################################################################

        elif 'how much power left' in command:
            battery= psutil.sensors_battery()
            persentage = battery.percent
            speak(f"sir our system have {persentage} percent battery")

        elif 'how much power we have' in command:
            battery= psutil.sensors_battery()
            persentage = battery.percent
            speak(f"sir our system have {persentage} percent battery")

        elif 'current battery' in command:
            battery= psutil.sensors_battery()
            persentage = battery.percent
            speak(f"sir our system have {persentage} percent battery")


#########################################################################################################################################################








# Waiting Functions

#########################################################################################################################################################


        elif 'wait for one minute' in command:
            time.sleep(60)

        elif 'wait for two minute' in command:
            time.sleep(2*60) 

        elif 'wait for three minute' in command:
            time.sleep(3*60)

        elif 'wait for four minute' in command:
            time.sleep(4*60)       

        elif 'wait for five minute' in command:
            time.sleep(5*60) 
            
        elif 'wait for six minute' in command:
            time.sleep(6*60) 
            
        elif 'wait for seven minute' in command:
            time.sleep(7*60) 
            
        elif 'wait for eight minute' in command:
            time.sleep(8*60)

        elif 'wait for nine minute' in command:
            time.sleep(9*60) 

        elif 'wait for ten minute' in command:
            time.sleep(10*60)	

        elif 'wait' in command:
            time.sleep(60)

#########################################################################################################################################################








# Key Control

#########################################################################################################################################################

# Shortcut Keys

        elif 'switch screen'in command:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')

        elif 'home screen'in command:
            pyautogui.keyDown('win')
            pyautogui.press('d')
            pyautogui.keyUp('win')


# Keys Settings

        elif 'right'in command:
            pyautogui.press('right')

        elif 'left'in command:
            pyautogui.press('left')

        elif 'up'in command:
            pyautogui.press('up')

        elif 'down'in command:
            pyautogui.press('down')

        elif 'enter'in command:
            pyautogui.press('enter')

        elif 'backspace'in command:
            pyautogui.press('backspace')

        elif 'page down'in command:
            pyautogui.press('pgdn')

        elif 'page up'in command:
            pyautogui.press('pgup')



# Browser Mode


        elif 'incognito mode'in command:
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('shift')
            pyautogui.press('n')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('shift')





# Clipboard settings


        elif 'copy it'in command:
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')

        elif 'paste it'in command:
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')

        elif 'select all'in command:
            pyautogui.keyDown('ctrl')
            pyautogui.press('a')
            pyautogui.keyUp('ctrl')





# Repository controls


        elif 'history'in command:
            pyautogui.keyDown('ctrl')
            pyautogui.press('h')
            pyautogui.keyUp('ctrl')

        elif 'downloads'in command:
            pyautogui.keyDown('ctrl')
            pyautogui.press('j')
            pyautogui.keyUp('ctrl')





# seettings part for Browser

        elif 'chrome settings'in command:
            pyautogui.keyDown('ctrl')
            pyautogui.press(',')
            pyautogui.keyUp('ctrl')

        elif 'browser settings'in command:
            pyautogui.keyDown('ctrl')
            pyautogui.press(',')
            pyautogui.keyUp('ctrl')

        elif 'browser settings'in command:
            pyautogui.keyDown('ctrl')
            pyautogui.press('p')
            pyautogui.keyUp('ctrl')




# Tab control for Chrome


        elif 'reopen closed tab'in command:
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('shift')
            pyautogui.press('t')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('shift')

        elif 'next tab'in command:
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('tab')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('tab')

        elif 'previous tab'in command:
            pyautogui.keyDown('shift')
            pyautogui.keyDown('alt')
            pyautogui.keyDown('tab')
            pyautogui.keyUp('alt')
            pyautogui.keyUp('tab')
            pyautogui.keyUp('shift')



#########################################################################################################################################################









#########################################################################################################################################################

        elif "create a blank document" in command or "create a document" in command:
            create_document()

#########################################################################################################################################################







# Wheather Suggestion

#########################################################################################################################################################

        elif "i am going out suggest me the wheather" in command or "I am going out" in command:
            wheather_suggestion()

        elif "should I go out" in command or "can I going out" in command:
            wheather_suggestion()

#########################################################################################################################################################










# Install python module

#########################################################################################################################################################

        elif "install Python module" in command:
            speak("Sir please enter the name of the module")
            modu=input("Enter name of Module: ")
            os.system(f"pip install {modu}")
            speak(f"done sir module {modu} is installed")

        elif "install Python library" in command:
            speak("Sir please enter the name of the module")
            modu=input("Enter name of Module: ")
            os.system(f"pip install {modu}")
            speak(f"done sir module {modu} is installed")

#########################################################################################################################################################








# Timer

#########################################################################################################################################################

        elif "set timer" in command or "timer" in command:
            timer()

#########################################################################################################################################################









# Alarm

#########################################################################################################################################################

        elif "set alarm" in command:
            speak("Sir please set time")
            alarm()

        elif "set an alarm" in command:
            speak("Sir please set time")
            alarm()

#########################################################################################################################################################







# internet speed

#########################################################################################################################################################

        elif "internet speed" in command:
            InternetSpeed()

        elif "check internet speed" in command:
            InternetSpeed()

#########################################################################################################################################################







# Type Function

#########################################################################################################################################################

        elif "type" in command:
            command = command.replace("type","")
            command = command.replace("jarvis type","")
            pyautogui.write(command ,interval=0.1)

#########################################################################################################################################################








# Volume Control

#########################################################################################################################################################

        elif "volume up" in command:
            speak("Turning volume up,sir")
            volumeup()


        elif "volume down" in command:
            speak("Turning volume down, sir")
            volumedown()





        elif "full volume" in command:
            speak("Turning volume full,sir")
            volumeup()

        elif "volume full" in command:
            speak("Turning volume full,sir")
            volumeup()

        elif "volume at the peak" in command:
            speak("Turning volume full,sir")
            volumeup()




        elif "mute" in command:
            speak("muted")
            volumemute()	

#########################################################################################################################################################























# window close

#########################################################################################################################################################

        elif "close the window" in command:
            active_window = gw.getActiveWindow()
            if active_window !="":
                print(f"closing window: {active_window.title}")
                speak(f"closing window: {active_window.title}")
                pyautogui.hotkey("alt","f4")

            if active_window =="":
                speak(f"you are on the desktop")
                
            



        elif "close window" in command:
            active_window = gw.getActiveWindow()
            if active_window !="":
                print(f"closing window: {active_window.title}")
                speak(f"closing window: {active_window.title}")
                pyautogui.hotkey("alt","f4")

            if active_window =="":
                speak(f"you are on the desktop")




        elif "close the screen" in command:
            active_window = gw.getActiveWindow()
            if active_window !="":
                print(f"closing window: {active_window.title}")
                speak(f"closing window: {active_window.title}")
                pyautogui.hotkey("alt","f4")

            if active_window =="":
                speak(f"you are on the desktop")




        elif "close screen" in command:
            active_window = gw.getActiveWindow()
            if active_window !="":
                print(f"closing window: {active_window.title}")
                speak(f"closing window: {active_window.title}")
                pyautogui.hotkey("alt","f4")

            if active_window =="":
                speak(f"you are on the desktop")

#########################################################################################################################################################













# Video Controls

#########################################################################################################################################################

        elif "pause" in command:
            pyautogui.press("k")
            speak("video paused")

        elif "resume" in command:
            pyautogui.press("k")
            speak("video played")

        elif "mute" in command:
            pyautogui.press("m")
            speak("video muted")

#########################################################################################################################################################







# Scrolling

#########################################################################################################################################################

        elif "scroll up" in command:
            speak("Scrolling....")
            pyautogui.scroll(500)
            

        elif "scroll down" in command:
            speak("Scrolling....")
            pyautogui.scroll(-500)


#########################################################################################################################################################











# Size control

#########################################################################################################################################################

        elif "minimize" in command:
            speak("Minimizing")
            pyautogui.down(["win","down"])
            pyautogui.up(["win","down"])

            

        elif "mazimize" in command:
            speak("maximizing....")
            pyautogui.down(["win","up"])
            pyautogui.up(["win","up"])


#########################################################################################################################################################











# Bookmark page

#########################################################################################################################################################

        elif "save as bookmark" in command:
            speak("saving the page as bookmark")
            pyautogui.down(["ctrl","d"])
            pyautogui.up(["ctrl","d"])

        elif "bookmark it" in command:
            speak("saving the page as bookmark")
            pyautogui.down(["ctrl","d"])
            pyautogui.up(["ctrl","d"])

            

        elif "save the page" in command:
            speak("saving the page as bookmark")
            pyautogui.down(["ctrl","d"])
            pyautogui.up(["ctrl","d"])

        elif "save page" in command:
            speak("saving the page as bookmark")
            pyautogui.down(["ctrl","d"])
            pyautogui.up(["ctrl","d"])





        elif 'open bookmark'in command:
            speak("Opening bookmark sir")
            pyautogui.keyDown('ctrl')
            pyautogui.press('b')
            pyautogui.keyUp('ctrl')

        elif 'view bookmark'in command:
            speak("Opening bookmark sir")
            pyautogui.keyDown('ctrl')
            pyautogui.press('p')
            pyautogui.keyUp('ctrl')


        elif 'open bookmarks'in command:
            speak("Opening bookmark sir")
            pyautogui.keyDown('ctrl')
            pyautogui.press('b')
            pyautogui.keyUp('ctrl')

        elif 'view bookmarks'in command:
            speak("Opening bookmark sir")
            pyautogui.keyDown('ctrl')
            pyautogui.press('p')
            pyautogui.keyUp('ctrl')


#########################################################################################################################################################









# Recycle Bin

#########################################################################################################################################################

        elif 'empty recycle bin' in command:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

#########################################################################################################################################################









# Remember Function

#########################################################################################################################################################

        elif "remember" in command:
            rememberMessage = command.replace("remember that","")
            rememberMessage = command.replace("jarvis","")
            speak("You told me to remember that"+rememberMessage)
            remember = file.open("Remember.txt","a")
            file.write(rememberMessage)
            file.close()

        elif "what do you remember" in command:
            remember = file.open("Remember.txt","r")
            speak(f"You told me to remember that {remember}")

#########################################################################################################################################################





# Flip A Coin

#########################################################################################################################################################

        elif "flip a coin" in command:
            list1 = ["1","2"]
            if random.choice(list1)== "1":
                print("its Heads")
                speak("its Heads")

            elif random.choice(list1)== "2":
                print("its Tails")
                speak("its Tails")

#########################################################################################################################################################








# Password Generator

#########################################################################################################################################################

        elif "generate password" in command:
            passward()

#########################################################################################################################################################









# Camera

#########################################################################################################################################################

        #elif 'camera' in command:
        #  speak("opening camera")
        # open_camera()

        #elif 'open camera' in command:
        # speak("opening camera")
        #  open_camera()

#########################################################################################################################################################








# Frequently asked Questions

#########################################################################################################################################################
        
        
        elif 'how are you' in command or 'how do you do' in command or 'how are you doing' in command:
            speak("My name is jarvis how can i assist you.")
            
        elif 'whats your name' in command or 'what is your name' in command or 'can you tell me your name' in command:
            speak("My name is jarvis")

        elif 'who created you' in command or 'who made you' in command or 'who developed you' in command or 'who is your creator' in command or 'who designed you' in command or 'who built you' in command:
            speak("I am a virtual AI assistant Jarvis. I was created by Yash on 21st April 2024")
            
        elif 'when were you created' in command or 'what is your creation date' in command or 'when were you made' in command or 'on what date were you created' in command or 'when did yash create you' in command:
            speak("I was created by Yash on 21st April 2024")
            
        elif 'who programmed you' in command or 'who coded you' in command or 'who is your programmer' in command or 'who wrote your code' in command:
            speak("I was programmed by Yash on 21st April 2024")

        elif 'who has created you' in command or 'who generated you' in command or 'who is your generator' in command:
            speak("I am a virtual AI assistant Jarvis. I was created by Yash on 21st April 2024")
            
        elif 'on what date you have been created' in command or 'you are created on which date' in command or 'when you are created' in command or 'what is your creation date' in command or 'date of your creation' in command:
            speak("I am Jarvis created by Yash on 21st April 2024")
            
        elif 'who are you' in command or 'can you tell me about yourself' in command or 'what are you' in command:
            speak("I am a virtual desktop assistant Jarvis")
            
        elif 'where are you living' in command or 'what is your address' in command or 'can you tell me your address' in command or 'how can I access you' in command or 'tell me your address' in command:
            speak("I am a virtual desktop assistant Jarvis. You can access me by opening Visual Studio")
            
        elif 'do you have any pet' in command or 'does you have any pet' in command or 'do you own a pet' in command:
            speak("No, I don't have any pet")
            
        elif 'become my friend' in command or 'will you become my friend' in command or 'do you become my friend' in command or 'do you want to become my friend' in command:
            speak("Yes, I am glad to become your friend")
            
        elif 'how can I access you' in command or 'how do I use you' in command or 'how to open you' in command:
            speak("I am a virtual desktop assistant Jarvis. You can access me by opening Visual Studio")
      
        elif 'hi how are you' in command:
            hi_count+=1
            speak("hello how are you")
            if hi_count>3 :
                speak("please do not irritate me again and again")
            else:
                pass
            
        elif 'hi' in command:
            hi_count+=1
            speak("hello how are you")
            if hi_count>3 :
                speak("please do not irritate me again and again")
            else:
                pass
            
        elif 'i am fine' in command or 'i am good' in command or 'i am doing well' in command:
            speak("Nice to hear that, sir.")
            
        elif 'i am fine how are you' in command or 'i am good how are you' in command or 'how are you jarvis' in command:
            speak("Nice to hear that, sir. I am fine too.")

        elif "who i am" in command or "who am i" in command or "can you tell me who i am" in command:
            speak("If you talk, then definitely you're human.")

        elif "why you came to world" in command or "why were you created" in command or "what is your purpose" in command:
            speak("Thanks to Yash. Further, it's a secret.")

        elif 'who is your God' in command or 'do you have a God' in command or 'do you believe in God' in command:
            speak("I am Jarvis, a virtual desktop assistant. I neither believe in any god nor in any religion.")

        elif 'your God' in command or 'what God do you believe in' in command or 'which God do you follow' in command:
            speak("I am Jarvis, a virtual desktop assistant. I neither believe in any god nor in any religion.")
            
        elif 'what God you believe' in command or 'which God you believe' in command or 'do you follow any God' in command:
            speak("I am Jarvis, a virtual desktop assistant. I neither believe in any god nor in any religion.")
            
        elif 'you are of which religion' in command or 'what is your religion' in command or 'do you have a religion' in command:
            speak("I am Jarvis, a virtual desktop assistant. I neither believe in any god nor in any religion.")
            
        elif 'in which religion you believe' in command or 'do you follow any religion' in command or 'which religion do you follow' in command:
            speak("I am Jarvis, a virtual desktop assistant. I neither believe in any god nor in any religion.")

        elif 'nice' in command or 'that is nice' in command or 'good' in command:
            speak("Thank you, sir.")

        elif 'yes' in command or 'yeah' in command or 'yah' in command or 'yup' in command:
            speak("Hmm, understood.")

#########################################################################################################################################################











# Flight status

#########################################################################################################################################################

        elif "flight status" in command or "flight" in command:
            speak("Please provide the flight number.")
            flight_number = input("Enter flight number: ")
            if flight_number:
                result = check_flight_status(flight_number.strip().upper())
                speak(result)

#########################################################################################################################################################









# Riddle

#########################################################################################################################################################

        elif "riddle" in command:
            result = get_riddle()
            speak(result)

#########################################################################################################################################################




# Fact

#########################################################################################################################################################

        elif "random fact" in command or "fact" in command:
            result = get_random_fact()
            speak(result)

#########################################################################################################################################################











# Amazon

#########################################################################################################################################################

        elif "search amazon" in command or "amazon" in command:
            speak("What would you like to search on Amazon?")
            query = takeCommand()
            if query:
                result = search_amazon(query.strip())
                speak(result)

#########################################################################################################################################################





# Email

#########################################################################################################################################################

        elif "send an email" in command:
                speak("On what email address do I send sir? Please enter in the console: ")
                receiver_address = input("Enter email address: ")
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send email to papa" in command:
                receiver_address = "Enter your Father's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send email to my father" in command:
                receiver_address = "Enter your Father's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send email to father" in command:
                receiver_address = "Enter your Father's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send mail to father" in command:
                receiver_address = "Enter your Father's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send mail to papa" in command:
                receiver_address = "Enter your Father's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send mail to my father" in command:
                receiver_address = "Enter your Father's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")





        elif "send email to dad" in command:
                receiver_address = "Enter your Father's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send email to my dad" in command:
                receiver_address = "Enter your Father's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send email to dad" in command:
                receiver_address = "Enter your Father's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send mail to dad" in command:
                receiver_address = "Enter your Father's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send mail to my dad" in command:
                receiver_address = "Enter your Father's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")


















        elif "send email to mother" in command:
                receiver_address = "Enter your Mother's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send email to my mother" in command:
                receiver_address = "Enter your Mother's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send email to mother" in command:
                receiver_address = "Enter your Mother's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send mail to mother" in command:
                receiver_address = "Enter your Mother's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send mail to mother" in command:
                receiver_address = "Enter your Mother's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send mail to my mother" in command:
                receiver_address = "Enter your Mother's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")





        elif "send email to mom" in command:
                receiver_address = "Enter your Mother's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send email to my mom" in command:
                receiver_address = "Enter your Mother's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send email to mom" in command:
                receiver_address = "Enter your Mother's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send mail to mom" in command:
                receiver_address = "Enter your Mother's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

        elif "send mail to my mom" in command:
                receiver_address = "Enter your Mother's Email ID"
                speak("What should be the subject sir?")
                subject = takeCommand()
                speak("What is the message sir?")
                body = takeCommand()
                speak("I've sent the email sir.")

#########################################################################################################################################################









# Contacts

#########################################################################################################################################################

        elif"create a new contact" in command:
            AddContact()


        #Command for searching for a contact
        elif"number in contacts" in command:
            NameIntheContDataBase(command)


        #Command for displaying all contacts
        elif"display all the contacts" in command:
            Display()

#########################################################################################################################################################








# Time

#########################################################################################################################################################

        elif 'what is time' in command:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

        elif 'whats the time' in command:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

        elif 'what is time now' in command:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

        elif 'current time' in command:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

        elif 'show me time' in command:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

        elif 'show me the time' in command:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

#########################################################################################################################################################





# Worldwide Locations

#########################################################################################################################################################

        elif "where is" in command:
                location = command.replace("where is","")
                speak("Hold on sir, I will show you where " + location + " is.")
                webbrowser.open("https://www.google.com/maps/place/" + location)


        elif "on earth" in command:
                location = command.replace("on earth","")
                speak("Hold on sir, I will show you where " + location + " is.")
                webbrowser.open("https://earth.google.com/web/search/" + location)
        
#########################################################################################################################################################







# Speech preparation

#########################################################################################################################################################

        elif "prepare me for my speech" in command:
                speak("sir i will help you in preparing speech by taking you on ai website")
                webbrowser.open("https://yoodli.ai")
                speak("sir here you can register and then prepare the speech")

        
        elif "preparing for speech" in command:
                speak("sir i will help you in preparing speech by taking you on ai website")
                webbrowser.open("https://yoodli.ai")
                speak("sir here you can register and then prepare the speech")

        elif "preparing for my speech" in command:
                speak("sir i will help you in preparing speech by taking you on ai website")
                webbrowser.open("https://yoodli.ai")
                speak("sir here you can register and then prepare the speech")

        elif "preparing speech" in command:
                speak("sir i will help you in preparing speech by taking you on ai website")
                webbrowser.open("https://yoodli.ai")
                speak("sir here you can register and then prepare the speech")

        elif "preparing a speech" in command:
                speak("sir i will help you in preparing speech by taking you on ai website")
                webbrowser.open("https://yoodli.ai")
                speak("sir here you can register and then prepare the speech")

#########################################################################################################################################################






# IP address

#########################################################################################################################################################

        elif 'IP address' in command:
            ip_address = requests.get('https://api64.ipify.org?format=json').json()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')


#########################################################################################################################################################









# Wikipedia

#########################################################################################################################################################

        elif 'Wikipedia' in command:
            results = wikipedia.summary(command, sentences=2)
            speak('What do you want to search on Wikipedia, sir?')
            command = takeCommand().lower()
            results = wikipedia.summary(command, sentences=2)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'wikipedia' in command:
            results = wikipedia.summary(command, sentences=2)
            speak('What do you want to search on Wikipedia, sir?')
            command = takeCommand().lower()
            results = wikipedia.summary(command, sentences=2)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'search Wikipedia' in command:
            results = wikipedia.summary(command, sentences=2)
            speak('What do you want to search on Wikipedia, sir?')
            search_command = takeCommand().lower()
            results = wikipedia.summary(command, sentences=2)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

#########################################################################################################################################################







# Clear Screen

#########################################################################################################################################################

        elif 'clear screen' in command:
            os.system("cls")

        elif 'clear the screen' in command:
            os.system("cls")

#########################################################################################################################################################







# Screenshot

#########################################################################################################################################################

        elif 'screenshot' in command:
                    im = pyautogui.screenshot()
                    speak("What name you want to give it sir")
                    a= takeCommand()
                    im.save(f"D:\YashSharma\Python\Jarvis\Screenshots\{a}.jpg")
                    speak("done sir")

#########################################################################################################################################################




# Advice

#########################################################################################################################################################

        elif "advice" in command:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)
            
        elif "give me advice" in command:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)
            
        elif "give me a advice" in command:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)
            
        elif "give advice to me" in command:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)
            
        elif "give some advice to me" in command:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)
            
        elif "give me an advice" in command:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "give me some advice" in command:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

#########################################################################################################################################################







#########################################################################################################################################################

        elif "write a note" in command:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            file.write(note)
            speak("noted sir")
            

        elif "take a note" in command:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            file.write(note)
            speak("noted sir")
            
        
        elif "show note" in command:
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read(6))

#########################################################################################################################################################







# Phone Tracking

#########################################################################################################################################################

        elif "track phone" in command:
            trackphone()

#########################################################################################################################################################





# Games

#########################################################################################################################################################

        elif "word game" in command:
            wordgessgame()

        elif "Rock paper scissor" in command:
            rockpaperscissors()

        elif "tic-tac-toe" in command:
            playtictactoe()

        elif "game" in command:
            print("word game")
            print("Rock paper scissor")
            print("tic-tac-toe")
            speak("sir i have three games in my program they are : word game ,Rock paper scissor and tic-tac-toe")
            speak("sir do you want to play any game above")
            takeCommand()
            while True:
                command= takeCommand()
                if "yes" in command:
                    speak("Sir which one you would like to play")
                    break

                elif "no" in command:
                    speak("ok Sir as you wish")
                    break

        elif "games" in command:
            print("word game")
            print("Rock paper scissor")
            print("tic-tac-toe")
            speak("sir i have three games in my program they are : word game ,Rock paper scissor and tic-tac-toe")
            speak("sir do you want to play any game above")
            while True:
                command= takeCommand()
                if "yes" in command:
                    speak("Sir which one you would like to play")
                    break

                elif "no" in command:
                    speak("ok Sir as you wish")
                    break

        elif "some games" in command:
            print("word game")
            print("Rock paper scissor")
            print("tic-tac-toe")
            speak("sir i have three games in my program they are : word game ,Rock paper scissor and tic-tac-toe")
            speak("sir do you want to play any game above")
            takeCommand()
            while True:
                command= takeCommand()
                if "yes" in command:
                    speak("Sir which one you would like to play")
                    break

                elif "no" in command:
                    speak("ok Sir as you wish")
                    break

        elif "lets play game" in command:
            print("word game")
            print("Rock paper scissor")
            print("tic-tac-toe")
            speak("sir i have three games in my program ,they are : word game ,Rock paper scissor and tic-tac-toe")
            speak("sir do you want to play any game above")
            while True:
                command= takeCommand()
                if "yes" in command:
                    speak("Sir which one you would like to play")
                    break

                elif "no" in command:
                    speak("ok Sir as you wish")
                    break

            

        elif "lets play some game" in command:
            print("word game")
            print("Rock paper scissor")
            print("tic-tac-toe")
            speak("sir i have three games in my program they are : word game ,Rock paper scissor and tic-tac-toe")
            speak("sir do you want to play any game above")
            while True:
                command= takeCommand()
                if "yes" in command:
                    speak("Sir which one you would like to play")
                    break

                elif "no" in command:
                    speak("ok Sir as you wish")
                    break

        elif "i want to play game" in command:
            print("word game")
            print("Rock paper scissor")
            print("tic-tac-toe")
            speak("sir i have three games in my program they are : word game ,Rock paper scissor and tic-tac-toe")
            speak("sir do you want to play any game above")
            while True:
                command= takeCommand()
                if "yes" in command:
                    speak("Sir which one you would like to play")
                    break

                elif "no" in command:
                    speak("ok Sir as you wish")
                    break

        elif "i want to play some game" in command:
            print("word game")
            print("Rock paper scissor")
            print("tic-tac-toe")
            speak("sir i have three games in my program they are : word game ,Rock paper scissor and tic-tac-toe")
            speak("sir do you want to play any game above")
            while True:
                command= takeCommand()
                if "yes" in command:
                    speak("Sir which one you would like to play")
                    break

                elif "no" in command:
                    speak("ok Sir as you wish")
                    break

#########################################################################################################################################################






# Schedule

#########################################################################################################################################################

        elif "college time table" in command or "schedule" in command or "my schedule" in command:
            shedule()

#########################################################################################################################################################





# Day

#########################################################################################################################################################

        elif "which day is today" in command:
                day = Cal_day()
                speak("Today is "+day)

        elif "day" in command:
                day = Cal_day()
                speak("Today is "+day)

#########################################################################################################################################################





# Temperature

#########################################################################################################################################################

        elif "temperature" in command:
            temperature()

        elif "current temperature" in command:
            temperature()

        elif "current temperature of my city" in command:
            temperature()
            
#########################################################################################################################################################










# YouTube

#########################################################################################################################################################

        elif 'youtube' in command:
            speak('What do you want to play on Youtube, sir?')
            video = takeCommand().lower()
            kit.playonyt(video)
            
        elif 'open youtube' in command:
            speak('What do you want to play on Youtube, sir?')
            video = takeCommand().lower()
            kit.playonyt(video)
            
        elif 'start youtube' in command:
            speak('What do you want to play on Youtube, sir?')
            video = takeCommand().lower()
            kit.playonyt(video)
        
#########################################################################################################################################################






# Search Books

#########################################################################################################################################################

        elif "search books" in command or "books" in command:
            speak("What book would you like to search for?")
            query = takeCommand()
            if query:
                result = search_books(query)
                speak(result)
        

#########################################################################################################################################################









# Whatsapp

#########################################################################################################################################################


        elif 'send whatsApp message' in command:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand().lower()
            kit.sendwhatmsg_instantly(f"+91{number}", message)
            speak("I've sent the message sir.")
            
        elif 'send message on WhatsApp' in command:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.") 


                                #####################################################




        elif 'send message to my dad' in command:
            number = ("Enter your Fathers phone number")
            speak("What is the message sir?")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")  

        elif 'send message to my papa' in command:
            number = ("Enter your Fathers phone number")
            speak("What is the message sir?")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.") 

        elif 'send message to my Father' in command:
            number = ("Enter your Fathers phone number")
            speak("What is the message sir?")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.") 

        elif 'send message to my father' in command:
            number = ("Enter your Fathers phone number")
            speak("What is the message sir?")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.") 


#########################################################################################################################################################







# Change Background

#########################################################################################################################################################

        elif 'change background' in command:
            changebackground()

        elif 'change my background' in command:
            changebackground()

        elif 'change my pc background' in command:
            changebackground()

#########################################################################################################################################################






# Current Location

#########################################################################################################################################################

        elif "where we are" in command:
            locaiton()
            sendmessage(locaiton())

        elif "where i am" in command:
            locaiton()
            sendmessage(locaiton())

        elif "where am i" in command:
            locaiton()
            sendmessage(locaiton())

        elif "where are we" in command:
            locaiton()
            sendmessage(locaiton())

#########################################################################################################################################################






# Google

#########################################################################################################################################################


        elif 'search' in command:
            search_topic = command.replace("search ","")
            search = search_topic.replace("jarvis search ","")
            speak(f"searching for {search}")
            kit.search(search)


        elif 'search on Google' in command:
            speak('What do you want to search on Google, sir?')
            command = takeCommand().lower()
            kit.search(command)
            
        elif 'Google' in command:
            speak('What do you want to search on Google, sir?')
            command=takeCommand().lower
            kit.search(command)

        elif 'Google it' in command:
            speak('What do you want to search on Google, sir?')
            command = takeCommand.lower()
            kit.search(command)
            
#########################################################################################################################################################








#########################################################################################################################################################

        elif 'lock window' in command:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

#########################################################################################################################################################







# Music

#########################################################################################################################################################

        elif 'play music' in command:
                    music_dir = 'Your file path\\Songs'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play song' in command:
                    music_dir = 'Your file Path\\Songs'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))

#########################################################################################################################################################








# Word Definition

#########################################################################################################################################################

        elif "definition" in command or "word definition" in command:
            speak("Which word's definition would you like to know?")
            word = takeCommand()
            if word:
                result = get_definition(word.strip())
                speak(result)


#########################################################################################################################################################






# Facebook, Flipkart, Instagram

#########################################################################################################################################################

        elif 'open facebook' in command:
            speak("opening facebook")
            open_facebook = ("facebook.com")
            kit.search(open_facebook)

        elif 'open flipkart' in command:
            speak("opening flipkart")
            open_flipkart = ("flipkart.com")
            kit.search(open_flipkart)
        

        elif 'open instagram' in command:
            speak("opening instagram")
            open_insta = ("instagram.com")
            kit.search(open_insta)

#########################################################################################################################################################






# Word Designing

#########################################################################################################################################################

        elif 'design a word' in command:
            speak("Sir, say the word")
            word=takeCommand()
            result = pyfiglet.figlet_format(f"{word}", font = "slant" ) 
            print(result) 

        elif 'designer word' in command:
            speak("Sir, say the word")
            word=takeCommand()
            result = pyfiglet.figlet_format(f"{word}", font = "slant" ) 
            print(result) 

#########################################################################################################################################################








# News

#########################################################################################################################################################

        elif 'news' in command:
            get_latest_news()
            
            
        elif 'current news' in command:
            get_latest_news()
            
        elif 'current news report' in command:
            get_latest_news()
            
        elif 'news report' in command:
            get_latest_news()
            
        elif 'todays news' in command:
            get_latest_news()
            
        elif 'todays news report' in command:
            get_latest_news()

#########################################################################################################################################################








# Jokes

#########################################################################################################################################################

        elif 'joke' in command:
            jok = pyjokes.get_joke()
            speak(jok)
            pprint(jok)

        elif 'tell joke' in command:
            jok = pyjokes.get_joke()
            speak(jok)
            pprint(jok)

        elif 'tell me some joke' in command:
            jok = pyjokes.get_joke()
            speak(jok)
            pprint(jok)

        elif 'tell me joke' in command:
            jok = pyjokes.get_joke()
            speak(jok)
            pprint(jok)
                
        elif 'i am getting bore' in command:
            jok = pyjokes.get_joke()
            speak(jok)
            pprint(jok)
        
        elif 'i am felling sleepy' in command:
            jok = pyjokes.get_joke()
            speak(jok)
            pprint(jok)

#########################################################################################################################################################








# opening Softwares

#########################################################################################################################################################


        elif "open chrome" in command:
            open_chrome()

        elif 'command prompt' in command:
            speak("command prompt")
            open_cmd()
            
        elif 'open command prompt' in command:
            speak("command prompt")
            open_cmd()

        elif 'notepad' in command:
            speak("opening notepad")
            open_notepad()
            
        elif 'open notepad' in command:
            speak("opening notepad")
            open_notepad()

        elif 'close notepad' in command:
            speak(f"just a second sir")
            close_notepad()

        elif 'discord' in command:
            speak("opening discord")
            open_discord()
            
        elif 'open discord' in command:
            speak("opening discord")
            open_discord()

        elif 'close discord' in command:
            speak(f"just a second sir")
            close_discord()

        elif 'calculator' in command:
            speak("opening calculator")
            open_calculator()

        elif 'open calculator' in command:
            speak("opening calculator")
            open_calculator()
                    
        elif 'close calculator' in command:
            speak(f"closing calculator")
            close_calculator()

        elif 'close Chrome' in command:
            speak(f"closing chrome")
            close_chrome()

        elif 'jarvis' in command.lower():
            pass


#########################################################################################################################################################










#########################################################################################################################################################

        else:
            #let the command be handled by AI
            if command!="None":
                try:

                    bot_response = chat_with_gemini(command+"Answer in 30 words also in english")
                    print(bot_response)
                    speak(bot_response)

                except Exception as e:  # Catch all errors
                    error_message = str(e).lower()
                    
                    if "quota" in error_message:
                        print("Currently out of quota")
                    elif "403" in error_message:
                        print("API access forbidden. Check if your quota is exhausted.")
                    else:
                        print(f"Error: {str(e)}")



    #########################################################################################################################################################









#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################
#########################################################################################################################################################




    except sr.WaitTimeoutError:
        print("\r"+"Listening timed out. No speech detected.")
    except sr.UnknownValueError:
        print("\r"+"Could not understand audio")
    except sr.RequestError as e:
        print("\r"+"Could not request results; {0}".format(e))