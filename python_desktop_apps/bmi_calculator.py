#####################################
# BMI calculator app in python:
# -----------------------------
# BMI aka body mass index is a tool
# that's used to access and monitor
# changes in body weight.
#
# Calculate BMI using feet/inches:
# -------------------------------
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
######################################

import tkinter as tk


class BMICalculator:

    def __init__(self, master):

        # BMI converter for inches and feet

        self.bmi_feet_inches_label = tk.Label(text='Enter height in feet')
        self.bmi_feet_inches_label.place(x=0, y=0, height=25, width=250)

        self.height_in_feet = tk.StringVar()
        self.weight_in_pounds = tk.StringVar()
        self.pounds_bmi = tk.StringVar()

        self.bmi_feet_inches_entry = tk.Entry(textvariable=self.height_in_feet)
        self.bmi_feet_inches_entry.place(x=275, y=0, height=25, width=250)
        self.bmi_feet_inches_entry.config(highlightbackground='white smoke')

        self.height_inches_label = tk.Label(text='Enter weight in pounds')
        self.height_inches_label.place(x=0, y=40, height=25, width=250)

        self.weight_pounds_entry = tk.Entry(textvariable=self.weight_in_pounds)
        self.weight_pounds_entry.place(x=275, y=40, height=25, width=250)
        self.weight_pounds_entry.config(highlightbackground='white smoke')

        self.bmi_button = tk.Button(text='Find BMI', command=self.bmi_in_pounds)
        self.bmi_button.place(x=50, y=80, width=100)

        self.display_bmi_inches = tk.Entry(textvariable=self.pounds_bmi)
        self.display_bmi_inches.place(x=200, y=80, height=25, width=100)
        self.display_bmi_inches.config(highlightbackground='black', bg='lavender')

        # BMI weight status labels

        tk.Label(bg='black', fg='white', text='BMI Weight Status').place(x=325, y=80)
        tk.Label(bg='floral white', text='Below 18.5     Under weight').place(x=325, y=95)
        tk.Label(bg='azure', text='Below 18.5-24.9     Normal weight').place(x=325, y=110)
        tk.Label(bg='yellow', fg='black', text='Below 25.0-29.9     Over weight').place(x=325, y=125)
        tk.Label(bg='red', fg='white', text='30.0 and above     Obese').place(x=325, y=140)

        # BMI converter for meters and kilograms

        self.height_in_meters = tk.StringVar()
        self.weight_in_kilos = tk.StringVar()
        self.kilos_bmi = tk.StringVar()

        self.meters_and_kilo_label = tk.Label(text='Enter height in meters')
        self.meters_and_kilo_label.place(x=100, y=200, width=400)

        self.height_meters_label = tk.Label(text='Enter height in meters')
        self.height_meters_label.place(x=0, y=250, height=25, width=250)
        self.height_meters_entry = tk.Entry(textvariable=self.height_in_meters)
        self.height_meters_entry.place(x=275, y=250, height=25, width=250)
        self.height_meters_entry.config(highlightbackground='white smoke')

        self.bmi_meters_kilo_label = tk.Label(text='Enter weight in kilograms')
        self.bmi_meters_kilo_label.place(x=0, y=300, height=25, width=260)
        self.bmi_meters_kilo_entry = tk.Entry(textvariable=self.weight_in_kilos)
        self.bmi_meters_kilo_entry.place(x=275, y=300, height=25, width=260)
        self.bmi_meters_kilo_entry.config(highlightbackground='white smoke')

        self.bmi_button_meters = tk.Button(text='Find BMI', command=self.weight_in_kilograms)
        self.bmi_button_meters.place(x=50, y=350, width=100)

        self.display_bmi_meters = tk.Entry(textvariable=self.kilos_bmi)
        self.display_bmi_meters.place(x=200, y=350, height=25, width=100)
        self.display_bmi_meters.config(highlightbackground='black', bg='lavender')

    def bmi_in_pounds(self):
        """
        height will be in feet, and
        weight will be in pounds.
        BMI = (weight in pounds /
        (height in inches) x (height in inches)) x 703
        """
        inches = float(self.height_in_feet.get()) * 12
        pounds = float(self.weight_in_pounds.get())
        bmi = round(float(pounds / (inches ** 2)) * 703, 2)
        self.pounds_bmi.set(bmi)

    def weight_in_kilograms(self):
        """
        Calculate BMI using meters and kilograms:
        BMI =	Weight in Kilograms / (Height in Meters)
        x (Height in Meters)
        """

        meters = float(self.height_in_meters.get())
        kilograms = float(self.bmi_meters_kilo_entry.get())
        bmi = round(float(kilograms / (meters ** 2)), 2)
        self.kilos_bmi.set(bmi)


def run():
    root = tk.Tk()
    root.title('Body Mass Index Calculator')
    root.geometry('600x600')
    root.configure(bg='AntiqueWhite2')
    BMICalculator(root)
    tk.mainloop()


if __name__ == '__main__':
    run()







