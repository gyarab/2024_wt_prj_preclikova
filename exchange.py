import httpx 

import pprint 

print("Online prevodnik men dle cnb.cz")

url ="https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

r = httpx.get(url)

in_array = r.text.split("\n")

#print(in_array)

radek_eur = ""
for line in in_array: 
    if "|EUR|" in line:
        radek_eur = line

radek_array = radek_eur.split("|")

kurz_str = radek_array[-1]
kurz_str = kurz_str.replace(",", ".")

kurz = float(kurz_str)

druhPrevodu = "x"
while druhPrevodu != "E" and druhPrevodu != "C":

    if "x" != druhPrevodu:
        print(f"Neznamy druh prevodu {druhPrevodu}")
    druhPrevodu = input("Zadej druh prevodu C=CZK/EUR nebo E=EUR/CZK ").upper()  

    if "E" == druhPrevodu:
        menaCastka = "EUR"
        menaVysledek = "CZK"

    if "C" == druhPrevodu:
        menaCastka = "CZK"
        menaVysledek = "EUR"
        kurz = 1/kurz

print(f"Kurz {menaCastka} na {menaVysledek} je {kurz}")
castkaZadana = False
while castkaZadana != True:
    try:
        castka = input(f"Zadej castku v {menaCastka} ") 
        castkaCislo = float(castka)
        castkaZadana = True
    except ValueError:
        print(f"Zadana castka {castka} neni cislo")

result = castkaCislo * kurz 
print(f"To je v {menaVysledek} : {result}")
