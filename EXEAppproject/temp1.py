# import tkinter as tk
#
# root = tk.Tk()
#
# canvas = tk.Canvas(root, width=300, height=300)
# canvas.pack()
#
#
# def hello():
#     label = tk.Label(
#         root, text="Hello World!", fg="blue", font=("Arial", 18, "bold")
#     )
#     canvas.create_window(150, 200, window=label)
#
#
# button = tk.Button(text="Click Me", command=hello, bg="brown", fg="white")
# canvas.create_window(150, 150, window=button)
#
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------
# import sys
# import tkinter as tk
#
#
# class PrintLogger:
#     def __init__(self, textbox):
#         self.textbox = textbox
#
#     def write(self, text):
#         self.textbox.insert(tk.END, text)
#
#
# root = tk.Tk()
#
# textbox = tk.Text(root)
# textbox.pack()
#
# printlogger = PrintLogger(textbox)
# sys.stdout = printlogger
#
# print("Hello, world!")  # This will appear in the Text widgetroot.mainloop()

#--------------------------------------------------------------------------------------------------
#
# import sys
# from tkinter import Tk, Button, Frame
# from tkinter.scrolledtext import ScrolledText
#
#
# class PrintLogger(object):  # create file like object
#
#     def __init__(self, textbox):  # pass reference to text widget
#         self.textbox = textbox  # keep ref
#
#     def write(self, text):
#         self.textbox.configure(state="normal")  # make field editable
#         self.textbox.insert("end", text)  # write text to textbox
#         self.textbox.see("end")  # scroll to end
#         self.textbox.configure(state="disabled")  # make field readonly
#
#     def flush(self):  # needed for file like object
#         pass
#
#
# class MainGUI(Tk):
#
#     def __init__(self):
#         Tk.__init__(self)
#         self.root = Frame(self)
#         self.root.pack()
#         self.redirect_button = Button(self.root, text="Redirect console to widget", command=self.redirect_logging)
#         self.redirect_button.pack()
#         self.redirect_button = Button(self.root, text="Redirect console reset", command=self.reset_logging)
#         self.redirect_button.pack()
#         self.test_button = Button(self.root, text="Test Print", command=self.test_print)
#         self.test_button.pack()
#         self.log_widget = ScrolledText(self.root, height=4, width=120, font=("consolas", "8", "normal"))
#         self.log_widget.pack()
#
#     def reset_logging(self):
#         sys.stdout = sys.__stdout__
#         sys.stderr = sys.__stderr__
#
#     def test_print(self):
#         print("Am i working?")
#
#     def redirect_logging(self):
#         logger = PrintLogger(self.log_widget)
#         sys.stdout = logger
#         sys.stderr = logger
#
#
# if __name__ == "__main__":
#     app = MainGUI()
#     app.mainloop()


# -------------------------------------------------------------------------------------------------------------
#
# import ctypes
# MessageBox = ctypes.windll.user32.MessageBoxW  # MessageBoxA in Python2
# MessageBox(None, 'Message\nfor\nthe\nuser', 'Window title', 0)

# ----------------------------------------------------------------------------------
import tkinter as tk
import sys

class ConsoleOutputRedirector:
    def __init__(self, label):
        self.label = label

    def write(self, message):
        self.label.config(text=self.label.cget("text") + message)

# Create the main window
root = tk.Tk()
root.title("Console Output in Label")

# Create a label widget to display console output
output_label = tk.Label(root, text="")
output_label.pack()

# Redirect stdout to the label
sys.stdout = ConsoleOutputRedirector(output_label)

# Print some output to demonstrate
print("Hello, world! This is console output.")

sys.stdout.flush()

# Start the GUI event loop
root.mainloop()
