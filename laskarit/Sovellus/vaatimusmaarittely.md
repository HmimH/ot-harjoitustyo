# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on yksinkertainen peli, jossa valitaan vaihtoehtojen 1-3 välillä ja edetään tarinassa ja dialogissa. Osa vaihtoehdoista vaatii onnea, johon vaikuttavat sattuma ja pelaajan statsit.

## Käyttäjät

Eriäviä käyttäjärooleja ei ole suunnitteilla.

## Käyttöliittymäluonnos

Sovellus toteutetaan ensin ilman graafista käyttöliittymää. Myöhemmin sitä laajennetaan mahdollisuuksien puitteissa Visual Novel-tyyppiseksi.

Esim. Alkutavoitteista:


_A contemplative mathematician blocks the way_

╮(￣_￣)╭

_1.Approach_

_2.Attack[Strength: DC 10]_

####_3.Sneak by [Stealth: DC 7]_

Stats: Stealth: +2, Strength: 0, Math: +4, CS: +1, Speech: +3


##Perurusversion tarjoama toiminnallisuus

### Ensisijaiset tavoitteet

Pelaaja voi tehdä valintoja ja edistyä yksinkertaisessa tarinassa.

Pelaajan valinnat tallentuvat pelikierroksen aikana siten, että esim. valinnat eivät looppaa.

Pelaajan statit voi arpoa uudelleen ja tarkistaa pelin aikana. Ne vaikuttavat tiettyihin lopputuloksiin.

Tarinassa on menu, josta voi aloittaa pelin. Menuun voi palata aloittaakseen tarinan alusta.


### Toissijaiset tavoitteet

Pelaaja voi tallentaa pelin ja jatkaa sitä seuraavalla kerralla.

Pelaajan tiedot tallennetaan tietokantoihin _Stats_ and _Progress._

_Progress_.db kuvaa pelin etenemistä ja toimii tallennusmenetelmänä. Se tallentaa tiedot siitä mitä on tapahtunut ja mitä ei, ja mitä pelaajalla on ja mitä ei.

_Stats_.db kuvaa pelaajan taitoja.

Tarina on monipuolisempi ja kiinnostavampi.


## Myöhemmät tavoitteet

Graafisen käyttöliittymän tuottaminen.

Musiikin lisääminen.

Useampi samanaikainen save-file.

Laajempi tarina.

Tappelu- tai minigame-mekaniikka.

_Achievements_ informaatio, joka säilyy läpi kaikkien save-filejen.
