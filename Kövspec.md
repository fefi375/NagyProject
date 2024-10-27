# Fejezetek

- [Jelenlegi Helyzet](#1-jelenlegi-helyzet)
- [Vágyálom rendszer](#2-vágyálom-rendszer)
- [Jelenlegi üzleti folyamatok](#3-jelenlegi-üzleti-folyamatok)
- [Igényelt üzleti folyamatok](#4-igényelt-üzleti-folyamatok)
- [rendszer szabályok](#5-rendszerre-vonatkozó-szabályok)
- [Követelménylista](#6-követelménylista)

# 1. jelenlegi helyzet
Az OI hírportál egy olyan internetes hírlap, mely megvédi felhasználóit az álhírekről, veszélyes információktól és félreinformálásoktól. Pontosan ezért az ehhez hasonló híreket és információkat töröljük az oldalon. Eddig ezt moderátoraink tették, viszont már nincs elég nagy kapacitásunk, hogy minden egyes hírt átnézzünk.

Ez nagyban megnehezíti hogy megvédjük olvasóinkat az álhírektől és félreinformálásoktól.

Ennek érdekében, egy olyan automata rendszer mely automatikusan észleli az álhírek és különböző információk jelenlétét, majd javítja azokat. A túl sok ilyen híreket feltöltő fiókokat is észleli és korlátozza hírfeltöltésüket vagy akár fiókjukat is felfüggeszheti.

Ez nagyban megnehezíti hogy megvédjük olvasóinkat az álhírektől és félreinformálásoktól.

Ennek érdekében egy olyan automata rendszer mely automatikusan észleli az álhírek és különböző információk jelenlétét, majd javítja azokat. A túl sok ilyen híreket feltöltő fiókokat is észleli és korlátozza hírfeltöltésüket vagy akár fiókjukat is függeszti.


# 2. Vágyálom rendszer
Az olvasóink megvédése érdekében egy olyan automatikus figyelőrendszert szeretnénk kifejleszteni amely észreveszi azon híreket amelyeket el kell rejtenünk a nagyközönség elől.

Szeretnénk bevezetni egy social credit változót amely méri az emberek pozitív vagy negatív hozzájárulását a portálhoz.

Megakadályozza hogy a kevés social credittel rendelkezők álhíreket terjesszenek és nagyon kevés pont esetén törli is a fiókjukat.

# 3. Jelenlegi üzleti folyamatok

- 3.1 Fiók regisztrálása
- 3.2 Fiók adatainak mentése (név, jelszó)
- 3.3 Bármelyik fiók bármennyi hírt tehet közzé az oldalon
- 3.4 Moderátorok végzik a hírek ellenőrzését és igazságtartalmát
- 3.5 A túl sok hamis hírt terjesztő fiókot moderátoraink manuálisan bannolhatják

# 4. Igényelt üzleti folyamatok

- 4.1. Igényelt folyamatok
   - 4.1.1. Jogosultság
      - 4.1.1.1. Fiók regisztráció
      - 4.1.1.2. Hírportálon való cikkírás
   - 4.1.2. Adatkezelés
      - 4.1.2.1. Fiók adatainak mentése
      - 4.1.2.2. Fiókhoz social credit rendelése
      - 4.1.2.3. Fiókon lévő hírírás blokkolása alacsony social credit szintnél
      - 4.1.2.4. Fiók törlése nagyon alacsony social credit szintnél

# 5. Rendszerre vonatkozó szabályok

# 6. Követelménylista
   |   Modul   |   ID  |   Név |   version |   Kifejtés    |
   |:----------|:------|:------|:----------|:--------------|
   |    Jogosultság |   1   |   Regisztráció    |   1.0 | Felhasználói fiók létrehozása  |
   |    Adatkezelés |   2   |   Adat mentése    |   1.0 |   Regisztrált adatok mentése adatbázisban |
   |   Jogosultság |   3  |    Bejelentkezés   |   1.0 |   A felhasználó a felhasználói nevével illetve jelszó párossal bejelentkezhet. Ha a felhasználónév illetve a jelszó páros nem megfelelő, hibaüzenetet kap. |
   |   Jogosultság |   4   |   Hírírás   |   1.0 |   A felhasználó hírt írhat az oldalon, ami alapján social credit számát növeli/csökkenti. |
   |   Adatkezelés |   5   | Social credit |   1.0 |   A felhasználó social creditet kap vagy veszít a hírének validációja alapján.   |
|   Adatkezelés    |   6   |   Hírírás jogának elvétele   |   1.0 |   A felhasználói fiók elveszíti hírírási jogát alacsony social credit szintnél.    |
   |   Adatkezelés    |   7   |   Account törlése   |   1.0 |   A felhasználói fiók törlésre kerül nagyon alacsony social credit szintnél.    |

# 7. Fogalomtár

- **Adatbázis**: Az adatbázis egy strukturált adattároló, amely lehetővé teszi adatok rendszerezett, biztonságos és hatékony tárolását, lekérdezését és kezelését (Név, jelszó).
- **Social credit**: A social credit egy olyan rendszer, amely a polgárok viselkedését és tevékenységeit értékeli, gyakran pontozás vagy rangsorolás alapján. Ezt a rendszert legjobban Kínában ismerik, ahol a kormány különböző adatokat gyűjt a polgárokról, például a pénzügyi viselkedésükről, a közlekedési szabálysértéseikről, és a közösségi médiában való aktivitásukról. A célja, hogy ösztönözze a "jó" viselkedést és csökkentse a "rossz" viselkedést, például a törvényszegéseket.