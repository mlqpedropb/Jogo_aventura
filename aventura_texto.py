import random
import tkinter as tk
from tkinter import messagebox


class JogoAventura:
    def __init__(self, root):
        self.root = root
        self.root.title("Aventura em Texto")
        self.localizacao = "floresta"
        self.inventario = []
        
        self.criar_interface()

    def criar_interface(self):
        # Texto do jogo
        self.texto = tk.Text(self.root, wrap="word", height=15, width=50, state="disabled")
        self.texto.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Caixa de entrada
        self.entrada = tk.Entry(self.root, width=40)
        self.entrada.grid(row=1, column=0, padx=10, pady=10)

        # Botão de enviar
        self.botao_enviar = tk.Button(self.root, text="Enviar", command=self.processar_comando)
        self.botao_enviar.grid(row=1, column=1, padx=10, pady=10)

        # Botão de inventário
        self.botao_inventario = tk.Button(self.root, text="Inventário", command=self.mostrar_inventario)
        self.botao_inventario.grid(row=2, column=0, columnspan=2, pady=10)

        # Mensagem inicial
        self.mostrar_mensagem("Bem-vindo à Aventura em Texto!")
        self.mostrar_mensagem("Você está em uma floresta escura. Use os comandos norte, sul, leste ou oeste.")

    def mostrar_mensagem(self, mensagem):
        self.texto.config(state="normal")
        self.texto.insert("end", f"{mensagem}\n")
        self.texto.config(state="disabled")
        self.texto.see("end")

    def mostrar_inventario(self):
        if self.inventario:
            itens = "\n".join(self.inventario)
            messagebox.showinfo("Inventário", f"Seus itens:\n{itens}")
        else:
            messagebox.showinfo("Inventário", "Seu inventário está vazio.")

    def processar_comando(self):
        comando = self.entrada.get().lower()
        self.entrada.delete(0, "end")

        if comando == "sair":
            self.mostrar_mensagem("Obrigado por jogar!")
            self.root.quit()
        elif comando in ["norte", "sul", "leste", "oeste"]:
            self.localizacao, self.inventario = self.executar_comando(comando, self.localizacao, self.inventario)
        else:
            self.mostrar_mensagem("Comando inválido. Tente novamente.")

    def executar_comando(self, comando, localizacao, inventario):
        if comando == "norte":
            if localizacao == "floresta":
                localizacao = "cabana"
                self.mostrar_mensagem("Você encontra uma cabana abandonada.")
            elif localizacao == "rio" and "chave" in inventario:
                self.mostrar_mensagem("Você atravessa o rio e encontra o tesouro! Parabéns!")
                self.root.quit()
            else:
                self.mostrar_mensagem("Você não pode ir para o norte daqui.")
        elif comando == "leste":
            if localizacao == "floresta":
                self.mostrar_mensagem("Você encontra um rio de águas turbulentas.")
                if self.combate():
                    self.mostrar_mensagem("Você venceu o combate e pode seguir em frente!")
                else:
                    self.mostrar_mensagem("Você perdeu o combate e o jogo acabou!")
                    self.root.quit()
            else:
                self.mostrar_mensagem("Você não pode ir para o leste daqui.")
        elif comando == "sul":
            self.mostrar_mensagem("Você não pode ir para o sul daqui.")
        elif comando == "oeste":
            if self.quebra_cabeca():
                self.mostrar_mensagem("Você resolveu o enigma e pode continuar!")
            else:
                self.mostrar_mensagem("Você falhou no enigma. Tente novamente.")
        return localizacao, inventario

    def combate(self):
        inimigo_vida = random.randint(5, 15)
        jogador_vida = random.randint(10, 20)

        while jogador_vida > 0 and inimigo_vida > 0:
            acao = random.choice(["atacar", "defender"])
            if acao == "atacar":
                dano = random.randint(2, 6)
                inimigo_vida -= dano
                jogador_vida -= random.randint(2, 5)
            elif acao == "defender":
                jogador_vida -= random.randint(1, 3)
            if inimigo_vida <= 0:
                return True
            if jogador_vida <= 0:
                return False

    def quebra_cabeca(self):
        resposta = messagebox.askquestion("Enigma", "Eu sou maior que Deus, mais mau que o Diabo. Os pobres me têm, os ricos me querem. Se você me comer, você morre. O que sou eu?")
        return resposta.lower() == "nada"


# Inicialização do jogo
root = tk.Tk()
jogo = JogoAventura(root)
root.mainloop()
