from abc import ABC

from .abstract_account import AbstractAccount


class CMBAccount(AbstractAccount, ABC):
    
    def __init__(self):
        super(CMBAccount, self).__init__(
            path="CMB",
            preheader = 1,
            bank="CMB",
            extension=".csv",
            delimiter=";"
        )

    def category_parsing(self, lib, cat):
        number_match = 0
        """
        if "" in lib:
            lib = ""
            cat = self.TAGS["check"]
            number_match += 1
        """
        if "PayPal" in lib:
            lib = "PayPal"
            cat = self.TAGS["check"]
            number_match += 1
        if "WERO ELIE B" in lib:
            lib = "Wero Elie B"
            cat = self.TAGS["check"]
            number_match += 1
        if "GIFFARD" in lib:
            lib = "Giffard"
            cat = self.TAGS["bouffe"]
            number_match += 1
        if "NUVERSE" in lib:
            lib = "SNAP : boutique nuverse"
            cat = self.TAGS["snap"]
            number_match += 1
        if "Xsolla Untapped" in lib:
            lib = "Xsolla Untapped"
            cat = self.TAGS["culture"]
            number_match += 1
        elif "Xsolla" in lib:
            lib = "Xsolla (snap/google/mtga) ?"
            cat = self.TAGS["check"]
            number_match += 1
        if "Vinted" in lib:
            lib = "Vinted"
            cat = self.TAGS["culture"]
            number_match += 1
        if "COMITEO" in lib:
            lib = "Comiteo"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "VIR FF" in lib:
            lib = "Virement PEE"
            cat = self.TAGS["salaire"]
            number_match += 1
        if "VIR INST PAYPAL" in lib:
            lib = "Paypal : TODO"
            cat = self.TAGS["check"]
            number_match += 1
        if "PRLV Paypal (Europe)" in lib:
            lib = "Paypal : TODO"
            cat = self.TAGS["check"]
            number_match += 1
        if "PAPETERIE BREST" in lib:
            lib = "Bureau Vallee"
            cat = self.TAGS["matériel"]
            number_match += 1
        if "PRLV FOREVER" in lib:
            lib = "Forever : Assurance prêt"
            cat = self.TAGS["loyer"]
            number_match += 1
        if "BERTRAND MELANIE" in lib:
            lib = "Virement Lanie"
            cat = self.TAGS["check"]
            number_match += 1
        if "GENERATION" in lib:
            lib = "Mutuelle Génération"
            cat = self.TAGS["santé"]
            number_match += 1
        if "MC DONALDS BREST" in lib:
            lib = "Macdo"
            cat = self.TAGS["fastfood"]
            number_match += 1
        if "PayPal Europe" in lib:
            lib = "Paypal: TODO check"
            cat = self.TAGS["check"]
            number_match += 1
        if "MAXICOFFEE" in lib:
            lib = "Machine à café Arkéa"
            cat = self.TAGS["bouffe"]
            number_match += 1
        if "LE RELECQ KERH" in lib:
            lib = "Self Arkéa"
            cat = self.TAGS["bouffe"]
            number_match += 1
        if "TARTINES D AUTRE" in lib:
            lib = "Tartines d'autrefois"
            cat = self.TAGS["bouffe"]
            number_match += 1
        if "Nintendo" in lib:
            lib = "Nintendo"
            cat = self.TAGS["culture"]
            number_match += 1
        if "PHARMA MOULIN BL" in lib:
            lib = "Pharmacie Moulin Blanc"
            cat = self.TAGS["santé"]
            number_match += 1
        if "DEMIRDELEN DILAN" in lib:
            lib = "Virement Dilan"
            cat = self.TAGS["check"]
            number_match += 1
        if "COUSSEAU" in lib:
            lib = "Virement Steph"
            cat = self.TAGS["check"]
            number_match += 1
        if "BASIC FIT" in lib:
            lib = "Basic Fit"
            cat = self.TAGS["sport"]
            number_match += 1
        if "vers SYNDIC" in lib:
            lib = "Mensualité appel de fond Syndic"
            cat = self.TAGS["loyer"]
            number_match += 1
        if "ECH PRET 0750863842401" in lib:
            lib = "Echeance prêt principal"
            cat = self.TAGS["loyer"]
            number_match += 1
        if "ECH PRET 0743863842401" in lib:
            lib = "Echeance prêt taux zéro"
            cat = self.TAGS["loyer"]
            number_match += 1
        if "VIR INST vers SYNDIC" in lib:
            lib = "Paiement Syndic"
            cat = self.TAGS["loyer"]
            number_match += 1
        if "PRLV SURAVENIR ASSURANCES" in lib:
            lib = "Assurance habitation"
            cat = self.TAGS["loyer"]
            number_match += 1
        if "TI COOP BREST" in lib:
            lib = "Ti Coop"
            cat = self.TAGS["bouffe"]
            number_match += 1
        if "ALLO PIZZAS BRE BREST" in lib:
            lib = "Allo Pizza"
            cat = self.TAGS["fastfood"]
            number_match += 1
        if "VIR M MEDI DEMIRDELEN" in lib:
            lib = "Virement Medi à check"
            cat = self.TAGS["check"]
            number_match += 1
        if "VIR INST vers COMPTE COMMUN" in lib:
            lib = "Vers compte commun"
            cat = self.TAGS["caché"]
            number_match += 1
        if "MC DONALD'S BREST" in lib:
            lib = "Macdo Brest"
            cat = self.TAGS["fastfood"]
            number_match += 1
        if "ROADSIDE BREST" in lib:
            lib = "Roadside Brest"
            cat = self.TAGS["fastfood"]
            number_match += 1
        if "LE SALON DE SAB" in lib:
            lib = "La salon de Sabine"
            cat = self.TAGS["coiffure"]
            number_match += 1
        if "ORIJINAL PIDE BREST" in lib:
            lib = "Orijinal Pide"
            cat = self.TAGS["fastfood"]
            number_match += 1
        if "VIR M MARCHAND MIKAIL" in lib:
            lib = "Virement Mikail"
            cat = self.TAGS["caché"]
            number_match += 1
        if "INT DEB FORFAIT" in lib:
            lib = "Frais banque"
            cat = self.TAGS["banque"]
            number_match += 1
        if "HAVAUX BOHARS" in lib:
            lib = "Glacier Capucins"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "SUPER U 29 BREST" in lib:
            lib = "Super U Keredern"
            cat = self.TAGS["bouffe"]
            number_match += 1
        if "MR DEMIRDELEN OU MLE MA" in lib:
            lib = "Compte Commun"
            cat = self.TAGS["caché"]
            number_match += 1
        if "DAB" in lib and "BREST BELLEVUE" in lib:
            lib = "DAB Bellevue"
            cat = self.TAGS["dab"]
            number_match += 1
        if "SALAIRE ARKADE" in lib:
            lib = "Salaire Arkea"
            cat = self.TAGS["salaire"]
            number_match += 1
        if "REEDITION CODE CONFIDENTIEL" in lib:
            lib = "Reedition code confidentiel"
            cat = self.TAGS["banque"]
            number_match += 1
        if "SOUSCRIPTION PARTS  SOCIALES" in lib:
            lib = "Souscription parts sociales"
            cat = self.TAGS["banque"]
            number_match += 1
        if "COTISATION EUROCOMPTE" in lib:
            lib = "Cotisation eurocompte"
            cat = self.TAGS["banque"]
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
        dateOp, date, lib, debit, credit = line.split(delimiter)
        debit = str(debit).replace('"', "").replace(",", ".")
        credit = str(credit).replace('"', "").replace(",", ".")
        if debit.strip() == "":
            debit = "0"
        if credit.strip() == "":
            credit = "0"
        eur = str(-float(debit) + float(credit))
        return date, lib, eur, ""
