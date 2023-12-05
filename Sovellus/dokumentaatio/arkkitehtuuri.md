classDiagram
  class Dialogue {
    __init__(message, first, second, third, firsteffect, 
    secondeffect, thirdeffect>

  }

  class Screenstate {
    __init__(background, icons, choices: Dialogue)
  }

  Dialogue --> Screenstate
  Screenstate --> Dialogue


