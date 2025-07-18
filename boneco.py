class boneco():
    def __init__(self, erros):
        self.erros = erros
        self.bonecos=["""
    ________     
    |      |
    |      
    |     
    |     
        ""","""
    ________     
    |      |
    |      O
    |     
    |     
        ""","""
    ________     
    |      |
    |      O
    |      |
    |     
        ""","""
    ________     
    |      |
    |      O
    |     /|
    |     
        ""","""
    ________     
    |      |
    |      O
    |     /|\ 
    |     
        ""","""
    ________     
    |      |
    |      O
    |     /|\ 
    |     / 
        ""","""
    ________ 
    |      | 
    |      O 
    |     /|\ 
    |     / \ 
        """]

    def draw(self):
        print(self.bonecos[self.erros])


