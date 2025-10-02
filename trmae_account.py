from abc import ABC

from .abstract_account import AbstractAccount


class TRMaeAccount(AbstractAccount, ABC):

    def __init__(self):
        super(TRMaeAccount, self).__init__(
            path="D:\\Mikail\\Papiers importants\\Comptes\\TR_Maeliss\\",
            preheader=1,
            bank="TRMAE",
            extension=".csv",
            delimiter=";"
        )

    def split_date(self, date):
        j, m, a = date.split("/")
        return j, m, a

    def split_date_lib_eur(self, line, delimiter):
        line.replace("€", "")
        date, typ, status, eur, lib = line.split(delimiter)
        eur = eur[:-4].replace(",", ".")
        if "Echec" in status:
            raise Warning("Operation refusée")
        if "Succ" in status:
            if "bit" in typ:
                # as in "Débit", not "Crédit" ; problème d'encoding d'où cette solution
                eur = "-" + eur
        return date, lib, eur, ""

    def category_parsing(self, lib, cat):
        number_match = 0
        if "17 ROUTE NATIONALE  ST LEGER DE LINIERES 49170" in lib:
            lib = "Boulangerie Saint Leger de Linieres"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "RUE DU BOURG DE PAILLE  BEAUCOUZE 49070" in lib:
            lib = "Super U Beaucouzé"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "23 RUE DE LA 2E DIVISION BLINDEE  BREST 29200" in lib:
            lib = "Thai Phucket"
            cat += self.TAGS["resto"]
            number_match += 1
        if "127 RUE JEAN JAURES  BREST 29200" in lib:
            lib = "Allo Pizza"
            cat += self.TAGS["fast-food"]
            number_match += 1
        if "SAS U EXPRESS" in lib:
            lib = "Super U"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL INDIGO - 32 AVENUE JEAN JANVIER" in lib:
            lib = "Epicerie Joseph (Rennes)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "MR PEREZ - 28 AVENUE DE TARENTE" in lib:
            lib = "Fournil des provinces Tarente (Boulangerie)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL BEAJ" in lib:
            lib = "Beaj Café"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "SUBWAY" in lib:
            lib = "Subway"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "CARREFOUR HYPERMARCHES - 126 BOULEVARD DE PLYMOUTH" in lib:
            lib = "Carrefour Iroise"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL BALBEK" in lib:
            lib = "Le cèdre (kebab)"
            cat += self.TAGS["resto"]
            number_match += 1
        if "BK LANDI" in lib:
            lib = "Burger King Landivisiau"
            cat += self.TAGS["resto"]
            number_match += 1
        if "TRIMARAN" in lib:
            lib = "Trimaran (bar)"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "MEMORIA" in lib:
            lib = "Casa Nostra"
            cat += self.TAGS["resto"]
            number_match += 1
        if "3DLS - PLACE NAPOLEON III" in lib:
            lib = "Carrefour Market"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "BARTOLALAN" in lib:
            lib = "Subway"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "POKEFACT" in lib:
            lib = "La Poke"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "COULEURS INSULAIRES" in lib:
            lib = "Amour de pomme de terre"
            cat += self.TAGS["resto"]
            number_match += 1
        if "SARL MAP GARE" in lib:
            lib = "Macdo Gare de Rennes"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "SARL AVEL BREIZH" in lib:
            lib = "Macdo Le Relecq"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "SAS JIPIGOULI" in lib:
            lib = "Roast It"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "Echange de vos titres" in lib:
            lib = "Récupération titres périmés"
            cat += self.TAGS["caché"]
            number_match += 1
        if "Titres p" in lib:
            lib = "Titres périmés"
            cat += self.TAGS["caché"]
            number_match += 1
        if "SA VICTORY - GALERIE ATLANTIS" in lib:
            lib = "Macdo Saint Herblain"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "ORIJINAL PIDE" in lib:
            lib = "Orijinal Pide"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "SARL BRGR" in lib:
            lib = "Pizzeria Pozzi"
            cat += self.TAGS["resto"]
            number_match += 1
        if "LA BRIOCHE DOREE" in lib:
            lib = "La Brioche Dorée"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LE TAMELIER DE SAINT MARC" in lib:
            lib = "Le Tamelier de Saint Marc"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL SAVEUR ROTIE" in lib:
            lib = "L'Oriflamme"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "SAS DISTRIBREIZH" in lib:
            lib = "Super U"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL POMODORO" in lib:
            lib = "La Tomate"
            cat += self.TAGS["resto"]
            number_match += 1
        if "SA STEREN" in lib:
            lib = "Intermarché"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SAS LBDP BRE" in lib:
            lib = "Les burgers de papa"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "LES DEUX MONTPARNASSE" in lib:
            lib = "Burger King Montparnasse"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "BELLEVUE KEBAB" in lib:
            lib = "Bellevue Kebab"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "SBH COMPANY" in lib:
            lib = "Subway Grenelle"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "EURL MC GUIGAN" in lib:
            lib = "Mc Guigan's"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "SARL JLGA RENNES" in lib:
            lib = "Carrefour City"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "FOURNIL DE PAULINE" in lib:
            lib = "Fournil de Pauline"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL HELIES LOIC" in lib:
            lib = "L'atelier du boulanger"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "CARREFOUR CITY" in lib:
            lib = "Carrefour City"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL XIN LE YUAN" in lib:
            lib = "China Town"
            cat += self.TAGS["resto"]
            number_match += 1
        if "SARL QLMD" in lib:
            lib = "O'Local"
            cat += self.TAGS["resto"]
            number_match += 1
        if "SARL CARPE DIEM" in lib:
            lib = "Chez Zaza"
            cat += self.TAGS["resto"]
            number_match += 1
        if "SARL JANVIER" in lib:
            lib = "Boulangerie Christian Janvier"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL TARTINES D AUTREFOIS" in lib:
            lib = "Boulangerie Tartines d'Autrefois"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LE MOULIN DE L IROISE" in lib:
            lib = "Boulangerie Le Moulin de l'Iroise"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL AUGUSTIN BREST IROISE" in lib:
            lib = "Boulangerie Saint Augustin"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SAS DCF" in lib:
            lib = "Géant Casino"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL LEATOM" in lib:
            lib = "Carrefour City"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LE BISTROT" in lib:
            lib = "Le Bistrot"
            cat += self.TAGS["resto"]
            number_match += 1
        if "ROADSIDE" in lib:
            lib = "Roadside"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "SARL EVAB1" in lib:
            lib = "Macdo"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "SARL JULIADIS" in lib:
            lib = "Carrefour City"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL E KICHEN AND AOD" in lib:
            lib = "Boulangerie Kichen An Aod"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SA HEBRIDES" in lib:
            lib = "Intermarché"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL MIDTOWN" in lib:
            lib = "Midtown"
            cat += self.TAGS["resto"]
            number_match += 1
        if "SARL CABELLAN JEZEGOU" in lib:
            lib = "Crêperie Cornouaille"
            cat += self.TAGS["resto"]
            number_match += 1
        if "SARL LES GOURMANDISES DE ST PIER" in lib:
            lib = "Boulangerie Gourmandises de Saint Pierre"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "MARCELLE MORRIS" in lib:
            lib = "Marcelle et Moris"
            cat += self.TAGS["resto"]
            number_match += 1
        if "OTANTIK KEBAB" in lib:
            lib = "Otantik Kebab"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "SARL FONTAINE" in lib:
            lib = "Sandwich"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SARL FLO 2005" in lib:
            lib = "Subway"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "SARL ANGELE - CCIAL ALMA" in lib:
            lib = "Brasserie Angele"
            cat += self.TAGS["resto"]
            number_match += 1
        if "SA HEBRIDES - 97 RUE P MASSON  BREST" in lib:
            lib = "Intermarché"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "EURL BOULANGERIE NICOL" in lib:
            lib = "Fournil de Pauline (Boulangerie)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "Chargement de votre carte" in lib:
            lib = lib[:-6] + "€ )".replace(",", ".")
            cat += self.TAGS["salaire"]
            number_match += 1
        return lib, cat, number_match
