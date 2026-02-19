#imports the Tkinter module and aliases it as 'tk' for easier reference and imports the 'messagebox'module from Tkinter,used to display various types of message boxes.

import tkinter as tk
from tkinter import messagebox

# A dictionary map to convert letter grades to grade points 
grade_to_point = {
    'A+': 4.0,
    'A' : 3.75,
    'A-': 3.50,
    'B+' : 3.25,
    'B'  : 3.0,
    'B-': 2.75,
    'C+': 2.50,
    'C': 2.25,
    'D': 2.0,
    'F': 0.0
}
# Function to calculate CGPA, defined with a single parameter 'subjects', expected to be a list of dictionaries representing subjects.
def calculate_cgpa(subjects):
    total_credits = 0
    weighted_grades = 0
       
    for subject in subjects:
        credit = subject['credit'] #extracting the value of the "credit" key from the subject dictionary
        grade = subject['grade'] #extracting the value of the "grade" key from the subject dictionary.
        grade_point = grade_to_point.get(grade, 0)
        
        total_credits += credit
        weighted_grades += credit * grade_point
    
    if total_credits == 0:
        return 0
    
    return weighted_grades / total_credits

# Function to convert marks to grade
def marks_to_grade(marks):
    if 80 <= marks <= 100:
        return 'A+'
    elif 75 <= marks <= 79:
        return 'A'
    elif 70 <= marks <= 74:
        return 'A-'
    elif 65 <= marks <= 69:
        return 'B+'
    elif 60 <= marks <= 64:
        return 'B'
    elif 55 <= marks <= 59:
        return 'B-'
    elif 50 <= marks <= 54:
        return 'C+'
    elif 45 <= marks <= 49:
        return 'C'
    elif 40 <= marks <= 44:
        return 'D'
    elif 0 <= marks <= 39:
        return 'F'
    else:
        raise ValueError("Invalid marks. Marks must be between 0 to 100.")

# GUI setup.This method serves as the constructor for the CGPAApp class.
class CGPAApp(tk.Tk):
    def __init__(self):
        super().__init__() # Call the constructor of the superclass (tk.Tk)
        self.title("CGPA Calculator")
        self.geometry("400x400")
        
        self.num_subjects_var = tk.IntVar()
        self.num_subjects_var.set(1)  # Default to 1
        
        # Prompt for number of subjects
        tk.Label(self, text="Number of Courses : ", font="TimesNewRoman").pack(pady=10)
        tk.Entry(self, textvariable=self.num_subjects_var).pack(pady=10)
        
        tk.Button(self, text="Enter", bg="skyblue", font="TimesNewRoman", command=self.create_subject_entries).pack(pady=10)
        
        self.subject_entries = []
        
    def create_subject_entries(self):
        num_subjects = self.num_subjects_var.get()
        if num_subjects <= 0:
            messagebox.showerror("Error", "Number of subjects must be greater than 0")
            return
        
        self.subject_entries = []
        subject_frame = tk.Frame(self)
        subject_frame.pack() #pack() method is used to organize and display widgets.
        
        for i in range(num_subjects):
            entry_frame = tk.Frame(subject_frame)
            entry_frame.pack(pady=5)
            
            tk.Label(entry_frame, text=f"Course Code : ", font="TimesNewRoman").pack(side=tk.LEFT)
            subject_name = tk.Entry(entry_frame)
            subject_name.pack(side=tk.LEFT)
            
            tk.Label(entry_frame, text=" Credit(s) : ", font="TimesNewRoman").pack(side=tk.LEFT)
            subject_credit = tk.Entry(entry_frame)
            subject_credit.pack(side=tk.LEFT)
            
            tk.Label(entry_frame, text=" Marks :", font="TimesNewRoman").pack(side=tk.LEFT)
            subject_marks = tk.Entry(entry_frame)
            subject_marks.pack(side=tk.LEFT)
            
            self.subject_entries.append((subject_name, subject_credit, subject_marks))
        
        tk.Button(self, text="Calculate CGPA", bg="skyblue", font="TimesNewRoman", command=self.compute_cgpa).pack(pady=10)
        tk.Button(self, text="Clear", bg="skyblue", font="TimesNewRoman", command=self.clear_entries).pack(pady=10)
        
    def compute_cgpa(self):
        subjects = []
        subject_grade_info = []
        
        for name_entry, credit_entry, marks_entry in self.subject_entries:
            name = name_entry.get().strip() #removes whitespace characters (like spaces, tabs, or newlines)
            
            #try and except blocks are used for error handling
            try:
                credit = int(credit_entry.get())
            except ValueError:
                messagebox.showerror("Error", f"Invalid credit for Course {name}")
                return
            
            try:
                marks = float(marks_entry.get())
                if marks < 0 or marks > 100:
                    raise ValueError()
            except ValueError:
                messagebox.showerror("Error", f"Invalid mark for {name} course.\n Marks for each course should be between 0 to 100.")
                return
            
            # Get the grade from the marks
            grade = marks_to_grade(marks)
            
            subjects.append({'name': name, 'credit': credit, 'grade': grade})
            subject_grade_info.append(f"{name}: {credit} credits, Grade: {grade} ({marks} marks)") #append() is a method used to add an element to the end of a list
        
        cgpa = calculate_cgpa(subjects)
        result_message = "\n".join(subject_grade_info)+f"\n\n CGPA  {cgpa:.2f}" #join() method is a string method that concatenates.
        messagebox.showinfo("CGPA Result", result_message)
     
    def clear_entries(self):
        for name_entry, credit_entry, marks_entry in self.subject_entries:
            name_entry.delete(0, tk.END) #Delete used to delete text from the widget.
            credit_entry.delete(0, tk.END) #0 and tk.END indicate the range of text to delete. 
            marks_entry.delete(0, tk.END) #0 and tk.END represent start and end of the text.
            
#checks the current script is being run as the main program or not and __name__ is a special built-in variable
if __name__ == "__main__": 
    app = CGPAApp() #CGPAApp runs its mainloop() method,  allows the GUI application to run
    app.mainloop()
