# 🚀 Simple BMI Calculator with Python!

## A clean, object-oriented implementation of a BMI calculator featuring:

- ✔ Modern GUI built with tkinter/ttk
- ✔ Input validation and error handling
- ✔ OOP structure for maintainability
- ✔ Practical health metric tool

### Why I built this:
As part of my skill development in Python automation and GUI programming, this project combines:

- OOP best practices

- User-friendly interfaces

- Real-world health calculations


### A step-by-step walkthrough of my Tkinter GUI project



## 1️⃣ Imports & Setup



```python
import tkinter as tk
from tkinter import ttk, messagebox
```


### Key Components:

- tkinter: Base GUI toolkit

- ttk: Themed widgets for modern look

- messagebox: Error handling popups


## 2️⃣ Class Initialization

```python
class BMICalculator:
    def __init__(self, master):
        self.master = master
        master.title("BMI Calculator")
        master.geometry("500x500")
        master.resizable(False, False)
        self.create_widgets()
```
### What This Does:

- Creates main application window

- Sets fixed dimensions (500x500)

- Initializes UI components


## 3️⃣ UI Structure (4 Frames)

```python
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
```

## Visual Layout:

- [ Header ]
- [ Weight | Entry ]
- [ Height | Entry ]
- [ Calculate Button ]
- [ BMI Result ]
- [ Category Info ]

## 4️⃣ Core Calculation Logic

```python
def calculate_bmi(self):
    try:
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get())
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
            
        self.bmi_result.config(text=f"BMI: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")
```

## Features:

- Input validation

- BMI formula calculation

- Dynamic classification

- Error handling

## 5️⃣ Launching the App

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
```

## Standard Python Pattern:

- Creates Tk root window

- Initializes BMI Calculator instance

- Starts main event loop
