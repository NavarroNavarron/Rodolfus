import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient



class View():

    cluster = MongoClient("mongodb+srv://Navarro:NCyePt5ZjBtp9oZa@teste.heu8sh0.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["CadastroProcessos"]
    collection = db["Processos"]

    #Principal Janela
    tela = tk.Tk()
    tela.title("Registrar-se")
    tela.config(bg='black',height=400,width=600,padx=20,pady=20)

    register = True

    #Inicio
    def __init__(self):
        self.telaProcessos()
        self.telaRelatorio()
        self.tela.mainloop()

    #Tela de processos
    def telaProcessos(self):
        #//Tela de cadastro
        self.processoTela = tk.Frame(self.tela,width=600,height=400,bg='black')
        self.processoTela.grid(row=0,column=0,columnspan=2)

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

        self.cadastrar_button = tk.Button(self.processoTela,width=25,text="Cadastrar processo",bg='black',fg='white',command=lambda:([self.pegarCadastro(self.PID_entry.get(),self.UID_entry.get(),self.prioridade_combobox.get(),self.CPU_entry.get(),self.estado_combobox.get(),self.memoria_entry.get()),self.updateRelatorio()]))
        self.cadastrar_button.grid(row=8,column=0,columnspan=2,padx=5,pady=5)

        mostrarButton = tk.Button(self.processoTela,width=25,text="Mostrar Processos",bg='black',fg='white',command=self.updateRelatorio)
        mostrarButton.grid(row=9,column=0,columnspan=2,padx=5,pady=5)
        #Tela de Cadastro//

        


    def telaRelatorio(self):
        #//Tela de relatorio
        self.relatorioTela = tk.Frame(self.tela,width=600,height=400,bg='gray')
        self.relatorioTela.grid(row=1,column=0,columnspan=2,pady=10)

        pid_label = tk.Label(self.relatorioTela,text="Processo",font=('Helvetica bold',13),bg='gray',fg='white')
        pid_label.grid(row=0, column=0,padx=10)

        uid_label = tk.Label(self.relatorioTela,text="Usuário",font=('Helvetica bold',13),bg='gray',fg='white')
        uid_label.grid(row=0,column=1,padx=10)

        Estado_label = tk.Label(self.relatorioTela,text="Estado",font=('Helvetica bold',13),bg='gray',fg='white')
        Estado_label.grid(row=0,column=2,padx=10)

        Prioridade_label = tk.Label(self.relatorioTela,text="Prioridade",font=('Helvetica bold',13),bg='gray',fg='white')
        Prioridade_label.grid(row=0,column=3,padx=10)

        cpu_label = tk.Label(self.relatorioTela,text="CPU",font=('Helvetica bold',13),bg='gray',fg='white')
        cpu_label.grid(row=0,column=4,padx=10)

        Memoria_label = tk.Label(self.relatorioTela,text="Espaço na memória",font=('Helvetica bold',13),bg='gray',fg='white')
        Memoria_label.grid(row=0,column=5,padx=10)     
        #Tela de relatorio//

        

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

    def updateRelatorio(self):
        for widget in self.relatorioTela.winfo_children():
            widget.grid_forget()

        self.telaRelatorio()

        processos = []
        usuarios = []
        estados = []
        prioridades = []
        cpus = []
        memorias = []
        self.deletars = []


        result = self.collection.find({"Processo":{"$exists":True}})
        for results in result:
            processos.append(results["Processo"])
            usuarios.append(results["Usuario"])
            estados.append(results["Estado"])
            prioridades.append(results["Prioridade"])
            cpus.append(results["Uso da CPU"])
            memorias.append(results["Espaço na Memoria"])

        for i in range(len(processos)):
                processo = tk.Label(self.relatorioTela,text=processos[i],font=('Helvetica bold',10),bg='gray',fg='white')
                processo.grid(row=i+1,column=0)
                usuario = tk.Label(self.relatorioTela,text=usuarios[i],font=('Helvetica bold',10),bg='gray',fg='white')
                usuario.grid(row=i+1,column=1)
                estado = tk.Label(self.relatorioTela,text=estados[i],font=('Helvetica bold',10),bg='gray',fg='white')
                estado.grid(row=i+1,column=2)
                prioridade = tk.Label(self.relatorioTela,text=prioridades[i],font=('Helvetica bold',10),bg='gray',fg='white')
                prioridade.grid(row=i+1,column=3)
                cpu = tk.Label(self.relatorioTela,text=cpus[i],font=('Helvetica bold',10),bg='gray',fg='white')
                cpu.grid(row=i+1,column=4)
                memoria = tk.Label(self.relatorioTela,text=memorias[i],font=('Helvetica bold',10),bg='gray',fg='white')
                memoria.grid(row=i+1,column=5)
                self.deletar = tk.Button(self.relatorioTela,text="Deletar",font=('Helvetica bold',10),bg='gray',fg='white')
                self.deletar.grid(row=i+1,column=6)
                self.deletars.append(self.deletar)
                print(self.deletars)
        self.test()

    def test(self):
        for i in range(len(self.deletars)):
            self.deletars[i].configure(command=lambda c=i: self.number(c))
            print(i)


    def number(self,number):
        print(number)

    def inserir(self):
        self.collection.insert_one(self.relatorio)



View()
