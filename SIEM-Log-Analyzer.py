print("=== ZASTRZEŻONY SYSTEM ANALIZY LOGÓW (SIEM) ===")

nieudane_proby = {}   

czarna_lista   = []

with open('server_logs.txt', 'r', encoding='utf-8') as plik:
    for linia in plik:
        linia  = linia.strip()
        
        if 'LOGIN_FAILED' in linia:
            elementy = linia.split(" ")
            ip = elementy[4]
            
            if ip in nieudane_proby:           
                nieudane_proby[ip] += 1
            else:
                nieudane_proby[ip] = 1
            
            if nieudane_proby[ip] > 2 and ip not in czarna_lista:
                czarna_lista.append(ip)

print("\n[i] Statystyki błędnych logowań per IP:")
for ip, ilosc in nieudane_proby.items():  
    print(f" --> IP: {ip} | Próby: {ilosc}")  
          
print("\n[🚨] GENEROWANIE REGUŁ FIREWALL (DO ZABLOKOWANIA):")
if czarna_lista:
 for zly_ip in czarna_lista:
  print(f"[-] REKOMENDACJA: Zablokuj ruch z IP: {zly_ip} -> Powód: Atak Brute-Force")
else:
    print("[+] Brak adresów IP do zablokowania. System bezpieczny.")
print("==============================================")