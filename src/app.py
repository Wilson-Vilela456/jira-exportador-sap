import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys

# Caminho do script principal
SCRIPT = os.path.join(os.path.dirname(__file__), "main.py")

def executar_script():
    try:
        resultado = subprocess.run(
            [sys.executable, SCRIPT],
            capture_output=True,
            text=True,
            check=True
        )
        messagebox.showinfo("Sucesso", "Exportação concluída com sucesso.")
    except subprocess.CalledProcessError as e:
        erro = e.stderr or e.stdout or "Erro desconhecido"
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar o script:\n\n{erro}")

# Criar janela
root = tk.Tk()
root.title("Exportador Jira")
root.geometry("300x150")
root.resizable(False, False)

# Elementos da interface
label = tk.Label(root, text="Clique abaixo para exportar os dados:")
label.pack(pady=20)

botao = tk.Button(root, text="Executar Exportação", command=executar_script, height=2, width=25)
botao.pack()

root.mainloop()
