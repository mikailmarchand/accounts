from abc import ABC

from .abstract_account import AbstractAccount


class LBPAccount(AbstractAccount, ABC):

    def __init__(self):
        super(LBPAccount, self).__init__(
            path="LBP",
            # Changement du pré-header en février 2022
            preheader=7,
            bank="LBP",
            extension=".tsv",
            delimiter="\t"
        )

    def split_date(self, date):
        j, m, a = date.split("/")
        return j, m, a

    def split_date_lib_eur(self, line, delimiter):
        try:
            line = line.strip()
            if line.count(delimiter) == 3:
                date, lib, eur, fr = line.split(delimiter)
            else:
                # line.count(delimiter) == 2
                date, lib, eur = line.split(delimiter)
        except Exception as e:
            breakpoint()
        return date, lib, eur, ""

    def category_parsing(self, lib, cat):
        number_match = 0
        # Laisser celui là en premier pour pas se faire écraser
        # Avec un libellé en "boulangerie"
        if "Boulanger" in lib:
            lib = "Boulanger"
            cat += self.TAGS["matériel"]
            number_match += 1

        # Ca commence donc là !
        """
        if "" in lib:
            lib = ""
            cat = self.TAGS["check"]
            number_match += 1
        """
        if "LUCAS BOURNEUF" in lib:
            lib = "Virement Lucas Bourneuf"
            cat = self.TAGS["check"]
            number_match += 1
        if "ENGIE ENERGIE" in lib:
            lib = "Engie"
            cat = self.TAGS["abonnements"]
            number_match += 1
        if "DeezerFR" in lib:
            lib = "Deezer"
            cat = self.TAGS["abonnements"]
            number_match += 1
        if "Nintendo" in lib:
            lib = "Nintendo"
            cat = self.TAGS["culture"]
            number_match += 1
        if "CMB SIEGE" in lib:
            lib = "Virement CMB Siege (CSE)"
            cat = self.TAGS["autre"]
            number_match += 1
        if "Vinted" in lib:
            lib = "Vinted"
            cat = self.TAGS["culture"]
            number_match += 1
        if "MANOMANO" in lib:
            lib = "Manomano"
            cat = self.TAGS["materiel"]
            number_match += 1
        if "SumUp" in lib:
            lib = "SumUp"
            cat = self.TAGS["check"]
            number_match += 1
        if "TICKETS" in lib:
            lib = "Tickets ?"
            cat = self.TAGS["check"]
            number_match += 1
        if "STEPHANE COUSSEAU" in lib:
            lib = "Virement Steph"
            cat = self.TAGS["check"]
            number_match += 1
        if "L Commerce" in lib:
            lib = "Leclerc web achat"
            cat = self.TAGS["culture"]
            number_match += 1
        if "CAPU BREST PAR" in lib:
            lib = "Parking Les Capucins"
            cat = self.TAGS["transport"]
            number_match += 1
        if "BRANDA 39" in lib:
            lib = "Bistrot 39"
            cat = self.TAGS["resto"]
            number_match += 1
        if "LES AILES P" in lib:
            lib = "Les ailes p ?"
            cat = self.TAGS["autre"]
            number_match += 1
        if "Tribee" in lib:
            lib = "Cagnotte Tribee"
            cat = self.TAGS["cadeau"]
            number_match += 1
        if "ENGIE SOLUTIONS" in lib:
            lib = "Engie"
            cat = self.TAGS["abos"]
            number_match += 1
        if "CB Vinted" in lib:
            lib = "Vinted"
            cat = self.TAGS["check"]
            number_match += 1
        if "CB PANDORA" in lib:
            lib = "Le garde manger"
            cat = self.TAGS["resto"]
            number_match += 1
        if "PHCIE DES HALL" in lib:
            lib = "Pharmacie des halles"
            cat = self.TAGS["santé"]
            number_match += 1
        if "FAIRPHONE B.V." in lib:
            lib = "Fairphone"
            cat = self.TAGS["matériel"]
            number_match += 1
        if "Bleu Lavande" in lib:
            lib = "Bleu Lavade"
            cat = self.TAGS["vêtements"]
            number_match += 1
        if "FLOA PAY" in lib:
            lib = "Paiement plusieurs fois FLOA PAY : TODO"
            cat = self.TAGS["check"]
            number_match += 1
        if "LA GRAY BOX" in lib:
            lib = "La Gray Box"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "OTacos" in lib:
            lib = "O'Tacos"
            cat = self.TAGS["fast-food"]
            number_match += 1
        if "LE BYGGVIR" in lib:
            lib = "Le Bygvvir"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "JUL 0397" in lib:
            lib = "Jules"
            cat = self.TAGS["vetements"]
            number_match += 1
        if "SEB INTERNATIO" in lib:
            lib = "Seb/Moulinex"
            cat = self.TAGS["matériel"]
            number_match += 1
        if "PHILIBERTNET" in lib:
            lib = "Philibert"
            cat = self.TAGS["culture"]
            number_match += 1
        if "199 VERSAILLES" in lib:
            lib = "Nature et Découverte"
            cat = self.TAGS["matériel"]
            number_match += 1
        if "PAPY DONUTS" in lib:
            lib = "Papy Donuts"
            cat = self.TAGS["fast-food"]
            number_match += 1
        if "TENGA STORE" in lib:
            lib = "Tenga store"
            cat = self.TAGS["matériel"]
            number_match += 1
        if "NUVERSE" in lib:
            lib = "Marvel snap nuverse"
            cat = self.TAGS["snap"]
            number_match += 1
        if "Google Play" in lib:
            lib = "Marvel snap, probablement"
            cat = self.TAGS["snap"]
            number_match += 1
        if "PANIC ROOM" in lib:
            lib = "Panic Room (escape game)"
            cat = self.TAGS["evl"]
            number_match += 1
        if "FOURNIL PIERRE" in lib:
            lib = "Boulangerie le fournil de pierre"
            cat = self.TAGS["check"]
            number_match += 1
        if "ATELIER BOUCHE" in lib:
            lib = "Atelier du boucher"
            cat = self.TAGS["fastfood"]
            number_match += 1
        if "ENVIE 29" in lib:
            lib = "Envie"
            cat = self.TAGS["emménagement"]
            number_match += 1
        if "LINSOUL" in lib:
            lib = "Linsoul"
            cat = self.TAGS["culture"]
            number_match += 1
        if "CCL" in lib:
            lib = "Café des Champs Libre"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "SP LOOP EARPLU" in lib:
            lib = "Loop earplug"
            cat = self.TAGS["matériel"]
            number_match += 1
        if "PAM BREST" in lib:
            lib = "Virement PAM"
            cat = self.TAGS["check"]
            number_match += 1
        if "YVETTE ET SIMO" in lib:
            lib = "Simone et Yvette"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "BUFFALO GRILL" in lib:
            lib = "Buffalo Grill"
            cat = self.TAGS["resto"]
            number_match += 1
        if "2TL RENNES" in lib:
            lib = "Bus tram Rennes"
            cat = self.TAGS["transport"]
            number_match += 1
        if "LES CHANCEUX" in lib:
            lib = "Les chanceux (PAM)"
            cat = self.TAGS["resto"]
            number_match += 1
        if "AU P TIT LIPOU" in lib:
            lib = "Glacier capucins"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "GABYSAM" in lib:
            lib = "Gourmand mais pas que"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "MAMAN COMPTE" in lib:
            lib = "Virement maman mika"
            cat = self.TAGS["check"]
            number_match += 1
        if "PRELEVEMENT DE GENERATION" in lib:
            lib = "Générations (mutuelle)"
            cat = self.TAGS["santé"]
            number_match += 1
        if "LA POSTE MOBILE" in lib:
            lib = "LA POSTE MOBILE"
            cat = self.TAGS["abos"]
            number_match += 1
        if "BLE NOIR" in lib:
            lib = "Crêperie Blé noir (stang alar)"
            cat = self.TAGS["resto"]
            number_match += 1
        if "CPAM" in lib:
            lib = "CPAM"
            cat = self.TAGS["santé"]
            number_match += 1
        if "PRPLDOT" in lib:
            lib = "Limited Run Games"
            cat = self.TAGS["culture"]
            number_match += 1
        if "MCDONALD" in lib:
            lib = "MCDONALD"
            cat = self.TAGS["fastfood"]
            number_match += 1
        if "EVERSPORTS" in lib:
            lib = "Pole Dance"
            cat = self.TAGS["sport"]
            number_match += 1
        if "MAC DONA" in lib:
            lib = "Macdo"
            cat += self.TAGS["resto"]
            number_match += 1
        if "MARIE BLACHERE" in lib:
            lib = "Marie blachère"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "STEAM" in lib:
            lib = "Steam"
            cat += self.TAGS["culture"]
            number_match += 1
        if "GoFundMe" in lib:
            lib = "GoFundMe"
            cat += self.TAGS["don"]
            number_match += 1
        if "LA VIA ROMA" in lib:
            lib = "LA VIA ROMA (pizzeria rennes)"
            cat = self.TAGS["resto"]
            number_match += 1
        if "XIN LE YUAN" in lib:
            lib = "XIN LE YUAN"
            cat = self.TAGS["autre"]
            number_match += 1
        if "900CARE" in lib:
            lib = "900care"
            cat = self.TAGS["bouffe"]
            number_match += 1
        if "BOLIDSTER.COM" in lib:
            lib = "Bolidster"
            cat = self.TAGS["vetement"]
            number_match += 1
        if "LES FRERES JAC" in lib:
            lib = "Les freres jacques (lancer de hache)"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "RECRE 3 CURES" in lib:
            lib = "La récré des 3 curés"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "LeBonCoin" in lib:
            lib = "Le Bon Coin"
            cat = self.TAGS["check"]
            number_match += 1
        if "LA FABRIK 1801" in lib:
            lib = "LA FABRIK 1801"
            cat = self.TAGS["resto"]
            number_match += 1
        if "MEMPHIS COFFEE" in lib:
            lib = "MEMPHIS COFFEE"
            cat = self.TAGS["resto"]
            number_match += 1
        if "Disney PLUS" in lib:
            lib = "Disney+"
            cat = self.TAGS["abo"]
            number_match += 1
        if "ALMA LA BAGUET" in lib:
            lib = "Paiement Alma pour la baguetterie"
            cat = self.TAGS["culture"]
            number_match += 1
        if "Decathlon Fran" in lib:
            lib = "Decathlon (web)"
            cat = self.TAGS["vetements"]
            number_match += 1
        if "MAMAMIA" in lib:
            lib = "Mamamia"
            cat = self.TAGS["fastfood"]
            number_match += 1
        if "MGP Vinted " in lib:
            lib = "Vinted"
            cat = self.TAGS["check"]
            number_match += 1
        if "BIO TOPIE" in lib:
            lib = "Bio topie"
            cat = self.TAGS["matériel"]
            number_match += 1
        if "ASPHALTE" in lib:
            lib = "Asphalte"
            cat = self.TAGS["vetement"]
            number_match += 1
        if "PRESSE BELLEVU" in lib:
            lib = "Tabac presse Carterie"
            cat = self.TAGS["check"]
            number_match += 1
        if "DE BUYER" in lib:
            lib = "De Buyer"
            cat = self.TAGS["matériel"]
            number_match += 1
        if "SATYR" in lib:
            lib = "Satyr (resto)"
            cat = self.TAGS["resto"]
            number_match += 1
        if "HUMBLEBUNDLE" in lib:
            lib = "Humble Bundle"
            cat = self.TAGS["culture"]
            number_match += 1
        if "Nintendo of Eu" in lib:
            lib = "Nintendo of Europe"
            cat = self.TAGS["culture"]
            number_match += 1
        if "PRISON ISLAND" in lib:
            lib = "Prison Island"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "GANDI" in lib:
            lib = "Gandi"
            cat = self.TAGS["evl"]
            number_match += 1
        if "CINEMA CGR" in lib:
            lib = "Cinéma CGR"
            cat = self.TAGS["sortie"]
            number_match += 1
        if "JULIE PASCAL Salaire" in lib:
            lib = "Paiement Julie Pascal"
            cat = self.TAGS["azenor"]
            number_match += 1
        if "LA FROMENTINE" in lib:
            lib = "La fromentine"
            cat = self.TAGS["resto"]
            number_match += 1
        if "leboncoin" in lib:
            lib = "Le Bon Coin"
            cat = self.TAGS["check"]
            number_match += 1
        if "MONDIAL RELAY" in lib:
            lib = "Mondial Relay"
            cat += self.TAGS["check"]
            number_match += 1
        if "VIREMENT INSTANTANE CREDIT" in lib:
            lib = "Virement instantané (mika cmb ?)"
            cat += self.TAGS["caché"]
            number_match += 1
        if "CASINO" in lib:
            lib = "Casino"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "lebonco payout" in lib:
            lib = "Virement le bon coin"
            cat += self.TAGS["check"]
            number_match += 1
        if "Doctolib" in lib:
            lib = "Doctolib"
            cat += self.TAGS["santé"]
            number_match += 1
        if "ALLO PIZZAS" in lib:
            lib = "Allo Pizzas"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "TOTALENERGIES" in lib:
            lib = "Total énergie"
            cat += self.TAGS["abos"]
            number_match += 1
        if "THAI PHUKET" in lib:
            lib = "Thai Phuket"
            cat += self.TAGS["resto"]
            number_match += 1
        if "RD BREST" in lib:
            lib = "BiBus (?)"
            cat += self.TAGS["transport"]
            number_match += 1
        if "3X 4X ONEY " in lib:
            lib = "Paiement en plusieurs fois via Oney : Check"
            cat += self.TAGS["check"]
            number_match += 1
        if "MERANO" in lib:
            lib = "La Catrina (bar)"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "BLUE" in lib:
            lib = "Bluebird coffee (Rennes)"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "FIVE GUYS" in lib:
            lib = "Five Guys"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "OLIVANE TILLY" in lib:
            lib = "Virement Olivane Tilly"
            cat += self.TAGS["check"]
            number_match += 1
        if "Leboncoin" in lib:
            lib = "Le Bon Coin : CHECK"
            cat += self.TAGS["check"]
            number_match += 1
        if "AU BOEUF CHARO" in lib:
            lib = "Au boeuf charolais (boucherie pl nap III)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "PPG BABYBIO" in lib:
            lib = "Babybio"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LA BRIOCHE DOR" in lib:
            lib = "La brioche dorée"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "THAI - PHUKET" in lib:
            lib = "Thai Phuket"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "ESHOPDIRECT" in lib:
            lib = "Vaude boutique en ligne"
            cat += self.TAGS["transport"]
            number_match += 1
        if "SOSTRENE GRENE" in lib:
            lib = "Sostrene Grene"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "AU SAINT ANTOI" in lib:
            lib = "Au Saint Antoine"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LE JARDIN PART" in lib:
            lib = "Au p'ty lyonnais"
            cat += self.TAGS["resto"]
            number_match += 1
        if "LAV LANGEVIN" in lib:
            lib = "Laverie Bellevue (Langevin)"
            cat += self.TAGS["autre"]
            number_match += 1
        if "COMPTE 10011000207560893387C" in lib:
            lib = "Virement CMB Mika"
            cat += self.TAGS["caché"]
            number_match += 1
        if "DEMUYNCKPIERRO" in lib:
            lib = "L'arome antique"
            cat += self.TAGS["resto"]
            number_match += 1
        if "JENNIFER CRETTEX" in lib:
            lib = "Jennifer Crettex (psy)"
            cat += self.TAGS["santé"]
            number_match += 1
        if "LE SALON DE SA" in lib:
            lib = "Le salon de sabine"
            cat += self.TAGS["coiffeur"]
            number_match += 1
        if "WIX.COM" in lib:
            lib = "Paiement site internet"
            cat += self.TAGS["evl"]
            number_match += 1
        if "LE DJERBA" in lib:
            lib = "Le Djerba (kebab)"
            cat += self.TAGS["fast-food"]
            number_match += 1
        if "LES VIVANDIERE" in lib:
            lib = "Les Ribines"
            cat += self.TAGS["resto"]
            number_match += 1
        if "M OU MME STEPHANE CO" in lib:
            lib = "Check : virement maman/steph"
            cat += self.TAGS["check"]
            number_match += 1
        if "BOUCHE A OREIL" in lib:
            lib = "Le bouche à oreille"
            cat += self.TAGS["resto"]
            number_match += 1
        if "LYDIA APP" in lib:
            lib = "Check : App Lydia (cagnotte ?)"
            cat += self.TAGS["check"]
            number_match += 1
        if "VERTBAUDET" in lib:
            lib = "Vert Baudet"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "PALM COURT" in lib:
            lib = "Kickstarter"
            cat += self.TAGS["culture"]
            number_match += 1
        if "MR OU MME MARCHAND PH" in lib:
            lib = "Virement Philippe Marchand"
            cat += self.TAGS["check"]
            number_match += 1
        if "ARENASHEDS" in lib:
            lib = "Arenasheds ???"
            cat += self.TAGS["autre"]
            number_match += 1
        if "MANDOO" in lib:
            lib = "Mandoo"
            cat += self.TAGS["resto"]
            number_match += 1
        if "ARCHE DE NEO" in lib:
            lib = "Arché de Néo"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "GLOBALES PREST" in lib:
            lib = "Globales prest ???"
            cat += self.TAGS["autre"]
            number_match += 1
        if "LES ENFANTS" in lib:
            lib = "Les enfants de dialogues"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "900.CARE" in lib:
            lib = "900.care"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LES GATEUSES" in lib:
            lib = "Les gateuses"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "UBER    EATS" in lib:
            lib = "Uber Eats"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "SP WALTS COMIC" in lib:
            lib = "Walt's Comics"
            cat += self.TAGS["culture"]
            number_match += 1
        if "LES VELOS BRES" in lib:
            lib = "Les vélos brestois"
            cat += self.TAGS["transport"]
            number_match += 1
        if "ASENDIA" in lib:
            lib = "Asendia (transport colis)"
            cat += self.TAGS["check"]
            number_match += 1
        if "LES LIBRAIRES" in lib:
            lib = "Dialogues"
            cat += self.TAGS["culture"]
            number_match += 1
        if "SP GENERAL GUI" in lib:
            lib = "General Guitar Gadget"
            cat += self.TAGS["culture"]
            number_match += 1
        if "LA GROTTE" in lib:
            lib = "La Grotte"
            cat += self.TAGS["check"]
            number_match += 1
        if "PHARMA MOULIN" in lib:
            lib = "Pharmacie Relecq"
            cat += self.TAGS["santé"]
            number_match += 1
        if "FOURNIL DU PON" in lib:
            lib = "Boulangerie, fournil ? "
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "O GOURMET" in lib:
            lib = "O Gourmet"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "BEAJ KAFE" in lib:
            lib = "Beaj Kafe"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "BOBA INVEST" in lib:
            lib = "Bubble Tea"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "AOR017020MCDO1" in lib:
            lib = "Macdo Montparnasse"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "BIG FERNAND" in lib:
            lib = "Big Fernand"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "AU BUREAU" in lib:
            lib = "Au Bureau"
            cat += self.TAGS["resto"]
            number_match += 1
        if "EURL JRCR" in lib:
            lib = "Macdo Gros Horloge Rouen"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "CGF15855BKING1" in lib:
            lib = "Burger King"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "RATP" in lib:
            lib = "RATP"
            cat += self.TAGS["transport"]
            number_match += 1
        if "TCAR" in lib:
            lib = "Bus Rouen"
            cat += self.TAGS["transport"]
            number_match += 1
        if "2THELOO" in lib:
            lib = "2 The Loo"
            cat += self.TAGS["autre"]
            number_match += 1
        if "LE BIOREK BRES" in lib:
            lib = "Biorek"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "LE TORTUGA" in lib:
            lib = "Le Tortuga"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "BARIL OR DIE" in lib:
            lib = "Brasserie de la PAM"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "AUCHAN.FR" in lib:
            lib = "Auchan.fr"
            cat += self.TAGS["check"]
            number_match += 1
        if "Gamefound" in lib:
            lib = "Gamefound (Kickstarter)"
            cat += self.TAGS["culture"]
            number_match += 1
        if "SIMON TIFFANY" in lib:
            lib = "Nounou (Tiffany Simon)"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "THE DUBLINERS" in lib:
            lib = "The Dubliners"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "MME MARCHAND AZENOR" in lib:
            lib = "Virement Azenor"
            cat += self.TAGS["check"]
            number_match += 1
        if "MAGIC BAZAR" in lib:
            lib = "Magic Bazar"
            cat += self.TAGS["magic"]
            number_match += 1
        if "NUANCES BRESIL" in lib:
            lib = "Coiffeur (Nuances Brésil)"
            cat += self.TAGS["coiffeur"]
            number_match += 1
        if "Wizards of the" in lib:
            lib = "Magic (Site officiel de wizards)"
            cat += self.TAGS["magic"]
            number_match += 1
        if "JARDIN DE GWEN" in lib:
            lib = "Jardin de Gwen"
            cat += self.TAGS["resto"]
            number_match += 1
        if "EVL" in lib:
            lib = "EVL (virement interne ?)"
            cat += self.TAGS["evl"]
            number_match += 1
        if "PHARMA L IROIS" in lib:
            lib = "Pharmacie de l'iroise"
            cat += self.TAGS["sante"]
            number_match += 1
        if "LE FOURNIL" in lib:
            lib = "Le fournil des provinces"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "Place des Salaries" in lib:
            lib = "Syndicat"
            cat += self.TAGS["abos"]
            number_match += 1
        if "LUDIPOLE" in lib:
            lib = "Ty Kall"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "Ulule" in lib:
            lib = "Ulule"
            cat += self.TAGS["check"]
            number_match += 1
        if "IMPERIALE" in lib:
            lib = "L'Impériale"
            cat += self.TAGS["resto"]
            number_match += 1
        if "PISCINE" in lib:
            lib = "Piscine"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "LORIANT VERONIQUE" in lib:
            lib = "Véronique Loriant (nounou)"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "NEWREST WAGONS" in lib:
            lib = "Bouffe Train"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "PAJE" in lib:
            lib = "PAJE"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "JULIEN BOUVET" in lib:
            lib = "Paiement Dude"
            cat += self.TAGS["check"]
            number_match += 1
        if "MAHE LYDIA / THOMAS LUKE" in lib:
            lib = "Paiement Luke Lydia"
            cat += self.TAGS["check"]
            number_match += 1
        if "FOURNIL BELLEV" in lib:
            lib = "Le fournil de Pauline (Boulangerie Bellevue)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "Rejeanne" in lib:
            lib = "Rejeanne"
            cat += self.TAGS["vetements"]
            number_match += 1
        if "MAGIC ATP" in lib:
            lib = "Magic Corporation"
            cat += self.TAGS["magic"]
            number_match += 1
        if "babybio" in lib:
            lib = "Babybio"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "Place des salaries" in lib:
            lib = "Remboursement chèque cadeau Maeliss"
            cat += self.TAGS["check"]
            number_match += 1
        if "LA CAVE AUX MO" in lib:
            lib = "La Cave aux moines"
            cat += self.TAGS["resto"]
            number_match += 1
        if "SKPCM CHOCOLAT" in lib:
            lib = "ShoCo"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "LOULI DES BOIS" in lib:
            lib = "Louli des bois"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "SAS LIBRAIRIE" in lib:
            lib = "Librairie (Dialogue ?)"
            cat += self.TAGS["culture"]
            number_match += 1
        if "MORPHE" in lib:
            lib = "Morphée"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "BOKU" in lib:
            lib = "Boku"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "ARTISAN PLOMBIER BRETON" in lib:
            lib = "Paiment Plombier"
            cat += self.TAGS["autre"]
            number_match += 1
        if "ASPHALTE.COM" in lib:
            lib = "Asphalte"
            cat += self.TAGS["vetement"]
            number_match += 1
        if "MAC DO - NFC" in lib:
            lib = "Macdo (Morlaix)"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "PHARM.SCHNEEGA" in lib:
            lib = "Pharmacie (Montreuil)"
            cat += self.TAGS["santé"]
            number_match += 1
        if "BERTRAND MELANIE" in lib:
            lib = "Paiment Lanie"
            cat += self.TAGS["check"]
            number_match += 1
        if "MLE MAUVE OU MR BOUV" in lib:
            lib = "Paiement dude"
            cat += self.TAGS["check"]
            number_match += 1
        if "PICARD SA" in lib:
            lib = "Picard"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "ACHATBILLETCIN" in lib:
            lib = "Cinéma (Saumur)"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "LE MAESTRO" in lib:
            lib = "Subway"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "BREST LUDIQUE" in lib:
            lib = "Ludik Addict"
            cat += self.TAGS["culture"]
            number_match += 1
        if "LA FABRIQUE" in lib:
            lib = "La Gentle Factory"
            cat += self.TAGS["vetements"]
            number_match += 1
        if "TIR NA NOG" in lib:
            lib = "Tir Na Nog"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "SYNDICAT CGT" in lib:
            lib = "CGT (Syndicat)"
            cat += self.TAGS["abonnement"]
            number_match += 1
        if "Garde Azen" in lib:
            lib = "Assmat Azenor"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "Bouygues Telecom" in lib:
            lib = "Bouygues"
            cat += self.TAGS["abos"]
            number_match += 1
        if "HelloFresh" in lib:
            lib = "HelloFresh"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "JUNEO" in lib:
            lib = "Juneo"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "ORIFLAMME" in lib:
            lib = "L'oriflamme"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "TRINITAINE" in lib:
            lib = "La trinitaine"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "TOUR DU MONDE" in lib:
            lib = "Le tour du monde"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "CHEQUES VACANCES" in lib:
            lib = "Chèques vacances"
            cat += self.TAGS["autre"]
            number_match += 1
        if "CB RELAY" in lib:
            lib = "Relay"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "STARBUCKS" in lib:
            lib = "Starbucks"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "WWW.CMYK.GAMES" in lib:
            lib = "CMYK Games (Kickstarter)"
            cat += self.TAGS["culture"]
            number_match += 1
        if "Philips Consum" in lib:
            lib = "Philipps"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "L IMPERATRICE" in lib:
            lib = "L'impératrice"
            cat += self.TAGS["resto"]
            number_match += 1
        if "ABGRALL LAUREN" in lib:
            lib = "Abgrall Lauren(ce?)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "DISPLATE" in lib:
            lib = "Displate"
            cat += self.TAGS["check"]
            number_match += 1
        if "PHIE BELLEVUE" in lib:
            lib = "Pharmacie Bellevue"
            cat += self.TAGS["santé"]
            number_match += 1
        if "PHARMACIE" in lib:
            lib = "Pharmacie"
            cat += self.TAGS["santé"]
            number_match += 1
        if "STARBUCKS" in lib:
            lib = "Starbucks"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "SARL LA CHOCOL" in lib:
            lib = "La chocolaterie"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "Wix.com" in lib:
            lib = "Wix.com"
            cat += self.TAGS["evl"]
            number_match += 1
        if "HELLOFRESH" in lib:
            lib = "Hellofresh"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "R KID" in lib:
            lib = "R Kid"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "PHARMACIE DES" in lib:
            lib = "Pharmacie des universités"
            cat += self.TAGS["santé"]
            number_match += 1
        if "DIRECTION GENERAL ES FINANCES PUBL" in lib:
            lib = "Impots"
            cat += self.TAGS["impots"]
            number_match += 1
        if "CALVARIN ELIA" in lib:
            lib = "Virement Mme Calvarin"
            cat += self.TAGS["loyer"]
            number_match += 1
        if "PETITSCULOTTES" in lib:
            lib = "Les petits culottés (couches)"
            cat += self.TAGS["azenor"]
            number_match += 1
        if "CHEZ MA PHARMA" in lib:
            lib = "Chez ma pharmacienne (pharma super u)"
            cat += self.TAGS["santé"]
            number_match += 1
        if "STARBUCKS" in lib:
            lib = "Starbucks"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "SUBSCRIBESTAR" in lib:
            lib = "Subscribe Star"
            cat += self.TAGS["abos"]
            number_match += 1
        if "ROAST IT" in lib:
            lib = "Roast It"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "COMITEO" in lib:
            lib = "Comiteo (CE) : check what was bought"
            cat += self.TAGS["check"]
            number_match += 1
        if "CB TC0CMRAO" in lib:
            lib = "Tram Rennes CB"
            cat += self.TAGS["transport"]
            number_match += 1
        if "MAP GARE" in lib:
            lib = "Macdo Gare Rennes"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "LES 3 BRASSEUR" in lib:
            lib = "Les 3 Brasseurs"
            cat += self.TAGS["resto"]
            number_match += 1
        if "VAUSELE MANU" in lib:
            lib = "Virement à Manu"
            cat += self.TAGS["check"]
            number_match += 1
        if "VAUSELLE MANU" in lib:
            lib = "Virement à Manu"
            cat += self.TAGS["check"]
            number_match += 1
        if "LUKE ET LYDIA" in lib:
            lib = "Virement Luke et Lydia"
            cat += self.TAGS["check"]
            number_match += 1
        if "UZR babymarkt" in lib:
            lib = "Rose ou bleu"
            cat += self.TAGS["grossesse"]
            number_match += 1
        if "MTGGOLDFISH" in lib:
            lib = "MTG Goldfish"
            cat += self.TAGS["magic"]
            number_match += 1
        if "MEMORIA" in lib:
            lib = "Casa Nostra"
            cat += self.TAGS["resto"]
            number_match += 1
        if "BOULANGERIE" in lib:
            lib = "Boulangerie"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "THOMANN" in lib:
            lib = "Thomann"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "UN AMOUR DE PD" in lib:
            lib = "Un amour de pomme de terre"
            cat += self.TAGS["resto"]
            number_match += 1
        if "LIBERTE CAISSE" in lib:
            lib = "Liberte caisse"
            cat += self.TAGS["autre"]
            number_match += 1
        if "TOLARIAN" in lib:
            lib = "Tolarian Community College"
            cat += self.TAGS["magic"]
            number_match += 1
        if "CAF DU FINISTERE" in lib:
            lib = "CAF"
            cat += self.TAGS["check"]
            number_match += 1
        if "BALBEK" in lib:
            lib = "Le cèdre"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "GRIBOUILLE" in lib:
            lib = "Gribouille ta chambre"
            cat += "grossesse"
            number_match += 1
        if "Chal-Tec GmbH" in lib:
            lib = "Klarstein"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "KEOLIS" in lib:
            lib = "Keolis"
            cat += self.TAGS["transport"]
            number_match += 1
        if "COMMISSION PAIEMENT PAR CARTE" in lib:
            lib = "Commission paiement par carte"
            cat += self.TAGS["banque"]
            number_match += 1
        if "BELLA MAMMA" in lib:
            lib = "Bella Mamma"
            cat += self.TAGS["resto"]
            number_match += 1
        if "TotalEnergies" in lib:
            lib = "Total Energie"
            cat += self.TAGS["abos"]
            number_match += 1
        if "Les Restos du" in lib:
            lib = "Les restos du coeur"
            cat += self.TAGS["don"]
            number_match += 1
        if "LES AILES POUR" in lib:
            lib = "Passage désir"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "LGE BREST" in lib:
            lib = "Laser Game Evolution (Brest)"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "LDLC" in lib:
            lib = "LDLC"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "CB AIRBNB" in lib:
            lib = "Airbnb"
            cat += self.TAGS["vacances"]
            number_match += 1
        if "KICKSTARTER" in lib:
            lib = "Kickstarter : check projet"
            cat += self.TAGS["check"]
            number_match += 1
        if "PAYSECURE.EU" in lib:
            lib = "Paysecure.eu : check si c'est pas un problème ? "
            cat += self.TAGS["autre"]
            number_match += 1
        if "EUZENOT PIERRE" in lib:
            lib = "Dr Euzenot"
            cat += self.TAGS["santé"]
            number_match += 1
        if "ROASTIT.FR" in lib:
            lib = "Roast It"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "LE POT COMMUN" in lib:
            lib = "Le pot commun"
            cat += self.TAGS["check"]
            number_match += 1
        if "PHARM UNIVERSI" in lib:
            lib = "Pharmacie universitaire"
            cat += self.TAGS["santé"]
            number_match += 1
        if "VIREMENT POUR VAUSELE MANU" in lib:
            lib = "Virement à Manu"
            cat += "TODO: check raison"
            number_match += 1
        if "JARDILAND" in lib:
            lib = "Jardiland"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "FETE-CI FETE" in lib:
            lib = "Fete-ci Fete-ça"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "ATELIER BOULAN" in lib:
            lib = "Atelier Boulangerie"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "VIREMENT PERMANENT POUR MR OU MME MARCHAND PH" in lib:
            lib = "Virement aux parents maeliss pour assurrance"
            cat += self.TAGS["abonnement"]
            number_match += 1
        if "MAXICOFFEE" in lib:
            lib = "Machine à café Arkéa"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "PAPAYOUX" in lib:
            lib = "Cagnotte Papayoux"
            cat += self.TAGS["cadeau"]
            number_match += 1
        if "Steam Purchase" in lib:
            lib = "Achat Steam"
            cat += self.TAGS["culture"]
            number_match += 1
        if "POZZI" in lib:
            lib = "Pizzeria Pozzi"
            cat += self.TAGS["resto"]
            number_match += 1
        if "O LOCAL" in lib:
            lib = "Burger O'Local"
            cat += self.TAGS["resto"]
            number_match += 1
        if "BOARDGAMEGEEK" in lib:
            lib = "Achat Board Game Geek"
            cat += self.TAGS["culture"]
            number_match += 1
        if "LALIBEE" in lib:
            lib = "Magasin Lalibee (capucins)"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "TAMELIER ST MA" in lib:
            lib = "Tamelier Saint-Marc (Boulangerie)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LA MIE CALINE" in lib:
            lib = "La mie caline"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "pathe ANGERS" in lib:
            lib = "Cinéma Gaumont Angers"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "PHARMACIE VITR" in lib:
            lib = "Pharmacie"
            cat += self.TAGS["santé"]
            number_match += 1
        if "MAGASIN CASINO" in lib:
            lib = "Casino"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "FNAC" in lib:
            lib = "FNAC"
            cat += self.TAGS["culture"]
            number_match += 1
        if "Amnesty Internati" in lib:
            lib = "Amnesty International"
            cat += self.TAGS["don"]
            number_match += 1
        if "STEPH COUSSEAU" in lib:
            lib = "Paiement Steph"
            cat += self.TAGS["check"]
            number_match += 1
        if "POLLACK ITO" in lib:
            lib = "Paiement Ito"
            cat += self.TAGS["check"]
            number_match += 1
        if "Klarstein Chal" in lib:
            lib = "Klarstein"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "FEDERAL FINANC" in lib:
            lib = "Federal Finance (PEE)"
            cat += self.TAGS["autre"]
            number_match += 1
        if "DISNEYPLUS" in lib:
            lib = "Disney+"
            cat += self.TAGS["abos"]
            number_match += 1
        if "KEVIN BIARDEAU" in lib:
            lib = "Paiement Kevin"
            cat += self.TAGS["check"]
            number_match += 1
        if "FRENCH PUB" in lib:
            lib = "French Pub"
            cat += self.TAGS["resto"]
            number_match += 1
        if "STAT HORODATEU" in lib:
            lib = "Horodateur"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "CB LA COLOC" in lib:
            lib = "La coloc"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "JAPANZON" in lib:
            lib = "Japanzone"
            cat += self.TAGS["culture"]
            number_match += 1
        if "MAJESTIC BREST" in lib:
            lib = "Majestic Brest (ciné)"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "Xsolla" in lib:
            lib = "CHECK : Xsolla"
            cat += self.TAGS["magic"]
            number_match += 1
        if "Leetchi" in lib:
            lib = "Check : Leetchi"
            cat += self.TAGS["check"]
            number_match += 1
        if "NATURE ET DECO" in lib:
            lib = "Nature et découverte"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "CULTURA" in lib:
            lib = "Cultura"
            cat += self.TAGS["culture"]
            number_match += 1
        if "leslibraires" in lib:
            lib = "Librairie Dialogues"
            cat += self.TAGS["culture"]
            number_match += 1
        if "MME CALVARIN" in lib:
            lib = "Loyer (Mme Calvarin)"
            cat += self.TAGS["loyer"]
            number_match += 1
        if "RAKUTEN" in lib:
            lib = "CHECK : Rakuten"
            number_match += 1
        if "LE MISTRAL" in lib:
            lib = "Le Mistral (kebab)"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "DISNEY PLUS" in lib:
            lib = "Disney +"
            cat += self.TAGS["abos"]
            number_match += 1
        if "EDF" in lib:
            lib = "EDF"
            cat += self.TAGS["abos"]
            number_match += 1
        if "ACHAT CB NPM" in lib:
            lib = "npm.fr (matériel en ligne)"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "CB EURL PHILIPPE" in lib:
            lib = "Garage Philippe Gassot ? (pas sur)"
            cat += self.TAGS["transport"]
            number_match += 1
        if "CB ROADSIDE" in lib:
            lib = "Roadside"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "PRELEVEMENT DE BOUYGUES TELECOM" in lib:
            lib = "Bouygues Telecom"
            cat += self.TAGS["abos"]
            number_match += 1
        if "MIDTOWN" in lib:
            lib = "Midtown"
            cat += self.TAGS["resto"]
            number_match += 1
        if "MICROMANIA" in lib:
            lib = "Micromania"
            cat += self.TAGS["culture"]
            number_match += 1
        if "MYSTERY O CLOC" in lib:
            lib = "Mystery O Clock"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "LEROY MER" in lib:
            lib = "Leroy Merlin"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "DRAGON D OR" in lib:
            lib = "Restaurant Dragon d'Or"
            cat += self.TAGS["resto"]
            number_match += 1
        if "BELLEVUE KEBAB" in lib:
            lib = "Bellevue Kebab (centre com)"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "ELECTRO DEPOT" in lib:
            lib = "Electro Dépot"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "CELTIC" in lib:
            lib = "Cinéma Le Celtic"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "LE KAMELEON" in lib:
            lib = "Coiffeur : Kaméléon"
            cat += self.TAGS["santé"]
            number_match += 1
        if "MAGASIN U" in lib:
            lib = "Magasin U"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "CB CHINA TOWN" in lib:
            lib = "China Town"
            cat += self.TAGS["resto"]
            number_match += 1
        if "BRICO DEPOT" in lib:
            lib = "Brico Dépot"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "TROC COM" in lib:
            lib = "Troc.com"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "CB SA STEREN" in lib:
            lib = "Intermarché"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LA CREPE FLAMB" in lib:
            lib = "La crêpe flambée"
            cat += self.TAGS["resto"]
            number_match += 1
        if "SARL CARPE DIE" in lib:
            lib = "Carpe Diem"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "CB BBM" in lib:
            lib = "Steakhouse turc"
            cat += self.TAGS["resto"]
            number_match += 1
        if "AVEL BREIZH" in lib:
            lib = "Macdo Le Relecq"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "BENVENUTO AU F" in lib:
            lib = "Le FAP"
            cat += self.TAGS["resto"]
            number_match += 1
        if "E KICHEN AN AO" in lib:
            lib = "Boulangerie David Le Relecq"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "BOUYGTEL VAD" in lib:
            lib = "Bouygues Tel"
            cat += self.TAGS["abonnement"]
            number_match += 1
        if "MOULIN DE L IR" in lib:
            lib = "Boulangerie : Le Moulin de l'Iroise"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LA TOULINE" in lib:
            lib = "Café La Touline Camaret"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "VIREMENT DE Sammelkartenmarkt" in lib:
            lib = "MKM"
            cat += self.TAGS["magic"]
            number_match += 1
        if "CB SUMUP" in lib:
            lib = "CB SUMUP (réparation vélo ?)"
            cat += self.TAGS["check"]
            number_match += 1
        if "ARKEA" in lib:
            lib = "Arkéa"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "MC DONALD" in lib:
            lib = "Macdo"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "BIBUS" in lib:
            lib = "Bibus"
            cat += self.TAGS["transport"]
            number_match += 1
        if "BIARDEAU KEVIN" in lib:
            lib = "Virement à Kevin B."
            cat += self.TAGS["autre"]
            number_match += 1
        if "DGFIP FINANCES PUBLI" in lib:
            lib = "TODO: Impots"
            number_match += 1
        if "MC GUIGAN" in lib:
            lib = "Mc Guigan's"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "PICARD SURGELE" in lib:
            lib = "Picard"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "L OYSTER" in lib:
            lib = "L'oyster"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "MOUTON 5 PATTE" in lib:
            lib = "Le mouton à 5 pattes"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "WE WANT BEER" in lib:
            lib = "We Want Beer"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "CABELLAN-JEZEG" in lib:
            lib = "Crêperie de Cornouaille"
            cat += self.TAGS["resto"]
            number_match += 1
        if "EUREST-C426" in lib:
            lib = "Resto Arkéa (in resto)"
            cat += self.TAGS["resto"]
            number_match += 1
        if "Recharge.fr" in lib:
            lib = "TODO : Recharge.fr"
            number_match += 1
        if "LE KIOSK" in lib:
            lib = "Crêperie Le Kiosk"
            cat += self.TAGS["resto"]
            number_match += 1
        if "TY COZ" in lib:
            lib = "Bar Ty Coz"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "ALBATROS" in lib:
            lib = "Hôtel Albatros"
            cat += self.TAGS["autre"]
            number_match += 1
        if "AU VENT DES IL" in lib:
            lib = "Au vent des iles (resto)"
            cat += self.TAGS["resto"]
            number_match += 1
        if "LES 2 S" in lib:
            lib = "Blev Hir"
            cat += self.TAGS["resto"]
            number_match += 1
        if "LA TOMATE" in lib:
            lib = "La Tomate"
            cat += self.TAGS["resto"]
            number_match += 1
        if "EG VACATION RE" in lib:
            lib = "TODO : Abritel"
            number_match += 1
        if "GAMEFOUND" in lib:
            lib = "Gamefound"
            cat += self.TAGS["culture"]
            number_match += 1
        if "IZEE" in lib:
            lib = "Izee"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "LE TARA INN" in lib:
            lib = "Tara Inn"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "SNCF" in lib:
            lib = "SNCF"
            cat += self.TAGS["transport"]
            number_match += 1
        if "REMISE DE CHEQUES" in lib:
            lib = "TODO : Remise de chèque"
            number_match += 1
        if "PAPS N BABS" in lib:
            lib = "Paps n Babs (Bar)"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "PAPS N BABS" in lib:
            lib = "Paps n Babs (Bar)"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "CHAPITRES" in lib:
            lib = "Chapitres (Bar)"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "BELISOFT" in lib:
            lib = "Belisoft"
            cat += self.TAGS["autre"]
            number_match += 1
        if "ORIJINAL PIDE" in lib:
            lib = "Orijinal Pide"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "BURGER KING" in lib:
            lib = "Burger King"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "BARADO ZIC" in lib:
            lib = "Barado'Zic (Bar)"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "TARTINES D AUT" in lib:
            lib = "Tartines d'Autrefois"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LBM GLASGOW" in lib:
            lib = "Laboratoire d'Analyse Médicale Glasgow"
            cat += self.TAGS["santé"]
            number_match += 1
        if "POEM" in lib:
            lib = "Brasserie Poem"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "CB BIERE   MALT" in lib:
            lib = "Brasserie Bière & Malt"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "FRAIS IRREGULARITES ET INCIDENTS" in lib:
            lib = "Frais irrégularités de banque"
            cat += self.TAGS["banque"]
            number_match += 1
        if "ACHAT CB COTE BOUL CESS" in lib:
            lib = "Marie Blachère"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "AMAZON" in lib:
            lib = "Amazon"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "HARMONIE MUTUELLE" in lib:
            lib = "Harmonie mutuelle"
            cat += self.TAGS["santé"]
            number_match += 1
        if "PAYPAL" in lib:
            lib = "TODO : Paypal - check détails"
            cat += self.TAGS["check"]
            number_match += 1
        if "OTANTIK" in lib:
            lib = "Kebab : Otantik kebab"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "THE BLIND PIPE" in lib:
            lib = "The Blind Piper"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "COTISATION TRIMESTRIELLE" in lib:
            lib = "Frais Banque"
            cat += self.TAGS["banque"]
            number_match += 1
        if "BURGERS DE PAP" in lib:
            lib = "Burgers de Papa"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "LEROY MERLIN" in lib:
            lib = "Leroy Merlin"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "FOURNIL DE PAU" in lib:
            lib = "Boulangerie : Fournil de Pauline"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "ROI DE BRETAGN" in lib:
            lib = "Roi de Bretagne"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SAVEURS DU POT" in lib:
            lib = "Saveurs du potager (épicerie)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SAMMELKARTENMARK" in lib:
            lib = "MKM (Magic)"
            cat += self.TAGS["magic"]
            number_match += 1
        if "MAGIC CARD MARKET" in lib:
            lib = "MKM (Magic)"
            cat += self.TAGS["magic"]
            number_match += 1
        if "BOUCHERIE" in lib:
            lib = "Boucherie"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SABLON" in lib:
            lib = "Dr DU CORAIL"
            cat += self.TAGS["santé"]
            number_match += 1
        if "BRULERIE" in lib:
            lib = "Brulerie"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "CHEZ SEB" in lib:
            lib = "Primeur (Chez Seb)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "MAGIC CARD MARKET" in lib:
            lib = "MKM (Magic)"
            cat += self.TAGS["magic"]
            number_match += 1
        if "LA MAISON DU B" in lib:
            lib = "La maison du boulanger"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "VIERA" in lib:
            lib = "Virement Frederic Viera"
            cat += self.TAGS["loyer"]
            number_match += 1
        if "MIKA" in lib:
            lib = "Virement Mika"
            cat += self.TAGS["caché"]
            number_match += 1
        if "MAELISS" in lib:
            lib = "Virement Maeliss"
            cat += self.TAGS["caché"]
            number_match += 1
        if "AGIOS" in lib:
            lib = "Agios (remise ou pas)"
            cat += self.TAGS["banque"]
            number_match += 1
        if "MINIMUM FORFAITAIRE" in lib:
            lib = "Agios (remise ou pas)"
            cat += self.TAGS["banque"]
            number_match += 1
        if "PRELEVEMENT DE CARE" in lib:
            lib = "Don à CARE"
            cat += self.TAGS["don"]
            number_match += 1
        if "INTERMARCHE" in lib:
            lib = "Intermarché"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "MISTINGUETTE" in lib:
            lib = "Primeur (Mistinguette)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "PHIE NICOLAS" in lib:
            lib = "Pharmacie Nicolas"
            cat += self.TAGS["santé"]
            number_match += 1
        if "LA ROSE CREMIE" in lib:
            lib = "La Rose Crémière (Fromage)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "CB LA POSTE" in lib:
            lib = "La poste"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "LA POSTE TELECOM" in lib:
            lib = "La poste mobile"
            cat += self.TAGS["abos"]
            number_match += 1
        if "LECLERC" in lib:
            lib = "Leclerc"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "MARCHE PLUS" in lib:
            lib = "Marché Plus (?) / Carrefour City ?"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "DECATHLON" in lib:
            lib = "Décathlon"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "GES PAPETERIE" in lib:
            lib = "Bureau Vallée"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "KERICCI" in lib:
            lib = "Kericci (épicerie)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LUDIK ADDICT" in lib:
            lib = "Ludik Addict"
            cat += self.TAGS["culture"]
            number_match += 1
        if "YFOG" in lib:
            lib = "Yfog (Halles Saint Martin)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SUBWAY" in lib:
            lib = "Subway"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "FOURNIL-SS" in lib:
            lib = "Boulangerie (Fournil SS CON?)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "ON FAIT DES GA" in lib:
            lib = "Pâtisserie On fait des Gateaux"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "EURODIF" in lib:
            lib = "Bouchara"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "CASA DE PAPILL" in lib:
            lib = "La Casa de Papilles"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "PATRONAGE LAIQUE" in lib:
            lib = "PLPR"
            cat += self.TAGS["culture"]
            number_match += 1
        if "MUSIC STAR" in lib:
            lib = "Music Star"
            cat += self.TAGS["culture"]
            number_match += 1
        if "HELLOASSO" in lib:
            lib = "Hello Asso : TODO Check raison"
            number_match += 1
        if "DE JAURIAS" in lib:
            lib = "Remboursement Flavie : TODO Check raison"
            number_match += 1
        if "ARCHE A JEUX" in lib:
            lib = "L'arche à Jeux"
            cat += self.TAGS["culture"]
            number_match += 1
        if "MAGIC CARD MARKET" in lib:
            lib = "MKM (Magic)"
            cat += self.TAGS["culture"]
            number_match += 1
        if "RESTAU ISTAMBU" in lib:
            lib = "Kebab (Istambul)"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "WILLIAM" in lib:
            lib = "Virement William"
            cat += self.TAGS["caché"]
            number_match += 1
        if "CARREFOUR" in lib:
            lib = "Carrefour"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "DELIVEROO" in lib:
            lib = "Deliveroo"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "DOCTOLIB" in lib:
            lib = "Doctolib"
            cat += self.TAGS["santé"]
            number_match += 1
        if "TI COOP" in lib:
            lib = "Ti Coop"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "POISSONNERIE" in lib:
            lib = "Poissonerie"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LE HETRE" in lib:
            lib = "Editeur livres Le Hêtre"
            cat += self.TAGS["culture"]
            number_match += 1
        if "STEAMGAMES" in lib:
            lib = "Steam (jeux)"
            cat += self.TAGS["culture"]
            number_match += 1
        if "CINEMA LES STU" in lib:
            lib = "Cinéma Les Studios"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "BIOCOOP" in lib:
            lib = "Biocoop"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "AZRA MARKET" in lib:
            lib = "Azra Market"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "CROC JEUX" in lib:
            lib = "Croc Jeux"
            cat += self.TAGS["culture"]
            number_match += 1
        if "BREDIS" in lib:
            lib = "Primeur (bredis)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "THE COTTAGE" in lib:
            lib = "The Cottage"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "LA CORBEILLE D" in lib:
            lib = "Primeur (Halles Saint Louis, La Corbeille d'Or)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "SITE WEB" in lib:
            lib = "Savonnerie La Licorne"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "CARREFOUR" in lib:
            lib = "Carrefour"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "DELIVEROO" in lib:
            lib = "Deliveroo"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "DOCTOLIB" in lib:
            lib = "Doctolib"
            cat += self.TAGS["santé"]
            number_match += 1
        if "TI COOP" in lib:
            lib = "Ti Coop"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "POISSONERIE" in lib:
            lib = "Poissonerie"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LE HETRE" in lib:
            lib = "Editeur livres Le Hêtre"
            cat += self.TAGS["culture"]
            number_match += 1
        if "STEAMGAMES" in lib:
            lib = "Steam (jeux)"
            cat += self.TAGS["culture"]
            number_match += 1
        if "CINEMA LES STU" in lib:
            lib = "Cinéma Les Studios"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "BIOCOOP" in lib:
            lib = "Biocoop"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "AZRA MARKET" in lib:
            lib = "Azra Market"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "CROC JEUX" in lib:
            lib = "Croc Jeux"
            cat += self.TAGS["culture"]
            number_match += 1
        if "BREDIS" in lib:
            lib = "Primeur (bredis)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "THE COTTAGE" in lib:
            lib = "The Cottage"
            cat += self.TAGS["sortie"]
            number_match += 1
        if "LA CORBEILLE D" in lib:
            lib = "Primeur (Halles Saint Louis, La Corbeille d'Or)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "MEAT COUTURE" in lib:
            lib = "Boucherie (Meat Couture, Halles Saint Louis)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "LIBRAIRIE DIAL" in lib:
            lib = "Dialogues (Librairie)"
            cat += self.TAGS["culture"]
            number_match += 1
        if "GEANT" in lib:
            lib = "Géant"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "CATHERINE COUSSE" in lib:
            lib = "CHECK : Remboursement Maman Mika"
            number_match += 1
        if "PHARMACIE NICO" in lib:
            lib = "Pharmacie Nico (PR)"
            cat += self.TAGS["santé"]
            number_match += 1
        if "RETRAIT DAB" in lib:
            lib = "Retrait"
            cat += self.TAGS["dab"]
            number_match += 1
        if "Netflix" in lib:
            lib = "Netflix"
            cat += self.TAGS["abos"]
            number_match += 1
        if "NETFLIX" in lib:
            lib = "Netflix"
            cat += self.TAGS["abos"]
            number_match += 1
        if "LAURAMADIS" in lib:
            lib = "Carrefour Express"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "CELIO" in lib:
            lib = "Celio"
            cat += self.TAGS["vêtement"]
            number_match += 1
        if "MC DONALDS" in lib:
            lib = "McDo"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "TROADEC OLIVIE" in lib:
            lib = "T Shirt"
            cat += self.TAGS["cadeau"]
            number_match += 1
        if "IKEA" in lib:
            lib = "IKEA"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "MAISON DU THE" in lib:
            lib = "Maison du thé"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "MAISONS DU MON" in lib:
            lib = "Maison du Monde"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "QUEMENEUR STEP" in lib:
            lib = "Dr Quemeneur (Ostéo)"
            cat += self.TAGS["santé"]
            number_match += 1
        if "LE BODRUM" in lib:
            lib = "Le Bodrum (Kebab)"
            cat += self.TAGS["fastfood"]
            number_match += 1
        if "BUREAU VALLEE" in lib:
            lib = "Burreau Vallée"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "THOMANN.DE" in lib:
            lib = "Thomann"
            cat += self.TAGS["culture"]
            number_match += 1
        if "CDISCOUNT" in lib:
            lib = "CDiscount"
            cat += self.TAGS["matériel"]
            number_match += 1
        if "LES CAVES SAVA" in lib:
            lib = "Cave (saint martin ?)"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "IDEAL COIFFURE" in lib:
            lib = "Idéal Coiffure"
            cat += self.TAGS["santé"]
            number_match += 1
        if "COOPER BRANCH" in lib:
            lib = "Ty Veggie"
            cat += self.TAGS["bouffe"]
            number_match += 1
        if "FRAIS VIREMENT INSTANTANE" in lib:
            lib = "Frais banque"
            cat += self.TAGS["banque"]
            number_match += 1
        if "MC DO LUGARE" in lib:
            lib = "Macdo"
            cat = self.TAGS["fast-food"]
            number_match += 1
        return lib, cat, number_match