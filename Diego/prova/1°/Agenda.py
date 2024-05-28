import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

def add():
    nomes=nome.get()
    numeros=numero.get()
    emails=email.get()
    if nomes or numeros or email:
        contatos = f"{nomes} | {numeros} | {emails}"
        
        lista_de_contatos.insert(0, contatos)
        salvar_contatos()
    else:
        messagebox.showerror('Erro', 'Complete todos os campos!')

def delete():
    dContato = lista_de_contatos.curselection()
    if dContato:
         lista_de_contatos.delete(dContato)
         salvar_contatos()
    else:
        messagebox.showerror('Erro no App', 'Selecione uma tarefa na lista!')      
        
def salvar_contatos():
    with open('contatos.txt', 'w') as t:
        tarefas = lista_de_contatos.get(0, END)
        
        for x in tarefas:
            t.write(x +'\n')
            
def carregar_contatos():
    try:
        with open('contatos.txt', 'r') as c:
            contatos = c.readlines()
            for x in contatos:
                lista_de_contatos.insert(0, x.strip())
    except:
        messagebox.showerror('Erro', 'Não foi possivel carregar os contatos!')
        

janela = ctk.CTk()
janela.geometry('500x550')
janela.title('Agenda de contatos')

ctk.CTkLabel(janela, text='Adicione um contato', text_color='green', font=('Arial', 20, 'bold')).pack(pady=10)

nome = ctk.CTkEntry(janela, placeholder_text='Digite o nome', text_color='green', width=250, height=40)
nome.pack(pady=10)

numero = ctk.CTkEntry(janela, placeholder_text='Digite o número', text_color='green', width=250, height=40)
numero.pack(pady=10)

email = ctk.CTkEntry(janela, placeholder_text='Digite o e-mail', text_color='green', width=250, height=40)
email.pack(pady=10)

AddButon = ctk.CTkButton(janela,text='Adicionar', width=90, height=25, fg_color='darkblue',command=add)
AddButon.place(x=120, y=257)

ExButon = ctk.CTkButton(janela,text='Excluir', width=90, height=25, fg_color='darkred', command=delete)
ExButon.place(x=280, y=257)

lista_de_contatos = Listbox(janela, width=37, height=25, font=('Verdana', 12))
lista_de_contatos.pack(pady=70)

carregar_contatos()
janela.mainloop()