somme = 0
class CompteBancaire:
    def __init__(self, titulaire, numero_de_compte, solde):
        self.__titulaire = titulaire
        self.__numero_de_compte = numero_de_compte
        self.__solde = solde
        self.__historique = []
        
        
        
    def afficher_informations(self):
        print(f"Titulaire : {self.__titulaire}, Numéro de compte: {self.__numero_de_compte}, Solde: {self.__solde}€ ")
        print(" ")
    def deposer(self):
        solde = int(input("Saisissez le montant à deposer: "))
        if solde > 0:
           self.__solde += solde
        print(f"Votre compte a été crédité de: {solde}€") 
        print(f"Votre solde actuel est de: {self.__solde}€")
        print(" ")
        transaction = {"type": "dépot","valeur": self.__solde}
        self.__historique.append(transaction)
        
        
    def retirer(self):
        solde = int(input("Saisissez le montant à retirer: "))
        if self.__solde - solde >= 0:
            self.__solde -= solde
            print(f"Vous avez effectué un retrait de: {solde}€")
            print(f"Votre solde actuel est de: {self.__solde}€")
            print(" ")
            transaction = {"type": "retrait","valeur": self.__solde}
            self.__historique.append(transaction)
            
        else:
            print("solde insuffisant")
    def afficher_solde(self):
        print(f"Votre solde actuel est de {self.__solde}€")
        print(" ")
    def afficher_historique(self):
        print(self.__historique)
        print(" ")
comptes = {
    "Franco": CompteBancaire("Franco", "ABCD01", 0), 
    "Maria": CompteBancaire("Maria", "EFGH02", 0), 
    "Jean": CompteBancaire("Jean", "IJKL03", 0)
    }        
Franco = CompteBancaire("Franco", "ABCD01", 0)
Running = True
while Running:        
    
    print("Bienvenue à Open Banq IT.")
    print("1. Afficher les informations")
    print("2. Dépôt d'argent")
    print("3. Retirer de l'argent ")
    print("4. afficher le solde")
    print("5. Consulter l'historique")
    print("6. Quitter l'application")
    
    print(" ")
    action = int(input("Saisissez le numéro de l'action a éffectuer: "))
    print(" ")
    mon_compte = input("Entrez le nom du titulaire du compte: ")
    if mon_compte in comptes:
        compte_selectionne = comptes[mon_compte]
        if action == 1:
            compte_selectionne.afficher_informations()
        elif action == 2:
            compte_selectionne.deposer()
        elif action == 3:
            compte_selectionne.retirer()
        elif action == 4:
            compte_selectionne.afficher_solde()
        elif action == 5:
            compte_selectionne.afficher_historique()
        else:
            Running = False

     