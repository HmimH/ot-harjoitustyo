(https://drive.google.com/file/d/1Ioud0ZR7cmQsZMJ3b5prb2OBm2GDPCcB/view?usp=sharing)

classDiagram
  class Dialogue {
    - message: string
    - first: string
    - second: string
    - third: string
    - e_1: function
    - e_2: function
    - e_3: function
    __init__(message, first, second, third, firsteffect, secondeffect, thirdeffect)
    __str__() string
  }

  class Screenstate {
    - background: string
    - icons: list
    - choices: Dialogue
    __init__(background, icons, choices: Dialogue)
    __str__() string
    ask()
    menu()
  }

  Dialogue --> Screenstate
  Screenstate --> Dialogue
