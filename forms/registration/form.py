import tkinter as tk
from tkinter import messagebox
from forms.registration.form_designer import FormRegisterDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Auth_User
import util.encoding_decoding as end_dec


class FormRegister(FormRegisterDesigner):
    def __init__(self):
        self.auth_repository = AuthUserRepository()
        super().__init__()

    def register(self):
        if (self.isConfimactionPassword()):
            user = Auth_User()
            user.username = self.usuario.get()
            user_db: Auth_User = self.auth_repository.getUserByUserName(
                self.usuario.get())

            if not (self.isUserRegistro(user_db)):
                user.password = end_dec.encrypted(self.password.get())
                self.auth_repository.insertUser(user)
                messagebox.showerror(
                    message="se registro el usuario", title="mensaje")
                self.ventana.destroy()

    def isConfimactionPassword(self):
        status: bool = True
        if (self.password.get() != self.confirmation.get()):
            status = False
            messagebox.showerror(
                message="la contraseña no coincide por favor verificar el registro", title="Mensaje")
            self.password.delete(0, tk.END)
            self.confirmation.delete(0, tk.END)
        return status

    def isUserRegistro(self, user: Auth_User):
        status: bool = False
        if (user != None):
            status = True
            messagebox.showerror(
                message=f"El usuario {user} ya existe en la base de datos.", title="Error")
        return status
