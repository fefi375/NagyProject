
# Fejezetek
- [Áttekintés](#1-áttekintés)
- [Jelenlegi helyzet](#2-jelenlegi-helyzet)
- [Követelménylista](#3-követelménylista)
- [Jelenlegi üzleti folyamatok](#4-jelenlegi-üzleti-folyamatok-modellje)
- [Igényelt üzleti folyamatok](#5-igényelt-üzleti-folyamatok-modellje)
- [Használati esetek](#6-használati-esetek)
- [Megfeleltetés](#7-megfeleltetés)
- [Képernyőtervek](#8-képernyőtervek)
- [Forgatókönyv](#9-forgatókönyv)
- [Funkció](#10-funkció)



# 1. Áttekintés

# 2. Jelenlegi helyzet
Az OI hírportál egy olyan internetes hírlap, mely megvédi felhasználóit az álhírekről, veszélyes információktól és félreinformálásoktól. Pontosan ezért az ehhez hasonló híreket és információkat töröljük az oldalon. Eddig ezt moderátoraink tették, viszont már nincs elég nagy kapacitásunk, hogy minden egyes hírt átnézzünk.

Ez nagyban megnehezíti hogy megvédjük olvasóinkat az álhírektől és félreinformálásoktól.

Ennek érdekében, egy olyan automata rendszer mely automatikusan észleli az álhírek és különböző információk jelenlétét, majd javítja azokat. A túl sok ilyen híreket feltöltő fiókokat is észleli és korlátozza hírfeltöltésüket vagy akár fiókjukat is felfüggeszheti.


Ennek érdekében egy olyan automata rendszer mely automatikusan észleli az álhírek és különböző információk jelenlétét, majd javítja azokat. A túl sok ilyen híreket feltöltő fiókokat is észleli és korlátozza hírfeltöltésüket vagy akár fiókjukat is függeszti.
# 3. Követelménylista
   |   Modul   |   ID  |   Név |   version |   Kifejtés    |
   |:----------|:------|:------|:----------|:--------------|
   |    Jogosultság |   1   |   Regisztráció    |   1.0 | Felhasználói fiók létrehozása  |
   |    Adatkezelés |   2   |   Adat mentése    |   1.0 |   Regisztrált adatok mentése adatbázisban |
   |   Jogosultság |   3  |    Bejelentkezés   |   1.0 |   A felhasználó a felhasználói nevével illetve jelszó párossal bejelentkezhet. Ha a felhasználónév illetve a jelszó páros nem megfelelő, hibaüzenetet kap. |
   |   Jogosultság |   4   |   Hírírás   |   1.0 |   A felhasználó hírt írhat az oldalon, ami alapján social credit számát növeli/csökkenti. |
   |   Adatkezelés |   5   | Social credit |   1.0 |   A felhasználó social creditet kap vagy veszít a hírének validációja alapján.   |
|   Adatkezelés    |   6   |   Hírírás jogának elvétele   |   1.0 |   A felhasználói fiók elveszíti hírírási jogát alacsony social credit szintnél.    |
   |   Adatkezelés    |   7   |   Account törlése   |   1.0 |   A felhasználói fiók törlésre kerül nagyon alacsony social credit szintnél.    |
# 4. Jelenlegi üzleti folyamatok modellje

# 5. Igényelt üzleti folyamatok modellje

4.1. Igényelt funkciók
4.1.1. Fiók regisztráció
4.1.2. Fiók adatainak mentése (név,jelszó)
4.1.3. Hírportálon való cikkírás
4.1.4. Fiókhoz rendelt social credit
4.1.5. Fiókon lévő hírírás blokkolása alacsony social credit szintnél
4.1.6. Fiók törlése nagyon alacsony social credit szintnél

# 6. Használati esetek
Az országban az első számú, legmegbízhatóbb hírportállá nőheti ki magát az OI hírportál ha az automata észlelő rendszer implementálásra kerül. Sokkal több felhasználó, sokkal gyorsabban tehet közzé híreket és mi sokkal gyorsabban tudjuk ellenőrizni azok hitelességét. Ezért hírportálunk mind országszerte mind nemzetközi szinten hamar populárissá válhat.

# 7. Megfeleltetés

# 8. Képernyőtervek

# 9. Forgatókönyv

# 10. Funkció
