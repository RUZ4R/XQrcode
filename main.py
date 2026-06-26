import qrcode 
from qrcode.image.styledpil import StyledPilImage
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

# Criado por Endrio dos Santos

def caminho_logo():
    caminho_entry.delete(0, "end")
    caminho_arquivo = filedialog.askopenfilename(
    title="Selecione um arquivo",
    filetypes=(("Arquivos de Texto", "*.png"), ("Todos os Arquivos", "*.*")))
    caminho_entry.insert(0,caminho_arquivo)

def salvar_onde():
    salvar_entry.delete(0, "end") 
    caminho_salvar = filedialog.askdirectory(title="Selecione a Pasta")
    salvar_entry.insert(index=0, string=caminho_salvar)

def gerar_sem_logo():
    link = url_entry.get()
    imagem = qrcode.make(link)
    caminho = salvar_entry.get()
    if os.path.isdir(caminho):
        imagem.save(f"{caminho}/qrcode.png")
        messagebox.showinfo("QRcode", "Feito!") 
    else:
        messagebox.showinfo("Aviso", "Selecione a pasta onde quer salvar!!!")

def gerar_logo():
    caminho = salvar_entry.get()
    link = url_entry.get()
    img = caminho_entry.get()
    if img != "":
        if os.path.isdir(caminho):
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)  # para poder adicionar uma imagem
            qr.add_data(link)
            imagem = qr.make_image(
                image_factory=StyledPilImage,
                embeded_image_path=img,)

            imagem.save(f"{caminho}/qrcode_logo.png")
            messagebox.showinfo("QRcode", "Feito!")  
        else:
            messagebox.showinfo("Aviso", "Selecione a pasta onde está sua logo!!!")
    else:
        messagebox.showinfo("Aviso", "Selecione a logo que deseja usar!!!")


#CONFIGURANDO A JANELA
janela = ctk.CTk()
janela.geometry("700x280")
janela.resizable(False, False)
janela.title("Gerador de QRcode   v.1.2")
janela._set_appearance_mode('light')
janela.configure(fg_color="#818181")

#TEXTOS
caminho_text = ctk.CTkLabel(janela, text='Caminho para Logo:', bg_color='transparent', text_color="#0a0a0a",
                           font=('arial black', 12)).place(x=50, y=17)

salvar_text = ctk.CTkLabel(janela, text='Caminho para salvar:', bg_color='transparent', text_color="#0a0a0a",
                        font=('arial black', 12)).place(x=50, y=77)

url_text = ctk.CTkLabel(janela, text='Url:', bg_color='transparent', text_color="#0a0a0a",
                        font=('arial black', 12)).place(x=50, y=137)

assinatura_text = ctk.CTkLabel(janela, text='Endrio S.', bg_color='transparent', text_color="#0a0a0a",
                        font=('arial black', 10)).place(x=640, y=260)

#CAIXAS DE ENTRADA
caminho_entry = ctk.CTkEntry(janela, bg_color="transparent", width=450, height=30, corner_radius=5, fg_color="#ffffff", border_color="#0a0a0a", text_color="#0a0a0a")
caminho_entry.place(x=50, y=40 )

salvar_entry = ctk.CTkEntry(janela, bg_color="transparent", width=450, height=30, corner_radius=5, fg_color="#ffffff", border_color="#0a0a0a", text_color="#0a0a0a")
salvar_entry.place(x=50, y=100 )

url_entry  = ctk.CTkEntry(janela, bg_color='transparent', width=450, height=30, corner_radius=5, fg_color="#ffffff", border_color="#0a0a0a", text_color="#0a0a0a")
url_entry.place(x=50, y=160)

#BOTOES
start_buton_logo = ctk.CTkButton(janela, text='COM LOGO', bg_color='transparent', fg_color="#1E634C", border_width=2, border_color="#ffffff",
                              font=('arial black', 14), width=100, height=30,
                              command=gerar_logo, corner_radius=5).place(x=50, y=200)

start_buton = ctk.CTkButton(janela, text='SIMPLES', bg_color='transparent', fg_color="#1E634C", border_width=2, border_color="#ffffff",
                              font=('arial black', 14), width=100, height=30,
                              command=gerar_sem_logo, corner_radius=5).place(x=160, y=200)

caminho_buton = ctk.CTkButton(janela, text='PROCURAR', bg_color='transparent', fg_color="#1E634C", border_width=2, border_color="#ffffff",
                              font=('arial black', 14), width=100, height=30,
                              command=caminho_logo, corner_radius=5).place(x=515, y=40)

salvar_buton = ctk.CTkButton(janela, text='SALVAR', bg_color='transparent', fg_color="#1E634C", border_width=2, border_color="#ffffff",
                              font=('arial black', 14), width=100, height=30,
                              command=salvar_onde, corner_radius=5).place(x=515, y=100)


#INICIANDO A JANELA
janela.mainloop()
