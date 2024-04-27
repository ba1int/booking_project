# gondoskodik ez a resz arrol, hogy a felhasznalo ne hagyjon ures mezot
def get_non_empty_input(prompt):
    value = input(prompt)
    while value.strip() == "":  # Eltávolítja a szóközöket az elejéről és a végéről, majd ellenőrzi, hogy üres-e
        print("Ez a mező nem lehet üres. Kérem, próbálja újra.")
        value = input(prompt)
    return value
