# Kalkulačka v Pythonu  
Jednoduchá kalkulačka vytvořená v programovacím jazyce Python. Tento projekt je ideální pro začátečníky, kteří se chtějí naučit základní principy programování, jako je práce s funkcemi, vstupy uživatele, podmínkami a cykly.  

---

## Jak funguje?  
Tato kalkulačka umožňuje uživateli provádět základní matematické operace, jako jsou:  
1. Sčítání  
2. Odčítání  
3. Násobení  
4. Dělení  

Uživatel si zvolí operaci, zadá dvě čísla a kalkulačka provede výpočet. Program se opakuje, dokud uživatel nezvolí možnost „Konec“.  

---

## Co se v kódu naučíš?

1. **Práce s funkcemi:**  
Funkce `kalkulacka()` organizuje celý program do přehledného bloku, který lze opakovaně volat.  

2. **Zpracování vstupů od uživatele:**  
- Použití `input()` pro zadávání údajů.  
- Konverze vstupů na čísla pomocí `float()`.  

3. **Podmínky a větvení:**  
- `if`, `elif`, `else` určují, která operace se provede na základě uživatelského výběru.  
- Zpracování chyb, jako je dělení nulou.  

4. **Cyklus:**  
- `while True` zajišťuje, že kalkulačka bude fungovat, dokud uživatel nezvolí možnost „Konec“.  

---

## Jak spustit kalkulačku?

### 1. Požadavky:  
- Python 3.6 nebo novější.  

### 2. Kroky:  
1. Ujisti se, že máš Python nainstalovaný na svém počítači.  
- [Stáhni Python](https://www.python.org/downloads/)  
2. Stáhni nebo zkopíruj kód do souboru, například `kalkulacka.py`.  
3. Otevři terminál a přejdi do složky, kde máš uložený soubor.  
4. Spusť příkaz:  
```bash
python kalkulacka.py
```

---

## Možnosti rozšíření

Tento projekt je skvělý základ, který lze snadno rozšířit a přizpůsobit. Tady je několik nápadů, jak kalkulačku vylepšit:  

### 1. **Pokročilé operace:**  
   - Přidej možnost počítat mocniny (`x^y`) nebo odmocniny (`√x`).  
   - Přidej modulární dělení (`%`), které vrací zbytek po dělení.  
   - Zaveď podporu pro více matematických funkcí, jako jsou logaritmy, sinus nebo kosinus.  

### 2. **Zpracování více čísel:**  
   - Umožni uživateli zadat více než dvě čísla najednou. Například:  
     ```
     Zadej čísla oddělená čárkou: 10, 20, 30
     Výsledek (součet): 60
     ```

### 3. **Historie výpočtů:**  
   - Ukládej všechny výpočty do seznamu a umožni uživateli zobrazit historii operací.  
   - Příklad:  
     ```
     Historie:
     10 + 5 = 15
     20 / 4 = 5
     ```

### 4. **Zlepšení uživatelského rozhraní:**  
   - Přidej lepší textové menu s jasnější navigací a ověřováním vstupů.  
   - Použij knihovny jako `Tkinter` nebo `PyQt` pro vytvoření jednoduchého grafického rozhraní.  

### 5. **Práce s pamětí:**  
   - Umožni uživateli uložit výsledek do paměti a použít ho v dalším výpočtu.  
   - Příklad:  
     ```
     Uloženo do paměti: 15
     Další operace: 15 + 10 = 25
     ```

---

## Feedback a podpora

Máš otázky ohledně kódu nebo se chceš pochlubit svým vlastním rozšířením? Napiš mi! 😊  
Rád se podívám na tvůj pokrok a poradím ti, jak posunout své dovednosti na další úroveň.  

