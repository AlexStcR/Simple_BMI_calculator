import tkinter as tk
from tkinter import ttk, messagebox

class BMICalculator:
    def __init__(self, master):
        self.master = master
        master.title("BMI Calculator")
        master.configure(background="white")

        master.geometry("500x500")
        master.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Header Frame
        self.header_frame = ttk.Frame(self.master)
        self.header_frame.pack(pady=10)

        ttk.Label(
            self.header_frame,
            text="BMI Calculator",
            style='Header.TLabel'
        ).pack()

        # Input Frame
        self.input_frame = ttk.Frame(self.master)
        self.input_frame.pack(pady=10, padx=20, fill=tk.X)

        # Weight input
        ttk.Label(
            self.input_frame,
            text="Weight (kg):"
        ).grid(row=0, column=0, sticky=tk.W, pady=5)

        self.weight_entry = ttk.Entry(self.input_frame)
        self.weight_entry.grid(row=0, column=1, sticky=tk.E, pady=5)

        # Height input
        ttk.Label(
            self.input_frame,
            text="Height (m):"
        ).grid(row=1, column=0, sticky=tk.W, pady=5)

        self.height_entry = ttk.Entry(self.input_frame)
        self.height_entry.grid(row=1, column=1, sticky=tk.E, pady=5)

        # Button Frame
        self.button_frame = ttk.Frame(self.master)
        self.button_frame.pack(pady=10)

        ttk.Button(
            self.button_frame,
            text="Calculate BMI",
            command=self.calculate_bmi
        ).pack()

        # Result Frame
        self.result_frame = ttk.Frame(self.master)
        self.result_frame.pack(pady=10)

        self.bmi_result = ttk.Label(
            self.result_frame,
            text="BMI: ",
            font=('Arial', 12)
        )
        self.bmi_result.pack()

        self.category_result = ttk.Label(
            self.result_frame,

            font=('Arial', 12)
        )
        self.category_result.pack()

        # BMI Info Frame
        self.info_frame = ttk.Frame(self.master)
        self.info_frame.pack(pady=10)

        info_text = """BMI Categories:
                   - Underweight: <18.5
                   - Normal weight: 18.5-24.9
                   - Overweight: 25-29.9
                   - Obese: ≥30"""

        ttk.Label(self.info_frame,text=info_text,justify=tk.LEFT).pack()

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Weight and height must be positive numbers")
                return

            bmi = weight / (height ** 2)
            self.bmi_result.config(text=f"BMI: {bmi:.2f}")

            # Determine category
            if bmi < 18.5:
                category = "Underweight"



            elif 18.5 <= bmi < 25:
                category = "Normal weight"

            elif 25 <= bmi < 30:
                category = "Overweight"

            else:
                category = "Obese"


            self.category_result.config(text=f"Category: {category}", foreground=color)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

def main():
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
