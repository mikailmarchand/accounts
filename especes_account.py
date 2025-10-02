from abc import ABC

from .abstract_account import AbstractAccount


class EspecesAccount(AbstractAccount, ABC):

    def __init__(self):
        super(EspecesAccount, self).__init__(
            path="D:\\Mikail\\Papiers importants\\Comptes\\Especes\\",
            preheader=0,
            bank="Especes",
            extension=".csv",
            delimiter=","
        )

    def split_date(self, date):
        a, m, j = date.split("/")
        return j, m, a

    def split_date_lib_eur(self, line, delimiter):
        try:
            splitted_line = line.split(delimiter)
            date = splitted_line[0]
            if "remb" in splitted_line[-1]:
                remb = -1
                lib = ",".join(splitted_line[1:-3])
            else:
                remb = 0
                lib = ",".join(splitted_line[1:-2])
            eur = splitted_line[-2 + remb]
            cat = splitted_line[-1 + remb]
            date = date[2:]
            eur = eur.replace("â\x82Ỳ", "")
            cat = cat.strip().replace("Ã©", "é").replace("ÃẂ", "ê")
        except Exception as e:
            # breakpoint()
            raise e
        return date, lib, eur, cat

    def category_parsing(self, lib, cat):
        return lib, cat, 1