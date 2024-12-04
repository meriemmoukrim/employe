from datetime import date

class Employe:
    __auto = 0

    def __init__(self, nom, prenom, dateNaissance, dateEmbauche, salaireBase):
        Employe.__auto += 1
        self.__matricule = Employe.__auto
        self.__nom = nom
        self.__prenom = prenom
        self.__dateNaissance = dateNaissance
        self.__dateEmbauche = dateEmbauche
        self.__salaireBase = salaireBase

    @property
    def matricule(self):
        return self.__matricule

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nouvelleNom):
        self.__nom = nouvelleNom

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, nouvellePrenom):
        self.__prenom = nouvellePrenom

    @property
    def dateNaissance(self):
        return self.__dateNaissance

    @dateNaissance.setter
    def dateNaissance(self, nouvelleDateNaissance):
        if isinstance(nouvelleDateNaissance, date):
            self.__dateNaissance = nouvelleDateNaissance
        else:
            raise ValueError("Date de naissance invalide")

    def Age(self):
        today = date.today()
        age = today.year - self.__dateNaissance.year
        if today.month < self.__dateNaissance.month or (
                today.month == self.__dateNaissance.month and today.day < self.__dateNaissance.day):
            age -= 1
        return age

    @property
    def dateEmbauche(self):
        return self.__dateEmbauche

    @dateEmbauche.setter
    def dateEmbauche(self, nouvelleDateEmbauche):
        if isinstance(nouvelleDateEmbauche, date):
            if self.Age() < 16:
                raise ValueError("L'âge de l'employé doit être supérieur ou égal à 16 ans pour être embauché.")
            self.__dateEmbauche = nouvelleDateEmbauche
        else:
            raise ValueError("Date d'embauche invalide.")

    @property
    def salaireBase(self):
        return self.__salaireBase

    @salaireBase.setter
    def salaireBase(self, nouvelleSalaire):
        if nouvelleSalaire < 0:
            raise ValueError("Salaire ne peut pas être négatif")
        self.__salaireBase = nouvelleSalaire


class Manager(Employe):
    def __init__(self, nom, prenom, dateNaissance, dateEmbauche, salaireBase, prime):
        super().__init__(nom, prenom, dateNaissance, dateEmbauche, salaireBase)
        self.__prime = prime

    def salaireBrut(self):
        return self.salaireBase + self.__prime  # Using self.salaireBase


class Ouvrier(Employe):
    def __init__(self, nom, prenom, dateNaissance, dateEmbauche, salaireBase, heurSupp, tauxHoraire):
        super().__init__(nom, prenom, dateNaissance, dateEmbauche, salaireBase)
        self.__heurSupp = heurSupp
        self.__tauxHoraire = tauxHoraire

    def salaireBrut(self):
        return self.salaireBase + (self.__heurSupp * self.__tauxHoraire)  # Using self.salaireBase


class Temporaire(Employe):
    def __init__(self, nom, prenom, dateNaissance, dateEmbauche, nbHrTravaille, tauxHoraire=80):
        super().__init__(nom, prenom, dateNaissance, dateEmbauche, salaireBase=0)
        self.__nbHrTravaille = nbHrTravaille
        self.__tauxHoraire = tauxHoraire

    def salaireBrut(self):
        return self.salaireBase + (self.__tauxHoraire * self.__nbHrTravaille)






employe1 = Employe(nom="Dupont", prenom="Pierre", dateNaissance=date(1990, 5, 15),
                   dateEmbauche=date(2015, 3, 20), salaireBase=2000)

print(f"Matricule: {employe1.matricule}")
print(f"Nom: {employe1.nom}")
print(f"Prénom: {employe1.prenom}")
print(f"Age: {employe1.Age()}")
print(f"Salaire de base: {employe1.salaireBase}")

employe1.nom = "meriem"
print(f"Nom modifié: {employe1.nom}")


manager1 = Manager(nom="asmae", prenom="Sophie", dateNaissance=date(1985, 7, 30),
                   dateEmbauche=date(2012, 6, 5), salaireBase=3000, prime=500)

print(f"Matricule: {manager1.matricule}")
print(f"Salaire brut du manager: {manager1.salaireBrut()}")


ouvrier1 = Ouvrier(nom="med", prenom="anas", dateNaissance=date(1980, 8, 20),
                   dateEmbauche=date(2018, 1, 10), salaireBase=1500, heurSupp=10, tauxHoraire=25)

print(f"Matricule: {ouvrier1.matricule}")
print(f"Salaire brut de l'ouvrier: {ouvrier1.salaireBrut()}")

temporaire1 = Temporaire(nom="alya", prenom="aicha", dateNaissance=date(1992, 11, 22),
                         dateEmbauche=date(2024, 6, 15), nbHrTravaille=40, tauxHoraire=15)

print(f"Matricule: {temporaire1.matricule}")
print(f"Salaire brut du temporaire: {temporaire1.salaireBrut()}")
