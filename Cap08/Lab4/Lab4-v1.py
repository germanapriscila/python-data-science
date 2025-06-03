# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name 

# Funçao limpa tela
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')
    
# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Hangman: 

     # Método Construtor
    def __init__(self, word):
        self.word = word   
        self.wrong_letters = []
        self.pic_letters = []
     
	# Método para adivinhar a letra   
    def guess_letter(self, letter):
        if letter in self.word and letter not in self.pic_letters:
            self.pic_letters.append(letter)
        elif letter not in self.word and letter not in self.wrong_letters:
            self.wrong_letters.append(letter)
        else: 
            return False
        return True 

    # Método para não mostrar a letra no board
    def hide_word(self):
        rtn = ""

        for letter in self.word:
            if letter not in self.pic_letters: 
                rtn += "_, "
            else:
                rtn += letter
        return rtn

    # Método para verificar se o jogo terminou
    def hang_over(self):
        return self.hangman_won() or (len(self.wrong_letters))
    
    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' in self.hide_word():
            return True
        return False
  
    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):

        print(board[len(self.wrong_letters)])
        print("\nPalavra: " + self.hide_word())
        print("\nLetras erradas: ")

        for letra in self.wrong_letters:
            print(letra,)
        
        print()
        print("Letras corretas: ")

        for letra in self.pic_letters:
            print(letra,)
        
        print()

# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_word():

    # Lista de palavras para o jogo
    words = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolhe randomicamente uma palavra
    word = random.choice(words)
        
    return word


# Método Main - Execução do Programa
def main():
     
    limpa_tela()

    # Cria o objeto e seleciona uma palavra randomicamente     
    game = Hangman(rand_word())
     
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hang_over():

        #  Status do game
        game.print_game_status()
		
		# Recebe input do terminal
        user_input = input('\nDigite uma letra: ')
          
        # Verifica se a letra digitada faz parte da palavra
        game.guess_letter(user_input)
    
    game.print_game_status()

    if game.hangman_won():
        print("Parabéns, você venceu!")
    else:
        print("Você perdeu.")
        print("A palavra era:" + game.word)

# Executa o programa		
if __name__ == "__main__":
	main()