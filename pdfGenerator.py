from fpdf import FPDF
import random,datetime,os
class PDF(FPDF):
    def header(self):
        self.image("Images/logo.png",10,3,50)
        self.set_font("helvetica","",18)
        self.cell(0,10,"POINTAGE DU 25 SEPT AU 26 OCT",ln=1,align="R")
        self.set_font("arial", "", 13)
        self.cell(0,8,"26/09/2022",align="R")
        self.ln(13)
        self.image("Images/barre.jpg",10,27,190)
        self.set_font("helvetica", "B", 15)
        pdf.cell(40, 10, "GROUPE SOGICI",ln=True)
        self.set_font("arial","", 12)
        pdf.cell(40, 7, "CI ABIDJAN YOP/ZI", ln=True)
        pdf.cell(40, 7, "01 BP3895 ABIDJAN 01", ln=True)
        self.ln(7)

    def body(self):
        pdf.set_auto_page_break(True, 20)
        pdf.add_page()
        Titre = ["MATRICULE", "HEURE D'ARRIVEE", "HEURE DE SORTIR", "DATE"]
        Body = [("5689", "08:44", "17:13", "22/08/2022"), ("95648", "08:44", "17:13", "22/08/2022"),
                ("19643", "08:44", "17:13", "22/08/2022")]

        pdf.set_draw_color(0, 0, 0)
        pdf.set_text_color(244, 119, 33)

        for i in Titre:
            pdf.cell(48, 10, i, border=True)
        pdf.ln(10)
        ii = 0

        pdf.set_text_color(0, 0, 0)
        for i in Body:
            for e in i:
                if ii == len(i) - 1:
                    pdf.cell(49, 10, e, ln=True)
                    ii = 0
                else:
                    pdf.cell(49, 10, e)
                    ii += 1

        pdf.output(str(datetime.date.today())+"_"+ str(random.randint(0,99999999))+".pdf","F")


    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica","I",10)
        self.cell(0,10,"La qualité, c'est notre affaire...",align="C")


pdf = PDF("p","mm","a4")
pdf.body()
