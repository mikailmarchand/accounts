import os
import csv
import pandas as pd
from .lbp_account import LBPAccount as LA
from .lbpmae_account import LBPMaeAccount as LMA
from .trmae_account import TRMaeAccount as TMA
from .cmb_account import CMBAccount as CMB
from .especes_account import EspecesAccount as ESP

pd.options.display.float_format = '{:,.2f}'.format

def new_main(date, full):
    cmb = CMB()
    la = LA()
    lma = LMA()
    # tma = TMA()
    # esp = ESP()
    all_accounts = [
        cmb,
        la,
        lma
    ]
    total_data = []
    for account in all_accounts:
        print(f"Dealing with package {account}")
        test = account.file_present(date)
        if account.file_present(date):
            output_file = account.path / f"{date}_parsable_temp{account.extension}"
            test2 = (not os.path.isfile(output_file))
            if (
                (not os.path.isfile(output_file))
                or full
            ):
                print("Checking for file", output_file)
                print("CSV Final file doesn't exist : computation ...")
                account.format_bank_file(date)
            try:
                csv_final_data = pd.read_csv(output_file, parse_dates=["Date"])
            except UnicodeDecodeError:
                csv_final_data = pd.read_csv(output_file, parse_dates=["Date"], encoding="latin-1")
            csv_final_data["Montant"] = csv_final_data["Montant"].str.replace("€", "")
            csv_final_data["Montant"] = csv_final_data["Montant"].str.replace("", "")
            csv_final_data["Libellé"] = csv_final_data["Libellé"].str.replace("", "€")
            csv_final_data["Montant"] = pd.to_numeric(csv_final_data["Montant"])
            total_data.append(csv_final_data)
        else:
            print("File not found")
    if total_data == []:
        print("Données vides")
        exit
    df = pd.concat(total_data)
    # Restitution
    print("Apparté : montant caché (should be zéro) :", df[df["Tag"] == "caché"]["Montant"].sum())
    print(df[df["Tag"] == "caché"][["Date", "Banque", "Libellé", "Montant"]])
    print()
    grouped_by_df = df[df["Tag"] != "caché"].groupby(['Tag']).sum(numeric_only=True)
    pd.set_option("display.max_columns", 10)
    pd.set_option("display.width", 400)
    print("Dépenses totales par catégories :")
    print(grouped_by_df)
    print()
    print("Total balance :")
    print(df[df["Tag"] != "caché"]["Montant"].sum())
    df.loc[df["Tag"].isna(), "Tag"] = "No Given Category"
    for tag in sorted(df["Tag"].unique()):
        if tag != "caché":
            print("################################e"
                  "############################")
            print("Détails par catégorie =>", tag, df[df["Tag"] == tag]["Montant"].sum())
            print()
            print(df[df["Tag"] == tag][["Date", "Banque", "Libellé", "Montant"]])
            print("############################################################")
            print()


if __name__ == '__main__':
    date = "25dec"
    full = False
    new_main(date, full)