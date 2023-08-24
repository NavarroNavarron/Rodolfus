import tkinter as tk
from tkinter import ttk
import pymongo
from pymongo import MongoClient



class View():

    cluster = MongoClient("mongodb+srv://Navarro:NCyePt5ZjBtp9oZa@teste.heu8sh0.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["Teste"]
    collection = db["Teste"]

    #Principal Janela
    tela = tk.Tk()
    tela.title("Registrar-se")
    tela.config(bg='black',height=400,width=600,padx=20,pady=20)

    register = True

    #Inicio
    def __init__(self):
        self.telaProcessos()

    #Tela de processos
    def telaProcessos(self):
        self.processoTela = tk.Frame(self.tela,width=600,height=400,bg='black')
        self.processoTela.grid(row=0,column=0)

        tituloProcesso_label = tk.Label(self.processoTela,text="Registro de Processos:",font=('Helvetica bold',22),bg='black',fg='white')
        tituloProcesso_label.grid(row=1,column=0,columnspan=2,pady=5)

        PID_label = tk.Label(self.processoTela,text="PID:",font=('Helvetica bold',16),bg='black',fg='white')
        PID_label.grid(row=2, column=0)

        UID_label = tk.Label(self.processoTela,text="UID:",font=('Helvetica bold',16),bg='black',fg='white')
        UID_label.grid(row=3,column=0)

        estado_label = tk.Label(self.processoTela,text="Estado:",font=('Helvetica bold',16),bg='black',fg='white')
        estado_label.grid(row=4,column=0)

        prioridade_label = tk.Label(self.processoTela,text="Prioridade:",font=('Helvetica bold',16),bg='black',fg='white')
        prioridade_label.grid(row=5,column=0)

        CPU_label = tk.Label(self.processoTela,text="Uso da CPU%:",font=('Helvetica bold',16),bg='black',fg='white')
        CPU_label.grid(row=6,column=0)

        memoria_label = tk.Label(self.processoTela,text="Uso da memória:",font=('Helvetica bold',16),bg='black',fg='white')
        memoria_label.grid(row=7,column=0)

        self.PID_entry = tk.Entry(self.processoTela,width=23)
        self.PID_entry.grid(row=2,column=1,sticky='w')

        self.UID_entry = tk.Entry(self.processoTela,width=23)
        self.UID_entry.grid(row=3,column=1,sticky='w')

        self.estado_combobox = ttk.Combobox(self.processoTela)
        self.estado_combobox['values'] = ["Pronto","Execução","Espera"]
        self.estado_combobox.grid(row=4,column=1,sticky='w')

        self.prioridade_combobox = ttk.Combobox(self.processoTela)
        self.prioridade_combobox['values'] = ["Alta","Média","Baixa"]
        self.prioridade_combobox.grid(row=5,column=1,sticky='w')

        self.CPU_entry = tk.Entry(self.processoTela,width=23)
        self.CPU_entry.grid(row=6,column=1,sticky='w')
        
        self.memoria_entry = tk.Entry(self.processoTela,width=23)
        self.memoria_entry.grid(row=7,column=1,sticky='w')

        self.cadastrar_button = tk.Button(self.processoTela,width=20,text="Cadastrar",bg='black',fg='white',command=lambda:[self.pegarCadastro(self.PID_entry.get(),self.UID_entry.get(),self.prioridade_combobox.get(),self.CPU_entry.get(),self.estado_combobox.get(),self.memoria_entry.get())])
        self.cadastrar_button.grid(row=8,column=0,columnspan=2,padx=5,pady=5)

        self.tela.mainloop()

    def pegarCadastro(self,PID,UID,PRIO,CPU,ESTA,MEMO):
        
        PID = PID
        UID = UID
        PRIO = PRIO
        CPU = CPU
        ESTA = ESTA
        MEMO = MEMO
        self.relatorio = {"Processo": PID, 
                        "Usuario": UID,
                     "Estado": ESTA,
                     "Prioridade": PRIO,
                     "Uso da CPU": CPU,
                     "Espaço na Memoria": MEMO}
        print(self.relatorio)

        self.inserir()


    def inserir(self):
        self.collection.insert_one(self.relatorio)



View()
