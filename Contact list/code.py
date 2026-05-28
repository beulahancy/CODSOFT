from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Contact Book")
root.geometry("400x500")

Label(root, text="Name").pack()
entry_name = Entry(root)
entry_name.pack()

Label(root, text="Phone").pack()
entry_phone = Entry(root)
entry_phone.pack()

Label(root, text="Email").pack()
entry_email = Entry(root)
entry_email.pack()

Label(root, text="Address").pack()
entry_address = Entry(root)
entry_address.pack()

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        contacts.append(contact)
        messagebox.showinfo("Success", "Contact Added")
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Error", "Name and Phone are required")


def view_contacts():
    listbox.delete(0, END)
    for contact in contacts:
        listbox.insert(END, f"{contact['name']} - {contact['phone']}")


def search_contact():
    search = entry_search.get().lower()
    listbox.delete(0, END)

    for contact in contacts:
        if search in contact['name'].lower() or search in contact['phone']:
            listbox.insert(END, f"{contact['name']} - {contact['phone']}")


def delete_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del contacts[index]
        view_contacts()
        messagebox.showinfo("Deleted", "Contact Deleted")
    else:
        messagebox.showwarning("Error", "Select a contact")


def update_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contacts[index]['name'] = entry_name.get()
        contacts[index]['phone'] = entry_phone.get()
        contacts[index]['email'] = entry_email.get()
        contacts[index]['address'] = entry_address.get()
        view_contacts()
        messagebox.showinfo("Updated", "Contact Updated")
    else:
        messagebox.showwarning("Error", "Select a contact")


def fill_fields(event):
    selected = listbox.curselection()
    if selected:
        contact = contacts[selected[0]]
        entry_name.delete(0, END)
        entry_name.insert(0, contact['name'])
        entry_phone.delete(0, END)
        entry_phone.insert(0, contact['phone'])
        entry_email.delete(0, END)
        entry_email.insert(0, contact['email'])
        entry_address.delete(0, END)
        entry_address.insert(0, contact['address'])


def clear_fields():
    entry_name.delete(0, END)
    entry_phone.delete(0, END)
    entry_email.delete(0, END)
    entry_address.delete(0, END)


Button(root, text="Add Contact", command=add_contact).pack(pady=5)
Button(root, text="Update Contact", command=update_contact).pack(pady=5)
Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

Label(root, text="Search").pack()
entry_search = Entry(root)
entry_search.pack()
Button(root, text="Search", command=search_contact).pack(pady=5)

listbox = Listbox(root)
listbox.pack(fill=BOTH, expand=True)
listbox.bind('<<ListboxSelect>>', fill_fields)

root.mainloop()