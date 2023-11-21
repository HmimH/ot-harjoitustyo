classDiagram
    Monopolipeli "1" -- "2" Noppa
        class Noppa{
        +heitaliike()
    }
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
        class Pelinappula{
            +liike()
    }
    Kortti "1" -- "1" Sattuma_tai_yhteismaa
    Pelilauta "1" -- "40" Kortti
    Pelaaja "2..8" -- "1" Monopolipeli
        class Pelaaja{
        +Int rahat
        +List omistetut
    }
        class Ruutu{
        +List[(ruutunro, tyyppi)]
    }


    Ruutu <|-- Vankila
        class Vankila{
            +liike_minus_nopat()
    }
    Ruutu <|-- Aloitusruutu
        class Aloitusruutu{
            +rahat+=200()
    }
    Ruutu <|-- Sattuma_tai_yhteismaa
        class Sattuma_tai_yhteismaa{
            +ota_kortti()
    }
    Ruutu <|-- Nimetty_katu
        class Nimetty_katu{
            +Pelaaja omistaja
            +int vapaat_tontit
            +osta()
            +rakenna()
    }
    Kortti "1" -- "1" Tapahtuma
        class Tapahtuma{
        +String tapahtuma
    }







