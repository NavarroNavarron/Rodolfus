import tkinter as tk
from tkinter import ttk

class View():

    #Principal Janela
    tela = tk.Tk()
    tela.title("Registrar-se")
    tela.config(bg='black',height=600,width=300,padx=20,pady=20)

    register = True

#Inicio
    def __init__(self):
        self.telaDeRegistro()

#Tela de Registro
    def telaDeRegistro(self):
        #Frame
        self.telaRegistro = tk.Frame(self.tela,height=300,width=200,bg='black')
        self.telaRegistro.grid(row=0,column=0)

        #Labels
        titulo_label = tk.Label(self.telaRegistro,text="Criar conta:",font=('Helvetica bold',25),bg='black',fg='white')
        titulo_label.grid(row=2,column=0,columnspan=2,pady=5)

        email_label = tk.Label(self.telaRegistro,text="Email:",font=('Helvetica bold',16),bg='black',fg='white')
        email_label.grid(row=4,column=0,sticky='w')

        usuario_label = tk.Label(self.telaRegistro,text="Usuario:",font=('Helvetica bold',16),bg='black',fg='white')
        usuario_label.grid(row=3, column=0,sticky='w')

        senha_label = tk.Label(self.telaRegistro,text="Senha:",font=('Helvetica bold',16),bg='black',fg='white')
        senha_label.grid(row=5,column=0,sticky='w')

        temConta_label = tk.Label(self.telaRegistro,text=" Já possui conta?", font=('Helvetiva bold',10),bg='black',fg='white')
        temConta_label.grid(row=9,column=0,padx=12)

        self.alertaRegistro = tk.Label(self.telaRegistro,text="PREENCHA TODOS OS CAMPOS EM BRANCO!",fg='red',bg='black',font=('Helvetica bold',8))

        self.alertaEmailRegistro = tk.Label(self.telaRegistro,text="EMAIL JÁ EM USO!",fg='red',bg='black',font=('Helvetica bold',8))

        self.alertaUserRegistro = tk.Label(self.telaRegistro,text="USUÁRIO JÁ EM USO!",fg='red',bg='black',font=('Helvetica bold',8))
        #Botões
        registrar_button = tk.Button(self.telaRegistro,text="Registrar-se",width=17,font=('Helvetica bold',16),bg='black',fg='white')
        registrar_button.grid(row=8,column=0,columnspan=2,pady=10)

        irLogin_button = tk.Button(self.telaRegistro,text="Fazer Login",width=9,font=('Helvetica bold',10),bg='black',fg='white',command=self.switch)
        irLogin_button.grid(row = 9,column = 1)

        #Entries
        self.emailRegister_entry = tk.Entry(self.telaRegistro)
        self.emailRegister_entry.grid(row=4,column=1)

        self.usuarioRegister_entry = tk.Entry(self.telaRegistro)
        self.usuarioRegister_entry.grid(row=3,column=1)

        #self.getUserRegister = self.usuarioRegister_entry.get()

        self.senhaRegister_entry = tk.Entry(self.telaRegistro,show="*")
        self.senhaRegister_entry.grid(row=5,column=1)

        self.tela.mainloop()
    
    #Tela de Login
    def telaLogin(self):
        #Frame
        self.loginTela = tk.Frame(self.tela,width=300,height=200,bg='black')
        self.loginTela.grid(row=0,column=0)

        #Labels
        tituloLogin_label = tk.Label(self.loginTela,text="Fazer Login:",font=('Helvetica bold',25),bg='black',fg='white')
        tituloLogin_label.grid(row=2,column=0,columnspan=2,pady=5)

        usuarioLogin_label = tk.Label(self.loginTela,text="Usuario:",font=('Helvetica bold',16),bg='black',fg='white')
        usuarioLogin_label.grid(row=3, column=0,sticky='w')

        senha_label = tk.Label(self.loginTela,text="Senha:",font=('Helvetica bold',16),bg='black',fg='white')
        senha_label.grid(row=4,column=0,sticky='w')

        naoTem = tk.Label(self.loginTela,text="Não possui conta?",bg='black',fg='white',font=('Helvetica bold',10))
        naoTem.grid(row=6,column=0)

        self.alertaLogin = tk.Label(self.loginTela,text="PREENCHA TODOS OS CAMPOS OBRIGATORIOS!",fg='red',bg='black',font=('Helvetica bold',8))

        self.alertaCredenciais = tk.Label(self.loginTela,text="CREDENCIAIS INCORRETAS!",fg='red',bg='black',font=('Helvetica bold',8))

        #Entries
        self.senha_entry = tk.Entry(self.loginTela,show="*")
        self.senha_entry.grid(row=4,column=1)

        self.usuario_entry = tk.Entry(self.loginTela)
        self.usuario_entry.grid(row=3,column=1)

        #Botões
        login_button = tk.Button(self.loginTela,text="Entrar",width=17,font=('Helvetica bold',16),bg='black',fg='white')
        login_button.grid(row=5,column=0,columnspan=2,pady=10)

        irRegistro_button = tk.Button(self.loginTela,text="Registrar-se",width=9,font=('Helvetica bold',10),bg='black',fg='white',command=self.switch)
        irRegistro_button.grid(row=6,column=1)
    
    def switch(self):
         self.loginAndRegisterScreens()

    def loginAndRegisterScreens(self):
        if self.register:
            print(self.register)
            self.telaRegistro.grid_forget()
            self.register = not self.register
            self.telaLogin()
        else:
            print(self.register)
            self.loginTela.grid_forget()
            self.register = not self.register
            self.telaDeRegistro()

View()

