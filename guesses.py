from boneco import boneco

class guesses():
    def __init__(self,palavra):
        self.guesses = []
        self.original = palavra
        self.palavra = palavra
        self.tentativa = "_ " * len(palavra)
        self.erros = 0


    def guess(self):
        print("letras: ", ', '.join(self.guesses))
        boneco(self.erros).draw()
        print(self.tentativa)

        guess = input("Digite uma letra: ")

        if guess not in self.guesses:
            self.guesses.append(guess)
        else:
            print("Letra já foi")
            return self.tentativa

        if guess in self.palavra:
            print(f"A palavra tem {guess}! ")
            for letra in self.palavra:
                if letra == guess:
                    c=self.palavra.index(letra)
                    self.palavra=self.palavra.replace(letra,"*",1)
                    self.tentativa=self.tentativa[:c*2]+letra+self.tentativa[c*2+1:]
            return self.tentativa

        elif guess not in self.original:
            print(f"Não tem {guess} na palavra!" )
            self.erros+=1
            return self.tentativa

        
        