from abc import ABC, abstractmethod
import csv
import os
from pathlib import Path


class AbstractAccount(ABC):
    DATA_ROOT = Path(__file__).resolve().parent / "Comptes"

    TAGS = {"abos": "abonnement", "abonnement": "abonnement", "autre": "autre", "caché": "caché", "cadeau": "cadeau",
            "dab": "dab", "don": "don", "emménagement": "emménagement", "loyer": "loyer", "matériel": "matériel",
            "perso": "perso", "resto": "restau", "santé": "santé", "sante": "santé", "sortie": "sortie",
            "vêtement": "vêtements", "remboursement": "remboursement", "salaire": "salaire", "banque": "banque",
            "bouffe": "bouffe", "magic": "magic", "culture": "culture", "check": "TODO : Check catégorie",
            "vÃẂtement": "vêtements", "vacances": "vacances", "économies": "economie", "écos": "economie",
            "économie": "economie", "éco": "economie", "economie": "economie", "eco": "economie", "ecos": "economie",
            "economies": "economie", "grossesse": "grossesse", "impôts": "impots", "impots": "impots",
            "azenor": "azenor", "Azenor": "azenor", "evl": "evl", "vetements": "vêtements", "vetement": "vêtements",
            "fastfood": "fastfood", "transport": "transport", "coiffeur": "coiffeur", "autres": "autre",
            "fast-food": "fastfood", "coiffure": "coiffeur", "abo": "abonnement", "sport": "sport", "snap": "snap",
            "materiel": "matériel", "abonnements": "abonnement",
            }

    IN_TAGS = [x for cat, x in TAGS.items() if cat in ("vêtement", "remboursement", "salaire", "banque", "caché")]

    def __init__(self, path, preheader, bank, extension, delimiter):
        self.path = self.DATA_ROOT / path
        self.__preheader = preheader
        self.__bank = bank
        self.__extension = extension
        self.__delimiter = delimiter

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @property
    def preheader(self):
        return self.__preheader

    @preheader.setter
    def preheader(self, value):
        self.__preheader = value

    @property
    def bank(self):
        return self.__bank

    @bank.setter
    def bank(self, value):
        self.__bank = value

    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        self.__extension = value

    @property
    def delimiter(self):
        return self.__delimiter

    @delimiter.setter
    def delimiter(self, value):
        self.__delimiter = value

    @abstractmethod
    def category_parsing(self, lib, cat):
        pass

    @abstractmethod
    def split_date(self, date):
        pass

    @abstractmethod
    def split_date_lib_eur(self, line, delimiter):
        pass

    def __str__(self):
        return f"Compte {self.__bank}"

    def file_present(self, date):
        return (self.path / f"{date}{self.extension}").is_file()

    def format_bank_file(self, date):
        path_file = self.path / f"{date}{self.extension}"
        output_path = self.path / f"{date}_parsable_temp{self.extension}"
        with open(path_file, encoding='ISO-8859-14') as input_file:
            with open(output_path, "w", encoding="utf-8") as csv_file:
                remb = False
                bank = self.bank
                writer = csv.writer(csv_file, delimiter=",", lineterminator="\n")
                writer.writerow('Date,Banque,Libellé,Montant,Tag,Type'.split(','))
                all_good_lines = [
                    l for l in input_file.readlines(False)[self.preheader:] if l.strip != ""
                ]
                for line in all_good_lines:
                    try:
                        date, lib, eur, cat = self.split_date_lib_eur(line, self.delimiter)
                    except Warning as w:
                        print("Opération refusée sur ligne", line)
                        continue
                    except Exception as e:
                        raise e
                    try:
                        j, m, a = self.split_date(date)
                        date = "/".join([a, m, j])
                        eur = str(eur).replace(",", ".")
                        remb = float(eur) > 0
                        lib, cat, number_match = self.category_parsing(lib, cat)
                        eur_parts = eur.split(".")
                        if len(eur_parts) > 1:
                            cents = eur_parts[1]
                            if len(cents) == 1:
                                cents = cents + "0"
                        else:
                            cents = "00"
                        eur_formatted = eur_parts[0] + "." + cents + "€"
                        if remb and cat not in self.IN_TAGS:
                            to_print = (date, bank, lib, eur_formatted, cat, "remboursement",)
                        else:
                            to_print = (date, bank, lib, eur_formatted, cat)
                        if number_match == 0:
                            print(date, lib, eur, "CHECK SI OK !")
                            writer.writerow(to_print)
                        elif number_match == 1:
                            writer.writerow(to_print)
                        else:
                            breakpoint()
                            raise Exception("Plusieurs matchs ! A analyser !", date, lib, eur, cat)
                    except Exception as e:
                        breakpoint()
                        raise e