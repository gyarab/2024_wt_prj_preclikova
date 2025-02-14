import httpx 
import pprint import pprint

print("Online prevodnik men dle cnb.cz")

url ="https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025"

r =httpx.get(url)

in_array = r.text.split("\n")

#print(in_array)

radek_eur= ""
for line in in_array: 
    if "|EUR|" in line:
        radek_eur = line

radek_array = radek_eur.split("|")

kurz_str = radek_array[-1]

kurz_str = kurz_str.replace(",",".")

kurz = float(kurz_str)
   
pprint(kurz)
    
castka = intut("Zadej castku v CZK") 
result = int(castka) * kurz 
print(f"To je v EUR: {result}")
