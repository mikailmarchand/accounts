from abc import ABC

from .abstract_account import AbstractAccount


class CICAccount(AbstractAccount, ABC):
    
    def __init__(self):
        super(CICAccount, self).__init__(
            path="D:\\Mikail\\Papiers importants\\Comptes\\CIC\\",
            preheader = 1,
            bank="CIC",
            extension=".csv",
            delimiter=";"
        )

    def category_parsing(self, lib, cat):
        number_match = 0
        if "VIR C P A M" in lib:
            lib = "Remboursement Sécu"
            cat = self.TAGS["santé"]
            number_match += 1
        if "VIRT INTERESSEMENT" in lib:
            lib = "Intéressement Arkéa"
            cat = self.TAGS["salaire"]
            number_match += 1
        if "VIRT PARTICIPATION" in lib:
            lib = "Participation Arkéa"
            cat = self.TAGS["salaire"]
            number_match += 1
        if "PHARMACIE DES U" in lib:
            lib = "Pharmacie des universités"
            cat = self.TAGS["santé"]
            number_match += 1
        if "COUSSEAU CATHERINE" in lib:
            lib = "Paiement Maman"
            cat = self.TAGS["check"]
            number_match += 1
        if "MEDI" in lib:
            lib = "Paiement Medi"
            cat = self.TAGS["check"]
            number_match += 1
        if "PARENTS" in lib:
            lib = "Remboursement parents"
            cat = self.TAGS["check"]
            number_match += 1
        if "ARKADE" in lib:
            lib = "Salaire Arkéa"
            cat += self.TAGS["salaire"]
            number_match += 1
        if "DILAN" in lib:
            lib = "Remboursement Dilan"
            cat = "TODO : Check remboursement de quoi ?"
            number_match += 1
        if "PHIE NICOLAS" in lib:
            lib = "Pharmacie Nicolas"
            cat += self.TAGS["santé"]
            number_match += 1
        if "GEANT" in lib:
            lib = "Géant"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "FOURNIL DE PAULI" in lib:
            lib = "Fournil de Pauline (Boulangerie)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "DAB" in lib:
            lib = "DAB"
            cat += self.TAGS["dab"]
            number_match += 1
        if "DEMIRDELEN" in lib:
            lib = "Virement Mika"
            cat += self.TAGS["caché"]
            number_match += 1
        if "KEVIN BIARDEAU" in lib:
            lib = "TODO : Check catégorie Remboursement"
            cat += self.TAGS["check"]
            number_match += 1
        if "LE GOFF LENA" in lib:
            lib = "Paiement Léna : Check catégorie"
            cat += self.TAGS["check"]
            number_match += 1
        if "DILAN DEMIRDELEN" in lib:
            lib = "TODO : Check catégorie Remboursement"
            cat += self.TAGS["check"]
            number_match += 1
        if "DILAN DEMIRDELEN" in lib:
            lib = "TODO : Check catégorie Remboursement"
            cat += self.TAGS["check"]
            number_match += 1
        if "MARCHAND" in lib:
            lib = "Virement Maeliss"
            cat += self.TAGS["caché"]
            number_match += 1
        if "COMPTE COMMUN" in lib:
            lib = "Virement Compte Commun"
            cat += self.TAGS["caché"]
            number_match += 1
        if "PAYPAL" in lib:
            lib = "TODO : Paypal - check détails"
            number_match += 1
        if "CHEQUE" in lib:
            lib = "TODO : Chèque - check détails"
            number_match += 1
        if "POLE EMPLOI" in lib:
            lib = "Pole Emploi"
            cat += self.TAGS["salaire"]
            number_match += 1
        if "LA POSTE" in lib:
            lib = "La poste"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "ECH PRET" in lib:
            lib = "Prêt étudiant"
            cat += self.TAGS["banque"]
            number_match += 1
        if "F COTIS" in lib:
            lib = "Frais banque CIC"
            cat += self.TAGS["banque"]
            number_match += 1
        if "CARREFOUR" in lib:
            lib = "Carrefour"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "TI COOP" in lib:
            lib = "Ti Coop"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "INTERMARCHE" in lib:
            lib = "Intermarché"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LUDIK ADDICT" in lib:
            lib = "Ludik Addict"
            cat += self.TAGS["culture"]
            number_match += 1
        if "BIBUS" in lib:
            lib = "Bibus (bus Brest)"
            cat += self.TAGS["transport"]
            number_match += 1
        if "LUDIK ADDICT" in lib:
            lib = "Temple du jeu Brest"
            cat += self.TAGS["culture"]
            number_match += 1
        return lib, cat, number_match

    def split_date(self, date):
        j, m, a = date.split("/")
        return j, m, a

    def split_date_lib_eur(self, line, delimiter):
        date, date2, debit, credit, lib, solde = line.split(delimiter)
        if debit == "":
            debit = "0"
        if credit == "":
            credit = "0"
        debit = str(debit).replace(",", ".")
        credit = str(credit).replace(",", ".")
        eur = str(float(debit) + float(credit))
        return date, lib, eur, ""
