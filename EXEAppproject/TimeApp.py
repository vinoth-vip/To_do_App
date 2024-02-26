from tkinter import *
from datetime import datetime, timedelta
import sys


main=Tk()

#StringVar for currentValue in R0C2
DEFAULT_TIME = "10:30"
currentValue = StringVar(main, DEFAULT_TIME)


def timemanagement(time_str):
        out_str = ""
        # Get input for date and time
        # time_str = input("Enter time (HH:MM): ")
        formatted_date = datetime.today().strftime("%Y-%m-%d")

        # Combine date and time strings into a datetime object
        try:
            datetime_str = f"{formatted_date} {time_str}"
            input_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        except ValueError as e:
            time_str = DEFAULT_TIME
            out_str += "You've enter the invalid time, So its taken default time automatically.\n"
            datetime_str = f"{formatted_date} {time_str}"
            input_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

            # return out_str
        # Adding the input time for 7.5 hrs
        minimum_hours = input_datetime + timedelta(hours=7.5)
        # Adding the input time for 9.5 hrs
        maximum_hours = input_datetime + timedelta(hours=9.5)

        # calculating time for 9.5 hrs
        maxDate = maximum_hours.strftime("%Y-%m-%d")
        maxTime = maximum_hours.strftime("%H:%M")
        formatted_time_12hr_9hers = datetime.strptime(str(maxTime), "%H:%M").strftime("%I:%M %p")

        # calculating time for 7.5 hrs
        minDate = minimum_hours.strftime("%Y-%m-%d")
        minTime = minimum_hours.strftime("%H:%M")
        formatted_time_12hr = datetime.strptime(str(minTime), "%H:%M").strftime("%I:%M %p")

        # Display the result
        out_str += (f"arrived at: Date-{formatted_date} Time:{time_str}\n")
        out_str += (f"Calculating the datetime after adding 7.5 hours: Date:{minDate} Time:{formatted_time_12hr}\n")
        out_str += (f"Calculating the datetime after adding 9.5 hours: Date:{maxDate} Time:{formatted_time_12hr_9hers}\n")

        return out_str
#Called by the setValues button, looks for content in the entry box and updates the "current" label



def setValues():
        content = entry.get()
        print("HI")
        if len(content) <= 5:
            print("output")
            print(timemanagement(content))
        else:
            print(content)
            exitProgram()


#This kills the program
def exitProgram():
        exit()

#Title and window size
main.title("TimeCalculation")
main.geometry("500x300")

#Descriptions on the far left
Label(main, text="Enter the time (HH:MM): ").grid(row=0, column=0)

#Entry boxes for values amidship
entry=Entry(main, width=10)
entry.grid(row=0, column=1)

#Displays what the value is currently set to.
currentValue = Label(textvariable=currentValue)
currentValue.grid(row=0,column=2)

#Takes any inputted values and sets them in the "Current" column using def setValues
setValues=Button(text='Set Values',width=30,command=setValues)
setValues.grid(row=9, column=0, columnspan=2)

#Red button to end program
exitButton=Button(main, text='Exit Program',fg='white',bg='red',width=30, height=1,command=exitProgram)
exitButton.grid(row=20, column = 0, columnspan=2)
main.mainloop()

