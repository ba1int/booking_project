# Szállodai Foglalási Rendszer

Ez a Python program egy szállodai foglalási rendszert valósít meg. A rendszer lehetővé teszi a szállodák, szobák és foglalások kezelését. A felhasználók hozzáadhatnak új szállodákat és szobákat, foglalhatnak szobákat, lemondhatják a foglalásokat, és listázhatják a meglévő foglalásokat.

## Funkciók

- Szállodák hozzáadása
- Szobák hozzáadása a szállodákhoz
- Szobák foglalása megadott dátumra
- Foglalások lemondása
- Foglalások listázása
- Foglalható szobák listázása megadott dátumra

## Osztályok

### `Szoba`

Ez az absztrakt alaposztály a szobákat reprezentálja. Tartalmazza a szobaszámot és az alapárat. Az `ar` metódus absztrakt, így a leszármazott osztályoknak kell megvalósítaniuk.

### `EgyAgyasSzoba`

A `Szoba` osztály leszármazottja, amely az egyágyas szobákat reprezentálja. Az `ar` metódus az alapárat adja vissza.

### `KetAgyasSzoba`

A `Szoba` osztály leszármazottja, amely a kétágyas szobákat reprezentálja. Az `ar` metódus az alapár 1,5-szeresét adja vissza.

### `Szalloda`

Ez az osztály a szállodákat reprezentálja. Tartalmazza a szálloda nevét és a hozzá tartozó szobák listáját. Lehetővé teszi új szobák hozzáadását.

### `Foglalas`

Ez az osztály a foglalásokat reprezentálja. Tartalmazza a szállodát, a szobát és a foglalás dátumát. Az `ar` metódus a szoba árát adja vissza.

### `FoglalasiRendszer`

Ez az osztály a foglalási rendszert valósítja meg. Tartalmazza a szállodák és foglalások listáját. Lehetővé teszi új szállodák hozzáadását, szobák foglalását, foglalások lemondását, foglalások és foglalható szobák listázását.

## Használat

A program futtatásakor egy alapértelmezett szálloda és néhány szoba kerül hozzáadásra, valamint néhány alapértelmezett foglalás. Ezután a felhasználó interaktív módon adhat hozzá új szállodákat és szobákat.

A főmenüben a következő lehetőségek állnak rendelkezésre:

1. Szoba foglalás
2. Szoba foglalás lemondása
3. Foglalások listázása
4. Kilépés

A megfelelő opció kiválasztásával a felhasználó foglalhat szobákat, lemondhatja a foglalásokat, listázhatja a meglévő foglalásokat, vagy kiléphet a programból.

## Példa

```
Üdv a feltöltési promptban! Adja meg a szállodákat és szobákat.
Adja meg a szálloda nevét (vagy 'enter' a befejezéshez): Hotel Alpha
Adja meg a szoba számát (vagy 'enter' a következő szállodához): 101
Adja meg a szoba számát (vagy 'enter' a következő szállodához): 102
Adja meg a szoba számát (vagy 'enter' a következő szállodához):
Adja meg a szálloda nevét (vagy 'enter' a befejezéshez): Hotel Beta
Adja meg a szoba számát (vagy 'enter' a következő szállodához): 201
Adja meg a szoba számát (vagy 'enter' a következő szállodához):
Adja meg a szálloda nevét (vagy 'enter' a befejezéshez):
Adatok feltöltve. Üdv a foglaló promptban!

Válasszon az alábbi lehetőségek közül:
1. Szoba foglalás
2. Szoba foglalás lemondása
3. Foglalások listázása
4. Kilépés
Adja meg a választását (1-4): 1
Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): 2024-07-10
Foglalható szobák 2024-07-10 dátumra:
Szálloda: 0
Szoba: 303, Típus: Egyágyas, Ár: 10000 Ft

Szálloda: Hotel Alpha
Szoba: 101, Típus: Egyágyas, Ár: 10000 Ft
Szoba: 102, Típus: Kétágyas, Ár: 15000 Ft

Szálloda: Hotel Beta
Szoba: 201, Típus: Egyágyas, Ár: 10000 Ft

Adja meg a szálloda nevét: Hotel Alpha
Adja meg a szoba számát: 101
Foglalás létrehozva. Ár: 10000 Ft

Válasszon az alábbi lehetőségek közül:
1. Szoba foglalás
2. Szoba foglalás lemondása
3. Foglalások listázása
4. Kilépés
Adja meg a választását (1-4): 3
Szálloda: 0, Szoba: 201, Dátum: 2024-06-15
Szálloda: 0, Szoba: 102, Dátum: 2024-06-20
Szálloda: 0, Szoba: 303, Dátum: 2024-06-25
Szálloda: 0, Szoba: 201, Dátum: 2024-07-01
Szálloda: 0, Szoba: 102, Dátum: 2024-07-05
Szálloda: Hotel Alpha, Szoba: 101, Dátum: 2024-07-10

Válasszon az alábbi lehetőségek közül:
1. Szoba foglalás
2. Szoba foglalás lemondása
3. Foglalások listázása
4. Kilépés
Adja meg a választását (1-4): 4
Köszönjük, hogy használta a foglalási rendszert. Viszontlátásra!
```

_DISCLAIMER: a README.md AI által generált._
