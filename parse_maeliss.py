#!/usr/bin/python3
"""Conversion des données de banque pour la banque postale (Maëliss)"""

import sys
import csv
import argparse


def parse_cli() -> argparse.ArgumentParser:
    """Simpler version"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'csvfile',
        type=str,
        help='fichier csv de la banque postale à éditer'
    )
    parser.add_argument(
        '-o',
        type=str,
        help='fichier csv à écrire'
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_cli()

    with open(args.csvfile, encoding="ISO-8859-14") as fd:
        for line in fd:
            if not line.strip():  # empty line: csv data starts here
                break

        reader = csv.reader(fd, delimiter='\t')

        if args.o:
            ofd = open(args.o, 'w')
        else:
            ofd = sys.stdout

        writer = csv.writer(ofd, delimiter=',')
        header = next(reader)
        writer.writerow("Date,Libellé,Montant,Tag,Type".split(','))

        for date, libelle, montant_eur in reader:
            day, month, year = date.split('/')
            date_fmt = f"{year}/{month}/{day}"

            # Nettoyage des libellés et des montants
            libelle = libelle.replace(" CARTE NUMERO", "").strip()
            montant_eur = montant_eur.replace(',', '.')

            line = (date_fmt, libelle, montant_eur, "", "")
            writer.writerow(line)

        if args.o:
            ofd.close()
