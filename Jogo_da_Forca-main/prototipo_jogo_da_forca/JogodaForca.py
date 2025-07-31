#classe Jogo da Forca
import random
from Palavra_Secreta import PalavraSecreta

class JogodaForca:
    def __init__(self):
        self.temas = {
            "Cores":["Rosa", "Roxo", "Azul", "Preto", "Vermelho"],
            "Animais":["Gato", "Cachorro", "Vaca", "Carneiro", "Ovelha"],
            "Frutas":["Banana","Maçã", "Morango", "Abacaxi", "Uva"],
            "Conceitos de Programação":["Variável", "Função", "Classe", "Objeto", "Herança", "Poliformismo"],
        }