#merkittävä osa tehtävän koodista on chat.gpt:n generoimaa


sequenceDiagram

  participant Main as Main

  participant Laitehallinto as Laitehallinto

  participant Rautatietori as Rautatietori

  participant Ratikka6 as Ratikka6

  participant Bussi244 as Bussi244

  participant LippuLuukku as LippuLuukku

  participant KallenKortti as KallenKortti


  Main->>Laitehallinto: Luo laitehallinto

  Laitehallinto->>Rautatietori: Lisää lataaja (Rautatietori)

  Laitehallinto->>Ratikka6: Lisää lukija (Ratikka6)

  Laitehallinto->>Bussi244: Lisää lukija (Bussi244)

  Main->>LippuLuukku: Luo LippuLuukku

  LippuLuukku->>KallenKortti: Osta matkakortti (Kalle)



  Rautatietori->>KallenKortti: Lataa arvoa (3)


  Ratikka6->>KallenKortti: Osta lippu (RATIKKA)

  Bussi244->>KallenKortti: Osta lippu (SEUTU)





