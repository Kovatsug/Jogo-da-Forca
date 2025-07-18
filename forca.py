import random
from boneco import boneco
from guesses import guesses

class forca():
    def get_word(self):
        palavras = [
        "abacaxi", "abrigo", "alicate", "amigo", "amor", "anel", "areia", "arroz", "avião", "balança",
        "baleia", "banana", "banho", "barro", "beijo", "bicicleta", "bola", "bolacha", "borboleta", "brinco",
        "caderno", "café", "calça", "cama", "caminhão", "caneta", "carne", "castelo", "cavalo", "cebola",
        "celular", "céu", "chave", "chinelo", "chocolate", "chuva", "coelho", "coração", "cortina", "dente",
        "dedo", "desenho", "dragão", "escola", "escova", "espelho", "estrela", "fábrica", "faca", "fada",
        "feijão", "fogo", "formiga", "fruta", "galinha", "gato", "girassol", "girafa", "goleiro", "guarda-chuva",
        "helicóptero", "janela", "jardim", "joelho", "joia", "jornal", "leite", "lençol", "leão", "lápis",
        "livro", "lua", "maçã", "mala", "mão", "mar", "mesa", "milho", "mochila", "montanha",
        "navio", "nuvem", "óculos", "olho", "orelha", "ovo", "pão", "papel", "parque", "peixe",
        "pijama", "pipa", "pizza", "planta", "porta", "prato", "prego", "rainha", "relógio", "rosa"]

        palavra_index = random.choice(range(0, len(palavras)))
        palavra=palavras[palavra_index]
        return palavra

    def jogar(self):
        palavra_escolhida = self.get_word()
    
        print("Adivinhe a palavra!")
        tentativa = guesses(palavra_escolhida)

        while 1:
            resultado = tentativa.guess()
            if resultado.replace(" ", "") == palavra_escolhida:
                
                print("Parabéns! Você adivinhou a palavra!")
                print("A palavra era:", palavra_escolhida)
                break
            elif tentativa.erros >= 6:
                boneco(6).draw()
                print("Você perdeu! A palavra era:", palavra_escolhida)
                break

forca_game = forca()

while True:
    forca_game.jogar()
    dnv = input("Jogar novamente? S ou N: ")
    if dnv.lower()=="s":
        continue
    elif dnv.lower()=="n":
        print("Obrigado por jogar.\nDeus, Pátria e Família!!")
        break
    else:
        print("Opção inválida. Encerrando o jogo.")
        break
        

