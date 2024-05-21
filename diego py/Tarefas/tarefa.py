import customtkinter as ctk
import os 
import tkinter
from tkinter import *
from tkinter import messagebox

ctk.set_appearance_mode('dark')

# Funções
def adicionar():
    tarefa = nova_tarefa.get()
    if tarefa:
        lista_tarefas.insert(0,tarefa)
        nova_tarefa.delete(0,END)
        salvar_tarefas()
    else:
        messagebox.showerror('Erro no APP', 'Digite uma tarefa!')
        
def deletar():
    dTarefa = lista_tarefas.curselection()
    if dTarefa:
         lista_tarefas.delete(dTarefa)
         salvar_tarefas()
    else:
        messagebox.showerror('Erro no App', 'Selecione uma tarefa na lista!')
        
def salvar_tarefas():
    with open('tarefas.txt', 'w') as t:
        tarefas = lista_tarefas.get(0, END)
        
        for x in tarefas:
            t.write(x +'\n')
            
def carregar_tarefas():
 try:
   with open('tarefas.txt', 'r') as t:
        tarefas = t.readlines()
        
        for x in tarefas:
            lista_tarefas.insert(0,x.strip())
 except:
    messagebox.showerror('Erro no APP', 'Não foi possivel carregar as tarefas!')
#----------------------

# Lista de cores e fonte

cor1 = '#00FF7F'
cor2 = '#32CD32'
cor3 = '#DC143C'

font1 = ('Arial', 30,'bold')
font2 = ('Arial', 18,'bold')
font3 = ('Arial', 14,'bold')

#-----------------------
janela = ctk.CTk()
janela.geometry('300x480')
janela.title('App Tarefas V1.0')

ctk.CTkLabel(janela, text='App Tarefas', font=font1, text_color=cor1).pack(pady=10)

add_tarefas = ctk.CTkButton(janela, text='Adicionar Tarefas', fg_color='blue',
                             width=100, height=30, command=adicionar)
add_tarefas.place(x=20,y=90)

remover_tarefas = ctk.CTkButton(janela, text='Remover Tarefas', fg_color=cor3,
                             width=100, height=30, command=deletar)
remover_tarefas.place(x=180,y=90)

nova_tarefa = ctk.CTkEntry(janela, width=250, height=30,
                           placeholder_text='Digita uma nova tarefa')
nova_tarefa.pack(pady=100)

ctk.CTkLabel(janela, text='Tarefas pendentes', font=font2, text_color=cor2).place(x=70,y=200)

lista_tarefas = Listbox(janela, width=40, height=15)
lista_tarefas.place(x=31,y=230)

carregar_tarefas()
janela.mainloop()
