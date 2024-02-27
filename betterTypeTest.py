import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox  
import threading
from spellchecker import SpellChecker


class BetterTypeTest:
    """
    BetterTypeTest implements a typing test where the user can input text into a
    tkinter gui for a period of time, after which the input is evaluated and the
    number of real words and misspelled words are counted and displayed in a popup.
    """

    def __init__(self, root, duration=60):
        self.root = root
        self.duration = duration
        self.spell = SpellChecker()

        self.root.title("Typing Test")
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Times New Roman", 15))
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.focus()

        self.start_timer()

    def start_timer(self):

        # Start the timer
        threading.Timer(self.duration, self.evaluate_input).start()

    def evaluate_input(self):

        # Prevent further text entry
        self.text_area.config(state=tk.DISABLED)

        # get typed text and split
        typed_text = self.text_area.get("1.0", tk.END)
        words = typed_text.split()

        # get misspelled words and real words count
        misspelled = self.spell.unknown(words)
        real_words = [word for word in words if word not in misspelled]

        # calculate results
        real_words_count = len(words) - len(misspelled)

        # Show results in a simple popup
        result_message = f"Time taken: {self.duration} seconds\n" \
                         f"Total words typed: {len(words)}\n" \
                         f"Number of real words: {real_words_count}\n" \
                         f"Misspelled or unknown words: {len(misspelled)}"\
                         f"\n\nMisspelled words: {misspelled}"\
                         f"\n\nReal words: {real_words} out of {len(words)}\n"\
                         f"Accuracy: {real_words_count/len(words)*100:.2f}%"
        
        tk.messagebox.showinfo("Test Results", result_message)
        print(result_message)

if __name__ == "__main__":

    # init GUI
    root = tk.Tk()
    
    btt = BetterTypeTest(root, 60)  # Set duration of the test here
    root.mainloop()
