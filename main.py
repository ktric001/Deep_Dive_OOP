import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about the bill, such as the total amount and the period of the bill.
    """
    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """
    def __init__(self, flatmate_name, days_in_house,):
        self.days_in_house = days_in_house
        self.flatmate_name = flatmate_name

    def pays(self, bill, flatmate_name):
        weight = self.days_in_house / (self.days_in_house + flatmate_name.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a PDF file that contains data about the flatmates such as their names, their due amounts,
    and the periods of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate_name, bill):

        flatmate1_pays = str(round(flatmate1.pays(bill=the_bill, flatmate_name=Mary), 2))
        flatmate2_pays = str(round(flatmate_name.pays(bill=the_bill, flatmate_name=john), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("house.png", w=30, h=30)
        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='INVOICE', border=1, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.flatmate_name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pays, border=0, ln=1)

        # Insert Period label and value
        pdf.cell(w=100, h=25, txt=flatmate_name.flatmate_name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pays, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


amount = float(input("Hey user, enter the bill amount"))
period = input(" What is the bill period? E.g. December 2020: ")
name1 = input(" What is your name? ")
days_in_house = int(input(f"How many days did {name1} stay in the house? "))
name2 = input("What is the name of any other flat mate?")
days_in_house_2 = int(input(f'How long did {name2} stay? '))

the_bill = Bill(amount=amount, period=period)
john = Flatmate(name1, days_in_house=days_in_house)
Mary = Flatmate(flatmate_name=name2, days_in_house=25)
print(f"{name1} pays: ", john.pays(bill=the_bill, flatmate_name=Mary))
print(f"{name2} Pays: ", Mary.pays(bill=the_bill, flatmate_name=john))

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.generate(flatmate1=john, flatmate_name=Mary, bill=the_bill)






