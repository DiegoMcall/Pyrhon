import customtkinter as ctk

def calcular():
    re1=float(receita1.get())
    re2=float(receita2.get())
    de1=float(despesas1.get())
    de2=float(despesas2.get())
    de3=float(despesas3.get())
    de4=float(despesas4.get())
    
    total = (re1+re2) - (de1 + de2 + de3 + de4)
    
    Resultado.configure(text=f"Sr(a) total do seu orçamento foi R${total:.2f}")
    


janela = ctk.CTk()
janela.geometry('500x550')
janela.title('Sistemas de Finanças')

ctk.CTkLabel(janela, text='Orçamento Financeiro', text_color='darkred', font=('Arial', 20, 'bold')).pack(pady=10)

receita1 = ctk.CTkEntry(janela, placeholder_text='Digite a 1° receita', text_color='green', width=250, height=40)
receita1.pack(pady=10)

receita2 = ctk.CTkEntry(janela, placeholder_text='Digite a 2° receita', text_color='green', width=250, height=40)
receita2.pack(pady=10)

despesas1 = ctk.CTkEntry(janela, placeholder_text='Digite a 1° despesa', text_color='green', width=250, height=40)
despesas1.pack(pady=10)

despesas2 = ctk.CTkEntry(janela, placeholder_text='Digite a 2° despesa', text_color='green', width=250, height=40)
despesas2.pack(pady=10)

despesas3 = ctk.CTkEntry(janela, placeholder_text='Digite a 3° despesa', text_color='green', width=250, height=40)
despesas3.pack(pady=10)

despesas4 = ctk.CTkEntry(janela, placeholder_text='Digite a 4° despesa', text_color='green', width=250, height=40)
despesas4.pack(pady=10)

Calcular = ctk.CTkButton(janela,text='Calcular', width=90, height=25, fg_color='darkblue', command=calcular)
Calcular.pack(pady=10)

Resultado = ctk.CTkLabel(janela, text='', font=('Italic', 17, 'bold'))
Resultado.pack(pady=20)

janela.mainloop()