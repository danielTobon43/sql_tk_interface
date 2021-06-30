from tkinter import Tk, Frame, Entry, Button, font, Menu, Label, messagebox, StringVar
from bbdd_manager.bbdd_tools import BBDD


class InterCrud(object):
    """docstring for Crud"""

    def __init__(self, database_name, title='CRUD', width=220, height=300, font_size=12):
        self.database_name = database_name

        # ------------------------------- Root
        self.root = Tk()
        self.root.title(title)
        self.root.resizable(width=False, height=False)
        self.root.config(bg='gray')

        # ------------------------------- Data
        self.id = StringVar()
        self.name = StringVar()
        self.last_name = StringVar()
        self.password = StringVar()
        self.address = StringVar()

        # ------------------------------- Frame
        self.header_frame = Frame(self.root, bg='white', padx=10, pady=10)
        self.center_frame = Frame(self.root, bg='white', padx=10, pady=10)
        self.bottom_frame = Frame(self.root, bg='white', padx=10, pady=10)

        self.header_frame.config(width=width)
        self.center_frame.config(width=width)
        self.bottom_frame.config(width=width)

        self.header_frame.grid(row=0, column=0, sticky='nsew')
        self.center_frame.grid(row=1, column=0, sticky='nsew')
        self.bottom_frame.grid(row=2, column=0, sticky='nsew')

        # ------------------------------- Menu
        self.menu_bar = Menu(self.header_frame)
        self.bbdd_menu = Menu(self.menu_bar, tearoff=0)
        self.bbdd_menu.add_command(label='Connect')
        self.bbdd_menu.add_command(label='Exit')

        self.clear_menu = Menu(self.menu_bar, tearoff=0)
        self.clear_menu.add_command(label='Clear fields')

        self.crud_menu = Menu(self.menu_bar, tearoff=0)
        self.crud_menu.add_command(label='Create')
        self.crud_menu.add_command(label='Read')
        self.crud_menu.add_command(label='Update')
        self.crud_menu.add_command(label='Delete')

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label='License')
        self.help_menu.add_command(label='About')

        self.menu_bar.add_cascade(label='BBDD', menu=self.bbdd_menu)
        self.menu_bar.add_cascade(label='Clear', menu=self.clear_menu)
        self.menu_bar.add_cascade(label='CRUD', menu=self.crud_menu)
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)

        self.root.config(menu=self.menu_bar)

        # ------------------------------- Entry fields
        Label(self.center_frame, text='Id:', bg='white', font=('Arial', font_size)).grid(row=0, column=0, sticky='e', columnspan=1)
        self.id_entry = Entry(self.center_frame, bg='white', width=37, selectborderwidth=10, textvariable=self.id)
        self.id_entry.grid(row=0, column=1, sticky='w', pady=10, padx=10, columnspan=1)

        Label(self.center_frame, text='Name:', bg='white', font=('Arial', font_size)).grid(row=1, column=0, sticky='e', columnspan=1)
        self.name_entry = Entry(self.center_frame, width=37, bg='white', selectborderwidth=10, textvariable=self.name)
        self.name_entry.grid(row=1, column=1, sticky='ew', pady=10, padx=10, columnspan=1)

        Label(self.center_frame, text='Last name:', bg='white', fg='black', font=('Arial', font_size)).grid(row=2, column=0, sticky='e', columnspan=1)
        self.last_name_entry = Entry(self.center_frame, width=37, bg='white', selectborderwidth=10, textvariable=self.last_name)
        self.last_name_entry.grid(row=2, column=1, sticky='e', pady=10, padx=10, columnspan=1)

        Label(self.center_frame, text='Password:', bg='white', fg='black', font=('Arial', font_size)).grid(row=3, column=0, sticky='e', columnspan=1)
        self.password_entry = Entry(self.center_frame, width=37, bg='white', selectborderwidth=10, show='*', textvariable=self.password)
        self.password_entry.grid(row=3, column=1, sticky='e', pady=10, padx=10, columnspan=1)

        Label(self.center_frame, text='Address:', bg='white', fg='black', font=('Arial', font_size)).grid(row=4, column=0, sticky='e', columnspan=1)
        self.address_entry = Entry(self.center_frame, width=37, bg='white', selectborderwidth=10, textvariable=self.address)
        self.address_entry.grid(row=4, column=1, sticky='e', pady=10, padx=10, columnspan=1)

        # ------------------------------- Buttons
        self.create_btn = Button(self.bottom_frame, text='Create', width=12, height=2, font=font.Font(family='Arial', size=7))
        self.read_btn = Button(self.bottom_frame, text='Read', width=12, height=2, font=font.Font(family='Arial', size=7))
        self.update_btn = Button(self.bottom_frame, text='Update', width=12, height=2, font=font.Font(family='Arial', size=7))
        self.delete_btn = Button(self.bottom_frame, text='Delete', width=12, height=2, font=font.Font(family='Arial', size=7))

        self.create_btn.config(command=lambda: self.create_btn_func())
        self.read_btn.config(command=lambda: self.read_btn_func())
        self.update_btn.config(command=lambda: self.update_btn_func())
        self.delete_btn.config(command=lambda: self.delete_btn_func())

        self.create_btn.grid(row=0, column=0)
        self.read_btn.grid(row=0, column=1)
        self.update_btn.grid(row=0, column=2)
        self.delete_btn.grid(row=0, column=3)

        # ------------------------------- Loop
        self.root.mainloop()

    def create_btn_func(self):
        messagebox.showinfo(title='Message', message="Create button Baby!")
        database = BBDD(''.join([self.database_name, '.db']))
        data = self.get_fields_data()
        # database.add_entry(('Daniel', 'Tobon', '122445', 'jamundi'))
        database.add_entry(data)
        self.clear_fields_data()
        pass

    def read_btn_func(self):
        messagebox.showinfo(title='Message', message="Read button Baby!")
        database = BBDD(''.join([self.database_name, '.db']))
        id_ = self.id.get()
        entry_fields = database.get_data_from_id(id_)
        self.name.set(entry_fields[0][1])
        self.last_name.set(entry_fields[0][2])
        self.password.set(entry_fields[0][3])
        self.address.set(entry_fields[0][4])

    def update_btn_func(self):
        messagebox.showinfo(title='Message', message="Update button Baby!")
        database = BBDD(''.join([self.database_name, '.db']))
        id_ = self.id.get()
        entry_fields = database.get_data_from_id(id_)
        data = tuple((self.id.get(), self.name.get(), self.last_name.get(), self.password.get(), self.address.get()))
        properties_ = ["ID", "NOMBRE", "APELLIDO", "PASSWORD", "DIRECCION"]
        for i, val in enumerate(entry_fields[0]):
            if i == 0:
                continue
            else:
                if val != data[i]:

                    database.update_data_in_field(properties_[i], data[i], id_)
        self.clear_fields_data()

    def delete_btn_func(self):
        messagebox.showinfo(title='Message', message="Delete button Baby!")
        database = BBDD(''.join([self.database_name, '.db']))
        id_ = self.id.get()
        database.delete_data_by_id(id_)
        self.clear_fields_data()
        messagebox.showinfo(title='Message', message="Deleted data!")

    def on_exit(self):
        print("Program has finished!")

    def get_fields_data(self):
        data = tuple((self.name.get(), self.last_name.get(), self.password.get(), self.address.get()))
        return data

    def clear_fields_data(self):
        self.name.set('')
        self.last_name.set('')
        self.password.set('')
        self.address.set('')
