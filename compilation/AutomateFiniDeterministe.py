class Automate:
    def __init__(self):
        self.etats = []
        self.etatInitial = 0
        self.etatsFinaux = [] 
        self.symboles = []
        self.tableTransition = []

    def getEtats(self):
        return self.etats

    def setEtats(self, x):
        for i in range(x):
            e = int(input(f'Etat {i}: '))
            while e in self.etats:
                e = int(input('Etat invalide car deja present donnez un autre: '))
            self.etats.append(e)
        
    def getEtatInitial(self):
        return self.etatInitial

    def setEtatInitial(self, x):
        if x in self.etats:
            self.etatInitial = x
        else:
            print(f'{x} n est pas dans les etats l etat initial par defaut est le premier etat')
            self.etatInitial = self.etats[0]

    def getEtatsFinaux(self):
        return self.etatsFinaux

    def setEtatsFinaux(self, x):
        for i in range(x):
            e = int(input(f'Etat final {i}: '))
            while e not in self.etats:
                e = int(input('Etat final invalid reprenez: '))
            self.etatsFinaux.append(e)
   
    def getSymboles(self):
        return self.symboles

    def setSymboles(self, x):
        self.symboles = []
        for i in range(x):
            symbole = input(f'Symbole {i}: ')
            while not symbole.isalpha():
                print('Seules les lettres sont acceptees')
                symbole = input(f'Symbole {i}: ')
            self.symboles.append(symbole)

    def getTableTransition(self):
        a = input(" 'oui' pour afficher la table de transition sinon la retourner tout simplement ") 
        if a == 'oui':
            print(f'\t {self.symboles}')
            for i, etat in enumerate(self.etats):   # give each element of self.etats and it position
                print(f'{self.etats[i]}\t  {self.tableTransition[i]}')
        else:
            return self.tableTransition

    def setTableTransition(self):
        self.tableTransition = [[0] * len(self.symboles) for _ in range(len(self.etats))]
        for i in range(len(self.etats)):
            for j, symbole in enumerate(self.symboles):
                e = int(input(f'Transition de l\'état {self.etats[i]} sur le symbole {symbole}: '))
                while e not in self.etats:
                    e = int(input('Etat final invalide reprenez: '))
                self.tableTransition[i][j] = e