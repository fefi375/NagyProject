
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

Az OI hírportál célja, hogy megbízható és hiteles információt nyújtson a felhasználóknak, védve őket az álhírek és félreinformálások ellen.

A rendszer fejlesztésével az automatizált hírészlelés és -kezelés bevezetése a fő irányvonal, amely lehetővé teszi, hogy a moderátorok helyett egy intelligens rendszer végezze el a hírek szűrését.

Az új rendszer a felhasználói fiókok social credit rendszerén alapul, amely értékeli a felhasználók hozzájárulását a portál hitelességéhez.

# 2. Jelenlegi helyzet
Az OI hírportál egy olyan internetes hírlap, mely megvédi felhasználóit az álhírekről, veszélyes információktól és félreinformálásoktól. Pontosan ezért az ehhez hasonló híreket és információkat töröljük az oldalon. Eddig ezt moderátoraink tették, viszont már nincs elég nagy kapacitásunk, hogy minden egyes hírt átnézzünk.

Ez nagyban megnehezíti hogy megvédjük olvasóinkat az álhírektől és félreinformálásoktól.

Ennek érdekében, egy olyan automata rendszer mely automatikusan észleli az álhírek és különböző információk jelenlétét, majd javítja azokat. A túl sok ilyen híreket feltöltő fiókokat is észleli és korlátozza hírfeltöltésüket vagy akár fiókjukat is felfüggeszheti.

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

- 3.1 Fiók regisztrálása
- 3.2 Fiók adatainak mentése (név, jelszó)
- 3.3 Bármelyik fiók bármennyi hírt tehet közzé az oldalon
- 3.4 Moderátorok végzik a hírek ellenőrzését és igazságtartalmát
- 3.5 A túl sok hamis hírt terjesztő fiókot moderátoraink manuálisan bannolhatják

# 5. Igényelt üzleti folyamatok modellje

- 4.1. Igényelt folyamatok
   - 4.1.1. Jogosultság
      - 4.1.1.1. Fiók regisztráció
      - 4.1.1.2. Hírportálon való cikkírás
   - 4.1.2. Adatkezelés
      - 4.1.2.1. Fiók adatainak mentése
      - 4.1.2.2. Fiókhoz social credit rendelése
      - 4.1.2.3. Fiókon lévő hírírás blokkolása alacsony social credit szintnél
      - 4.1.2.4. Fiók törlése nagyon alacsony social credit szintnél

# 6. Használati esetek
Az országban az első számú, legmegbízhatóbb hírportállá nőheti ki magát az OI hírportál ha az automata észlelő rendszer implementálásra kerül. Sokkal több felhasználó, sokkal gyorsabban tehet közzé híreket és mi sokkal gyorsabban tudjuk ellenőrizni azok hitelességét. Ezért hírportálunk mind országszerte mind nemzetközi szinten hamar populárissá válhat.

# 7. Megfeleltetés
Az alkalmazás használatához a felhasználónak először egy fiókot kell regisztrálnia, amelyhez feltétel, hogy rendelkezzen egy érvényes email címmel.

A regisztráció befejezése után a felhasználó hozzáférhet a hírportál egyes funkcióihoz, kivéve azokhoz melyekhez admin jogosultság szükséges. A sikeres regisztrációt követően a felhasználó az általa megadott felhasználónév és jelszó kombinációjával léphet be a rendszerbe.

A belépési folyamat során a rendszer ellenőrzi a megadott adatokat, és ha azok helyesek, a felhasználó számára megnyílik portál főmenüje.
- Ebben a menüben a felhasználó több lehetőség közül választhat:
   - láthatja a mások által megosztott híreket
   - hírt tölthet fel az oldalra, amennyiben elegendő social credittel rendelkezik

A portál a felhasználóknak egyszerű kezelést és megfelelő biztonságot nyújt ellenőrzött és szabályozott információkkal.

A híreket közzétenni csak megbízható fiókoknak lehet, amelyet egy social credit pontszám határoz meg. A nem bízható (vagyis kevés pontszámmal rendlekező) fiókokat először elzárjuk a további hírek közzétételétől, majd töröljük.
   



# 8. Képernyőtervek

# 9. Forgatókönyv
A felhasználó regisztálhat a hírportálra, amelyet követően a helyesen megadott felhasználónév és jelszó kombinációjával az oldal belépést biztosít a felületre.

A regisztrációt követően a felhasználó automatikusan kap egy adott számú social credit pontszámot amely a fiók hitelességét jelzi.

A felhasználói felület úgy lett kialakítva, hogy könnyedén átlátható és kezelhető legyen, még azok számára is, akik nem rendelkeznek magas szintű technikai tudással. A hírek megjelennek a főoldalon, ahol könnyedén lehet új hírt hozzáadni.

A híreket az alkalmazás automatikusan ellenőrzi és a nem elfogadható hírek esetén attól a felhasználótól, aki a hírt közzétette adott számú social credit pontszámot vesz el.

A nem elegendő social creditel rendelkező fiókok nem tehetnek közzé híreket, majd fiókjuk törlésre is kerülhet.

A hírportál lehetővé teszi a felhasználók számára a könnyű tájékozódást, egyszerű felhasználói felületet és hatékony hírfeltöltést biztosít.A közzétett hírek azonnal láthatóvá válnak a felületen.



# 10. Funkció

Az alábbi funkciók kerülnek megvalósításra a hírportálon, amelyek biztonságosabbá, gyorsabbá és effektívebbé teszik a hírek böngészését felhasználóink számára:

- **Új fiók létrehozása**: Új fiókot hozhat létre a felhasználó, annak érdekében hogy saját ízléséhez megfelelő hírt ajánljon neki az oldal. Ezen felül hírt írni csak a regisztrált fiókkal rendelkező felhasználók tudnak.
- **social kredit hozzárendelése a fiókhoz**:Új fiók létrehozása esetén, a felhasználó egy adott összegű social creditet kap. Ez mutatja hogy a felhasználó megbízható forrás, ezért posztolhat a portálra.
- **Automatikus bejelentkezés**: A fiók sikeres létrehozása után az applikáció automatikusan bejelentkezteti a felhasználót, majd megjeleníti a főmenüt, ahonnan további funkciókat érhet el. Kijelentkezés esetén pedig felhasználónév és jelszó párossal visszaléphet a fiókjába.
- **Credit kezelése**: Ha a rendszer a felhasználó híreit hamisnak ítéli, a fiókjától social kredit pontokat vesz el, ezzel figyelmezteti/csökkenti a jogusultságait a felhasználónak.
- **Fiók korlátozása**: Ha a creditszám elég alacsony a rendszer automatikusan megszünteti a felhasználó posztolási lehetőségét.
- **Fiók törlése**: Ha a social credit elég alacsony, a fiók automatikusan törlődni fog a portálról.
- **Kijelentkezés**: A felhasználónak lehetősége van kijelentkezni a rendszerből, amely visszaviszi őt a kezdőmenübe. Innen új fiókot hozhat létre, vagy bejelentkezhet egy másik fiókba. A kijelentkezési funkció biztosítja, hogy a felhasználói adatok védelme érdekében a munkamenet biztonságosan lezáruljon.
- **Elfelejtett jelszó**: Elfejeltett jelszó esetén a felhasználó által megadott email fiókjára küldünk egy kódot (amennyiben ezzel az email címmel létezik regisztrált fiók), aminek beírása után a felhasználó megváltoztathatja jelszavát. Az új jelszava nem lehet az előző 3 alkalommal használt jelszó.