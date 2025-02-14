import httpx

print("Online")

url ="https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025"

r =httpx.get(url)

in_array = r.text.split("\n")
print(in_array)

for line in r.text: 
    if "|EUR|" in line:
    
     castka = intut("Zadej castku v CZK")
     result = int(castka) *25
     print(f"To je v EUR: {result}")