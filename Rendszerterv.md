# Fejezetek
- [Rendszer célja](#1-rendszer-célja)
- [Projektterv](#2-projektterv)
- [Üzleti folyamatok modellje](#3-üzleti-folyamatok-modellje)
- [Követelmények](#4-követelmények)
- [Funkcionális terv](#5-funkcionális-terv)
- [Fizikai környezet](#6-fizikai-környezet)
- [Architekturális terv](#7-architekturális-terv)
- [Implementációs terv](#8-implementációs-terv)
- [Tesztterv](#9-tesztterv)
- [Telepítési terv](#10-telepítési-terv)
- [Karbantartási terv](#11-karbantartási-terv)


# 1. Rendszer célja

A hírportál célja egy olyan platform létrehozása, ahol a felhasználók regisztrálhatnak, bejelentkezhetnek, híreket írhatnak, és ezzel social credit rendszert használhatnak. A rendszer célja a minőségi tartalom előmozdítása és a felhasználói közösség felelősségteljes viselkedésének ösztönzése.

# 2. Projektterv

- **Felhasználói interfész létrehozása**
    - Home screen
    - Regisztrálás
    - Bejelentkezés
    - Hírírás
    - Aktivitás ellenőrzés
- **Social credit mechanizmus kidolgozása**
    - Fiókjogok állítása social credit alapján:
        - Alacsony szintnél hírírás jogának elvétele.
        - Nagyon alacsony szintnél fiók törlése.


# 3. Üzleti folyamatok modellje

1. **Felhasználói regisztráció**:
    - A felhasználó megadja a szükséges adatokat.
    - A szükséges adatok közé tartozik a név, e-mail cím, jelszó.
    - Ezek az adatok adatbázisban kerülnek mentésre.

2. **Bejelentkezés**:
    - A felhasználó a regisztrált e-mail címével és jelszavával tud belépni.
    - A rendszer az adatbázisban tárolt adatokat ellenőrzi a bejelentkezés során.
3. **Anonymous felhasználó**:
    - Az anonymous felhasználók a nem regisztrált, nem bejelentkezett felhasználók.
    - Az anonymous felhaszálók olvashatják a közzé tett híreket, de nem reagálhatnak rájuk.
    - Az anonymous felhasználók nem írhatnak híreket.
3. **Hírírás**:
    - A felhasználó hírt írhat a portálon, amit közzé tehet az oldalon.
    - A felhasználó által írt híreket minden felhasználó, illetve anonym felhasználó olvashatja.
4. **Social credit**:
    - A regisztrált felhasználók social creditet szerezhetnek illetve veszíthetnek el.
    - Alacsony social credit szintnél a felhasználó elveszti hírírási jogát.
    - Nagyon alacsony social credit szintnél a felhasználó fiókja törlődik.

# 4. Követelmények

1. ### **Funkcionális követelmények**:
    - Regisztrációs és bejelentkezési rendszer.
    - Hírek írásának és olvasásának funkciója.
    - Social credit rendszer integrálása.
2. ### **Nem funkcionális követelmények**:
    - Magas szintű biztonság.
    - Felhasználóbarát felület.
    - Teljesítmény és skálázhatóság.

# 5. Funkcionális terv

### **A rendszer fő funkciói a következők**:

- Felhasználói fiók létrehozása, kezelése.
- Hírek létrehozása ás publikálása az oldalon.
- Social credit nyomon követése és kezelése.
- Statisztikák és riportok készítése a felhasználók aktivitásáról.

# 6. Fizikai környezet


# 7. Architekturális terv

# 8. Adatbázis terv

# 9. Implementációs terv
1. **Kezdeti fejlesztés**:
    - A felhasználói regisztráció, bejelentkezés létrehozása.
    - Adatbázis implementálása a felhasználói adatok tárolására
    - GUI fejlesztése.
2. **Funkcionális fejlesztés**:
    - Az hírek közzétételének, social credit manipulálásának, nem megbízható források letiltásának implementálása.<br>
4. **Tesztelés**:
    - Minden funkció tesztelése különböző felhasználói forgatókönyvekkel.<br>
5. **Finomítás**:
    - Az esetleges hibák javítása és az alkalmazás teljesítményének optimalizálása.
    - A fejlesztés során folyamatosan figyelemmel kísérjük a kód minőségét és a legjobb gyakorlatokat alkalmazzuk, hogy a karbantartás és a további fejlesztések a jövőben zökkenőmentesen valósuljanak meg, végig törekedünk a tiszta kódra.
6. **Verziókezelés**:
    - A projekt során verziókezelő rendszert használunk a kód nyomon követésére és a csapatmunkához való alkalmazkodás érdekében.

# 10. Tesztterv

# 11. Telepítési terv

# 12. Karbantartási terv

# 13. Képernyő terv

# 14. Fogalomtár

- **Adatbázis**: Az adatbázis egy strukturált adattároló, amely lehetővé teszi adatok rendszerezett, biztonságos és hatékony tárolását, lekérdezését és kezelését (Név, jelszó).
- **Social credit**: A social credit egy olyan rendszer, amely a polgárok viselkedését és tevékenységeit értékeli, gyakran pontozás vagy rangsorolás alapján. Ezt a rendszert legjobban Kínában ismerik, ahol a kormány különböző adatokat gyűjt a polgárokról, például a pénzügyi viselkedésükről, a közlekedési szabálysértéseikről, és a közösségi médiában való aktivitásukról. A célja, hogy ösztönözze a "jó" viselkedést és csökkentse a "rossz" viselkedést, például a törvényszegéseket.
- **Anonymous user**: Azok a felhasználók, akik rátekintenek az oldalra, de nem jelentkeznek be. Limitált jogokkal rendelkeznek (pl.: hírolvasás). 