from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    voor = korting * 36
    fractional_separator = ","
    voor_1 = "{:,.2f}". format(voor)
    if fractional_separator == ",":
        main_currency, fractional_currency = voor_1.split(".")[0], voor_1.split(".")[1]
        new_main_currency = main_currency.replace(",", ".")
        voor_1 = new_main_currency + fractional_separator + fractional_currency
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {voor_1} euro."
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))

inkomsten = 220, 430, 125, 160, 205, 90, 345
def inkomsten_totaal(inkomsten):
    totaal= sum(inkomsten)
    bedrag_1= totaal*0.09
    fractional_separator = ","
    bedrag = "{:,}". format(bedrag_1)
    if fractional_separator == ",":
        main_currency, fractional_currency = bedrag.split(".")[0], bedrag.split(".")[1]
        new_main_currency = main_currency.replace(",", ".")
        bedrag = new_main_currency + fractional_separator + fractional_currency
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return uitvoer
print(inkomsten_totaal(inkomsten))

mijn_lijst = 220, 430, 125, 160, 205, 90, 345
def laag_en_hoog(mijn_lijst):
    laag=min(mijn_lijst)
    hoog=max(mijn_lijst)
    return laag, hoog
print(laag_en_hoog(mijn_lijst))

# Import statistics Library
import statistics
def gemiddeld(mijn_list):
    gem= statistics.mean(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gem} euro."
    return uitvoer
print(gemiddeld(mijn_lijst))

invoer_lijst = 10,5,3,2,1,2,9
def meervoudig(invoer_lijst):
    meer= laag_en_hoog(invoer_lijst)
    return meer
print(meervoudig(invoer_lijst))

invoer_lijst_2 = 10,5,3
def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    uitvoer=mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie(invoer_lijst_2))





