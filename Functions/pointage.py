import sqlite3,pyglet
from datetime import date,datetime,timedelta

class Pointage():
    def __init__(self):
        self.Connexion = sqlite3.connect("./srh.db")
        self.Cursor = self.Connexion.cursor()
    def AlertSystem(self):
        #self.Alert = vlc.MediaPlayer("./song.mp3")
        #self.Alert.play()
        self.Alert = pyglet.resource.media("song.mp3")
        self.Alert.play()
        return 0

    def StopAlertSystem(self):
        self.Alert.stop()
        return 0

#_______ Methodes de pointage ______________#
    def Pointage(self,Matricule):
        Data = (date.today(),Matricule)
        Req = "UPDATE Employer SET DernierPointage = ? WHERE Matricule = ?"
        self.Cursor.execute(Req, Data)
        self.Connexion.commit()
        return 0

    def PointageJournalier1(self,Data):
        Req = "INSERT INTO P_Journalier(Nom,Matricule,Date,Heure) VALUES(?,?,?,?)"
        self.Cursor.execute(Req,Data)
        self.Connexion.commit()
        return 0

    def PointageJournalie2(self,Matricule):
        Data = (datetime.now().strftime("%H:%M:%S"),Matricule)
        Req = "UPDATE P_Journalier SET Heure2 = ? WHERE Matricule = ?"
        self.Cursor.execute(Req,Data)
        self.Connexion.commit()
        return 0

    def PointageHeure1(self,Data):
        Req = "INSERT INTO P_Heure(Nom,Matricule,Date,Heure) VALUES(?,?,?,?)"
        self.Cursor.execute(Req,Data)
        self.Connexion.commit()
        return 0

    def PointageHeure2(self,Matricule):
        Data = (datetime.now().strftime("%H:%M:%S"),Matricule)
        Req = "UPDATE P_Heure SET Heure2 = ? WHERE Matricule = ?"
        self.Cursor.execute(Req,Data)
        self.Connexion.commit()
        return 0

    def Synchronisation(self,Matricule,Type):
        Data = (Matricule,date.today())
        if Type == "E":
            Req = "SELECT Heure2,Heure FROM P_Journalier WHERE Matricule = ? AND Date = ?"
        elif Type == "O":
            Req = "SELECT Heure2,Heure FROM P_Heure WHERE Matricule = ? AND Date = ?"
        self.Cursor.execute(Req, Data)
        Heure = self.Cursor.fetchall()
        Heure2 = Heure[0][0]
        Heure1 = Heure[0][1]
        t = datetime.strptime(Heure2, '%H:%M:%S') - datetime.strptime(Heure1, '%H:%M:%S')

        #Tenir compte de la journée de Samedi
        dt = datetime.now()
        JourSemaine = dt.weekday()
        # Une heure de repos
        if JourSemaine != 5:
            Repos = "1:00:00"
            t = datetime.strptime(str(t), '%H:%M:%S') - datetime.strptime(Repos, '%H:%M:%S')

        t = datetime.strptime(str(t), '%H:%M:%S')
        t = self.ArrondiTemps(t)
        Temps = str(t).split(" ")[-1]
        Data2 = (Temps,Matricule,date.today())
        if Type == "E":
            Req2 = "UPDATE P_Journalier SET Temps = ? WHERE Matricule = ? AND Date = ?"
        elif Type == "O":
            Req2 = "UPDATE P_Heure SET Temps = ? WHERE Matricule = ? AND Date = ?"
        self.Cursor.execute(Req2, Data2)
        self.Connexion.commit()
        return 0


    def ArrondiTemps(self,t):
        return str((t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
                    + timedelta(hours=t.minute // 30))).split(" ")[-1]

    # _______ Fin des methodes de pointage ______________#

    def PointageHeure(self,Data):
        Req = "INSERT INTO P_Heure(Matricule,Date,Pointage1) VALUES(?,?,?)"
        self.Cursor.execute(Req,Data)
        self.Connexion.commit()
        return 0

    #Vérification du 2è pointage des employers
    def VerifyP2(self, Matricule):
        Data = (Matricule, date.today())
        Req = "SELECT Heure2 FROM P_Journalier WHERE Matricule = ? AND Date = ?"
        self.Cursor.execute(Req, Data)
        try:
            if len(self.Cursor.fetchone()[0]) > 2:
                return 1  # Déjà pointé
        except:
            return 0  # Pas encore pointé
    #Vérification du 2è pointage des ouvriers
    def VerifyH2(self,Matricule):
        Data = (Matricule, date.today())
        Req = "SELECT Heure2 FROM P_Heure WHERE Matricule = ? AND Date = ?"
        self.Cursor.execute(Req, Data)
        try:
            if len(self.Cursor.fetchone()[0]) > 2:
                return 1  # Déjà pointé
        except:
            return 0  # Pas encore pointé

    def GetHeureDeConnexionByMatricule(self,Matricule,Type):
        Data = (Matricule,date.today())
        if Type == "E":
            Req = "SELECT Date,Heure FROM P_Journalier WHERE Matricule = ? AND Date = ?"
        elif Type == "O":
            Req = "SELECT Date,Heure FROM P_Heure WHERE Matricule = ? AND Date = ?"
        self.Cursor.execute(Req,Data)
        try:
            if int(self.Cursor.fetchone()[1].split(":")[0]) < int(datetime.now().strftime("%H")):
                return 0 #Cette personne a déjà été pointé mais essaye de se faire pointer encore | On peut faire un deuxieme pointage quand on a la valeur 0
            else:
                return 1 #Cette personne a déjà été pointé le jour courant
        except:
            return 2 #Cette personne n'a pas été pointé le jour courant.

    def getPointageEmbauche(self):
        Data = (date.today(),)
        Req = "SELECT Matricule,Nom,Heure,Heure2,Date from P_Journalier WHERE Date = ?"
        self.Cursor.execute(Req, Data)
        return self.Cursor.fetchall()
    def getPointageOuvrier(self):
        Data = (date.today(),)
        Req = "SELECT Matricule,Nom,Heure,Heure2,Date from P_Heure WHERE Date = ?"
        self.Cursor.execute(Req,Data)
        return self.Cursor.fetchall()

    def getPointage(self):
        P = []
        for i in self.getPointageEmbauche():
            P.append(i)
        for e in self.getPointageOuvrier():
            P.append(e)
        return P

    def getPointageMoisCourantEmbauche(self):
        """Get courant mois pour employer"""
        Month = str(date.today()).split('-')
        del (Month[2])
        Month = "-".join(Month)+"%"
        Data = (Month,)
        Req = "SELECT Matricule,Nom,Heure,Heure2,Date from P_Journalier WHERE Date LIKE ? ORDER BY Date DESC"
        self.Cursor.execute(Req,Data)
        return self.Cursor.fetchall()

    def getPointageMoisCourantOuvrier(self):
        """Get courant mois pour ouvrier"""
        Month = str(date.today()).split('-')
        del (Month[2])
        Month = "-".join(Month) + "%"
        Data = (Month,)

        Req = "SELECT Matricule,Nom,Heure,Heure2,Date from P_Heure WHERE Date LIKE ? ORDER BY Date DESC"
        self.Cursor.execute(Req, Data)
        return self.Cursor.fetchall()


    def getPointagePersonnalise(self,Type,Data):
        """Get pointage personnalisé par l'utilisateur pour Employer"""
        if Type == "Employés":
            Req = "SELECT Matricule,Nom,Heure,Heure2,Date from P_Journalier WHERE date BETWEEN ? AND ? ORDER BY Date DESC"
        elif Type == "Ouvriers":
            Req = "SELECT Matricule,Nom,Heure,Heure2,Date from P_Heure WHERE date BETWEEN ? AND ? ORDER BY Date DESC"
        self.Cursor.execute(Req,Data)
        return self.Cursor.fetchall()


    def GeneratePointage(self,Table,Data):
        # - P_Heure
        # - P_Journalier
        if Table == "P_Journalier":
            Req = f"SELECT P_Journalier.Matricule,Employer.Nom,Employer.Prenoms,Employer.Poste,COUNT(P_Journalier.Id) AS Total from P_Journalier INNER JOIN Employer WHERE P_Journalier.Matricule=Employer.Matricule AND  P_Journalier.date BETWEEN ? AND ? GROUP BY Employer.Matricule"
        elif Table == "P_Heure":
            Req = f"SELECT P_Heure.Matricule,Employer.Nom,Employer.Prenoms,Employer.Poste,SUM(P_Heure.Temps) As Temps from P_Heure INNER JOIN Employer WHERE P_Heure.Matricule=Employer.Matricule AND P_Heure.date BETWEEN ? AND ? GROUP BY Employer.Matricule"
        self.Cursor.execute(Req, Data)
        return self.Cursor.fetchall()

    def getAbsentJourEnCours(self):
        Data = (date.today(),)
        Req = "SELECT Matricule,Nom,Prenoms from Employer WHERE DernierPointage != ? "
        self.Cursor.execute(Req,Data)
        return self.Cursor.fetchall()

    def JustifierAbsence(self,Type,Nom,Matricul,Date,Justification):
        if datetime.now().weekday() == 5:
            Temps = "05:00:00"
        else:
            Temps = "08:00:00"
        Temps = datetime.strptime(Temps, "%H:%M:%S")

        if Type == "E":
            Data = (Nom,Matricul,Date,Temps,Justification)
            Req = "INSERT INTO P_Journalier(Nom,Matricule,Date,Temps,Justification) VALUES(?,?,?,?,?)"
        else:
            Data = (Nom, Matricul, Date, Temps, Justification)
            Req = "INSERT INTO P_Heure(Nom,Matricule,Date,Temps,Justification) VALUES(?,?,?,?,?)"



# #
# P = Pointage()
# P = P.getAbsentJourEnCours()
# print(P)