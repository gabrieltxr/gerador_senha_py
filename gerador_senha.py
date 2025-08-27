#GERADOR DE SENHA
#SIMPLES APLICACAO
#PROJETO EM PYTHON E UI TKINTER



import random
import string
import tkinter as tk
from tkinter import messagebox

def gerar_senha(tamanho=12):
    #caracteres = string.ascii_letters + string.digits + string.punctuation

    #senha = ''.join(random.choice(caracteres) for _ in range (tamanho))
    #return senha
    tamanho = int(entry_tamanho.get())

    caracteres = ""
    if var_letras.get():
        caracteres += string.ascii_letters
    if var_numeros.get():
        caracteres += string.digits
    if var_simbolos.get():
        caracteres += string.punctuation
    
    if not caracteres:
        messagebox.showerror("Erro!, Selecione pelo menos uma opção")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, senha)

def copiar_senha():
    senha = entry_resultado.get()
    if senha:
        root.clipboard_clear()
        root.clipboard_append(senha)
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar.")

root = tk.Tk()
root.title("Gerador de senhas")
root.geometry("350x250")

tk.Label(root, text="Tamanho da senha: ").pack()
entry_tamanho = tk.Entry(root)
entry_tamanho.insert(0,"12")
entry_tamanho.pack()

var_letras = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Letras", variable=var_letras).pack()
tk.Checkbutton(root, text="Números", variable=var_numeros).pack()
tk.Checkbutton(root, text="Símbolos", variable=var_simbolos).pack()

tk.Button(root, text="Gerar senha", command=gerar_senha).pack(pady=10)
tk.Button(root, text="Copiar Senha", command=copiar_senha).pack(pady=5)

entry_resultado = tk.Entry(root, width=30)
entry_resultado.pack()

root.mainloop()
