import tkinter as tk
from tkinter import messagebox

# Base Patient Class
class Patient:
    def __init__(self, pid, name, age, condition):
        self.pid = pid  # Patient ID
        self.name = name
        self.age = age
        self.condition = condition

    def __str__(self):
        return f"ID: {self.pid} | {self.name} ({self.age}) | Condition: {self.condition}"

# App Interface (Graphical User Interface)
class PatientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HIMS - Patient Record Manager")
        self.root.geometry("450x600")
        self.patients_list = []

        # --- Input Fields ---
        self.create_label_entry("Patient ID (Unique):", "id_entry")
        self.create_label_entry("Patient Name:", "name_entry")
        self.create_label_entry("Age:", "age_entry")
        self.create_label_entry("Current Condition:", "cond_entry")

        # --- Buttons ---
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Register", bg="#4CAF50", fg="white", width=12,
                  command=self.register_patient).grid(row=0, column=0, padx=5)
        
        tk.Button(btn_frame, text="Update Condition", bg="#FF9800", fg="white", width=12,
                  command=self.update_patient).grid(row=0, column=1, padx=5)

        tk.Button(root, text="Refresh List", bg="#2196F3", fg="white", width=26,
                  command=self.display_list).pack(pady=5)

        # --- Display Area ---
        tk.Label(root, text="Records Database:", font=('Arial', 10, 'italic')).pack(pady=5)
        self.display_box = tk.Listbox(root, width=60, height=12)
        self.display_box.pack(padx=10, pady=5)

    def create_label_entry(self, label_text, var_name):
        tk.Label(self.root, text=label_text, font=('Arial', 9, 'bold')).pack()
        entry = tk.Entry(self.root, width=40)
        entry.pack(pady=2)
        setattr(self, var_name, entry)

    def register_patient(self):
        pid = self.id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        cond = self.cond_entry.get()

        if all([pid, name, age, cond]):
            # Check if ID already exists
            if any(p.pid == pid for p in self.patients_list):
                messagebox.showerror("Error", "Patient ID must be unique!")
                return

            new_p = Patient(pid, name, age, cond)
            self.patients_list.append(new_p)
            messagebox.showinfo("Success", f"Registered: {name}")
            self.clear_fields()
            self.display_list()
        else:
            messagebox.showwarning("Incomplete", "Fill all fields to register.")

    def update_patient(self):
        search_id = self.id_entry.get()
        new_cond = self.cond_entry.get()

        if not search_id or not new_cond:
            messagebox.showwarning("Input Needed", "Enter Patient ID and New Condition to update.")
            return

        found = False
        for p in self.patients_list:
            if p.pid == search_id:
                p.condition = new_cond  # Updating the object attribute
                found = True
                break
        
        if found:
            messagebox.showinfo("Updated", f"Condition updated for ID: {search_id}")
            self.display_list()
            self.clear_fields()
        else:
            messagebox.showerror("Not Found", "No patient found with that ID.")

    def display_list(self):
        self.display_box.delete(0, tk.END)
        for p in self.patients_list:
            self.display_box.insert(tk.END, str(p))

    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.cond_entry.delete(0, tk.END)


root = tk.Tk()
app = PatientApp(root)
root.mainloop()