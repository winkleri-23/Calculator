def kalkulacka():
    print("Vítej v kalkulačce!")
    print("Vyber operaci:")
    print("1 - Sčítání")
    print("2 - Odčítání")
    print("3 - Násobení")
    print("4 - Dělení")
    print("5 - Konec")

    while True:
        volba = input("Zadej číslo operace (1–5): ")

        if volba == "5":
            print("Děkujeme za použití kalkulačky. Nashledanou!")
            break

        cislo1 = float(input("Zadej první číslo: "))
        cislo2 = float(input("Zadej druhé číslo: "))

        if volba == "1":
            print(f"Výsledek: {cislo1 + cislo2}")
        elif volba == "2":
            print(f"Výsledek: {cislo1 - cislo2}")
        elif volba == "3":
            print(f"Výsledek: {cislo1 * cislo2}")
        elif volba == "4":
            if cislo2 != 0:
                print(f"Výsledek: {cislo1 / cislo2}")
            else:
                print("Chyba: dělení nulou není možné!")
        else:
            print("Neplatná volba. Zkus to znovu.")

kalkulacka()
