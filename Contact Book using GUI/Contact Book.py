#!/usr/bin/env python
# coding: utf-8

# In[7]:


from tkinter import *
from tkinter import ttk, messagebox

class AddressBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Address Book")
        self.root.geometry("400x300")
        self.root.configure(bg="#dfe6e9")

        self.contacts = []

        # Background Image
        background_image = PhotoImage(file="C:\\Users\\Nagasai\\OneDrive\\Pictures\\Luffy.png")
        background_label = Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        # UI Components
        self.label_title = Label(root, text="Address Book", font=("Helvetica", 20, "bold"), bg="#2c3e50", fg="white", pady=10)
        self.label_title.pack(fill=X)

        frame = Frame(root, bg="#ecf0f1", bd=5)
        frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.55, anchor="n")

        self.label_name = Label(frame, text="Name:", font=("Helvetica", 12), bg="#ecf0f1", fg="#333")
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.entry_name = Entry(frame, width=30, font=("Helvetica", 12))
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_phone = Label(frame, text="Phone:", font=("Helvetica", 12), bg="#ecf0f1", fg="#333")
        self.label_phone.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.entry_phone = Entry(frame, width=30, font=("Helvetica", 12))
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        self.button_add = Button(frame, text="Add Contact", command=self.add_contact, font=("Helvetica", 12, "bold"), bg="#3498db", fg="white", relief=FLAT)
        self.button_add.grid(row=2, columnspan=2, pady=10)

        self.button_view = Button(frame, text="View Contacts", command=self.view_contacts, font=("Helvetica", 12, "bold"), bg="#2ecc71", fg="white", relief=FLAT)
        self.button_view.grid(row=3, columnspan=2, pady=10)

        self.button_clear = Button(frame, text="Clear Entries", command=self.clear_entries, font=("Helvetica", 12, "bold"), bg="#e74c3c", fg="white", relief=FLAT)
        self.button_clear.grid(row=4, columnspan=2, pady=10)

        self.button_exit = Button(frame, text="Exit", command=root.destroy, font=("Helvetica", 12, "bold"), bg="#333", fg="white", relief=FLAT)
        self.button_exit.grid(row=5, columnspan=2, pady=10)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        if name and phone:
            contact = f"Name: {name}, Phone: {phone}"
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter both name and phone.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
        else:
            contacts_text = "\n".join(self.contacts)
            messagebox.showinfo("Contacts", contacts_text)

    def clear_entries(self):
        self.entry_name.delete(0, END)
        self.entry_phone.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = AddressBook(root)
    root.mainloop()


# In[ ]:




