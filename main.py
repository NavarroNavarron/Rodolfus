import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from pymongo import MongoClient
from ttkbootstrap.scrolled import ScrolledFrame



cluster = MongoClient("mongodb+srv://Navarro:NCyePt5ZjBtp9oZa@teste.heu8sh0.mongodb.net/?retryWrites=true&w=majority")
db = cluster["CadastroProcessos"]
collection = db["Processos"]

#Principal Janela
tela = tk.Tk()
tela.title("Registrar-se")
tela.config(bg='black',height=400,width=600,padx=20,pady=20)

relatorioTela = tk.Frame(tela,width=600,height=400,bg='gray')
relatorioTela.grid(row=1,column=0,columnspan=2,pady=10)

scrollTela = ScrolledFrame(tela,width=700,height=400,autohide=False)
scrollTela.grid(row=2,column=0,columnspan=3)

#Inicio
def main():
        telaProcessos()
        telaRelatorio()
        updateRelatorio()
        tela.mainloop()

#Tela de processos
def telaProcessos():
        #//Tela de cadastro
        processoTela = tk.Frame(tela,width=600,height=400,bg='black')
        processoTela.grid(row=0,column=0,columnspan=2)

        tituloProcesso_label = tk.Label(processoTela,text="Registro de Processos:",font=('Helvetica bold',22),bg='black',fg='white')
        tituloProcesso_label.grid(row=1,column=0,columnspan=2,pady=5)

        PID_label = tk.Label(processoTela,text="PID:",font=('Helvetica bold',16),bg='black',fg='white')
        PID_label.grid(row=2, column=0)

        UID_label = tk.Label(processoTela,text="UID:",font=('Helvetica bold',16),bg='black',fg='white')
        UID_label.grid(row=3,column=0)

        estado_label = tk.Label(processoTela,text="Estado:",font=('Helvetica bold',16),bg='black',fg='white')
        estado_label.grid(row=4,column=0)

        prioridade_label = tk.Label(processoTela,text="Prioridade:",font=('Helvetica bold',16),bg='black',fg='white')
        prioridade_label.grid(row=5,column=0)

        CPU_label = tk.Label(processoTela,text="Uso da CPU%:",font=('Helvetica bold',16),bg='black',fg='white')
        CPU_label.grid(row=6,column=0)

        memoria_label = tk.Label(processoTela,text="Uso da memória:",font=('Helvetica bold',16),bg='black',fg='white')
        memoria_label.grid(row=7,column=0)

        PID_entry = tk.Entry(processoTela,width=(23))
        PID_entry.grid(row=2,column=1,sticky='w')

        UID_entry = tk.Entry(processoTela,width=(23))
        UID_entry.grid(row=3,column=1,sticky='w')

        estado_combobox = ttk.Combobox(processoTela,width=20)
        estado_combobox['values'] = ["Pronto","Execução","Espera"]
        estado_combobox.grid(row=4,column=1,sticky='w')

        prioridade_combobox = ttk.Combobox(processoTela)
        prioridade_combobox['values'] = ["Alta","Média","Baixa"]
        prioridade_combobox.grid(row=5,column=1,sticky='w')

        CPU_entry = tk.Entry(processoTela,width=(23))
        CPU_entry.grid(row=6,column=1,sticky='w')
        
        memoria_entry = tk.Entry(processoTela,width=(23))
        memoria_entry.grid(row=7,column=1,sticky='w')

        cadastrar_button = tk.Button(processoTela,width=25,text="Cadastrar processo",bg='black',fg='white',command=lambda:([pegarCadastro(PID_entry.get(),UID_entry.get(),prioridade_combobox.get(),CPU_entry.get(),estado_combobox.get(),memoria_entry.get()),updateRelatorio()]))
        cadastrar_button.grid(row=8,column=0,columnspan=2,padx=5,pady=5)
        #Tela de Cadastro//

        


def telaRelatorio():
        #//Tela de relatorio
        pid_label = tk.Label(relatorioTela,text="Processo",font=('Helvetica bold',13),bg='gray',fg='white')
        pid_label.grid(row=0, column=0,padx=7)

        uid_label = tk.Label(relatorioTela,text="Usuário",font=('Helvetica bold',13),bg='gray',fg='white')
        uid_label.grid(row=0,column=1,padx=13)

        Estado_label = tk.Label(relatorioTela,text="Estado",font=('Helvetica bold',13),bg='gray',fg='white')
        Estado_label.grid(row=0,column=2,padx=15)

        Prioridade_label = tk.Label(relatorioTela,text="Prioridade",font=('Helvetica bold',13),bg='gray',fg='white')
        Prioridade_label.grid(row=0,column=3,padx=7)

        cpu_label = tk.Label(relatorioTela,text="CPU",font=('Helvetica bold',13),bg='gray',fg='white')
        cpu_label.grid(row=0,column=4,padx=10)

        Memoria_label = tk.Label(relatorioTela,text="Espaço na memória",font=('Helvetica bold',13),bg='gray',fg='white')
        Memoria_label.grid(row=0,column=5,padx=10)

        espaco_label = tk.Label(relatorioTela,text="Ação",font=('Helvetica bold',13),bg='gray',fg='white')
        espaco_label.grid(row=0,column=6,padx=10)     

        #Tela de relatorio//

        

def pegarCadastro(PID,UID,PRIO,CPU,ESTA,MEMO):
        
        PID = PID
        UID = UID
        PRIO = PRIO
        CPU = CPU
        ESTA = ESTA
        MEMO = MEMO
        relatorio = {"Processo": PID, 
                     "Usuario": UID,
                     "Estado": ESTA,
                     "Prioridade": PRIO,
                     "Uso da CPU": CPU,
                     "Espaço na Memoria": MEMO}
        print(relatorio)

        collection.insert_one(relatorio)

def updateRelatorio():
        for widget in scrollTela.winfo_children():
            widget.grid_forget()

        telaRelatorio()

        processos = []
        usuarios = []
        estados = []
        prioridades = []
        cpus = []
        memorias = []


        result = collection.find({"Processo":{"$exists":True}})
        for results in result:
            processos.append(results["Processo"])
            usuarios.append(results["Usuario"])
            estados.append(results["Estado"])
            prioridades.append(results["Prioridade"])
            cpus.append(results["Uso da CPU"])
            memorias.append(results["Espaço na Memoria"])

        for i in range(len(processos)):
                processo = tk.Label(scrollTela,text=processos[i],font=('Helvetica bold',13),bg='gray',fg='white')
                processo.grid(row=i+1,column=0,pady=5,padx=15)
                usuario = tk.Label(scrollTela,text=usuarios[i],font=('Helvetica bold',13),bg='gray',fg='white')
                usuario.grid(row=i+1,column=1,pady=5,padx=17)
                estado = tk.Label(scrollTela,text=estados[i],font=('Helvetica bold',13),bg='gray',fg='white')
                estado.grid(row=i+1,column=2,pady=5,padx=11)
                prioridade = tk.Label(scrollTela,text=prioridades[i],font=('Helvetica bold',13),bg='gray',fg='white')
                prioridade.grid(row=i+1,column=3,pady=5,padx=18)
                cpu = tk.Label(scrollTela,text=cpus[i],font=('Helvetica bold',13),bg='gray',fg='white')
                cpu.grid(row=i+1,column=4,pady=5,padx=24)
                memoria = tk.Label(scrollTela,text=memorias[i],font=('Helvetica bold',13),bg='gray',fg='white')
                memoria.grid(row=i+1,column=5,pady=5,padx=45)
                deletar = tk.Button(scrollTela,text="Deletar",font=('Helvetica bold',13),bg='gray',fg='white',command=lambda id = i: rowID(id))
                deletar.grid(row=i+1,column=6,pady=5,padx=20)
        return processos
        

def rowID(id):
    processos = updateRelatorio()
    item = str(processos[id])
    delete(item)

def delete(item):
       collection.delete_one({"Processo": item})
       updateRelatorio()

main()