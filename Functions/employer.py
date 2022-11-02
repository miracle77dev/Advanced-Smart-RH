import sqlite3
class Employer():
    def __init__(self):
        self.Connexion = sqlite3.connect("./srh.db")
        self.Cursor = self.Connexion.cursor()

    def GetEmployerCategorieByMatricule(self, Matricule):
        Data = (Matricule,)
        Req = "SELECT Categorie FROM Employer WHERE Matricule = ?"
        self.Cursor.execute(Req, Data)
        try:
            return self.Cursor.fetchone()[0]
        except:
            ...

    def AddEmployer(self, Data):
        Req = "INSERT INTO Employer(Matricule,Categorie,Nom,Prenoms,Poste) VALUES(?,?,?,?,?)"
        self.Cursor.execute(Req, Data)
        self.Connexion.commit()
        return 0

    def GetNumberOfEmployer(self):
        Req = "SELECT COUNT(Id) FROM Employer"
        self.Cursor.execute(Req)
        return self.Cursor.fetchone()[0]

