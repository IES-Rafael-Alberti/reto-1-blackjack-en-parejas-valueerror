import random
import os


def borrar_Consola():
    """Clears the console.

    In the os module if the Operating system is Windows 'os.name' will be 'nt', if the operating system is mac or linux-based it will be 'posix' 
    """
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")


def pedir_Opcion(limite: int):
    """Takes a user string input and checks if it is an integer within the specified range.
    
    While the user input does not match an integer within the specified range it will keep asking the user for an input.
    
    Args:
        limite:
            An integer representing the maximum number acceptable.
    
    Returns:
        The user input as a string once all conditions have been met.
    """
    loop = True
    while loop == True:
        opcion = input(f"Introuduzca un número entre 1 y {limite}: ")
        try:
            if int(opcion) < 1 or int(opcion) > limite:
                print(
                    f"Error, ese valor no corresponde a ninguna opción. Por favor introduzca un número entero entre 1 y {limite}: "
                )
            else:
                loop = False
                return opcion
        except ValueError:
            print(
                f"Error, el valor introducido no es un número entero. Por favor introduzca un número entero entre 1 y {limite}: "
            )


def barajar_Baraja(
    barajaNumeros: str,
    barajaPalos: str,
):
    """Shuffles a deck of cards and saves it into a string.
    
    Takes a string made up of all the possible numbers in a deck of cards repeated 4 times and a string made up of all the possible colors in a deck of cards repeated 13 times and shuffles them into a new string which represents a shuffled deck.

    Args:
        barajaNumeros:
            A string made up of all the possible numbers in a deck of cards.
        barajaPalos:
            A string made up of all the possible colors in a deck of cards repeated for each card of the deck.
    
    Returns:
        A string made up of all the numbers in the deck shuffled followed by all the colors in the deck shuffled.
    """
    barajaNumerosBarajada = ""
    barajaPalosBarajada = ""
    for i in range(1, 53):
        cartaPosicion = int(random.randint(0, ((len(barajaNumeros)) - 1)))
        barajaNumerosBarajada += barajaNumeros[cartaPosicion]
        barajaPalosBarajada += barajaPalos[cartaPosicion]
        barajaNumeros = (
            barajaNumeros[:cartaPosicion] + barajaNumeros[cartaPosicion + 1 :]
        )
        barajaPalos = barajaPalos[:cartaPosicion] + barajaPalos[cartaPosicion + 1 :]
    barajaStr = barajaNumerosBarajada + "&" + barajaPalosBarajada
    return barajaStr


def dar_Carta(
    barajaNumerosBarajada: str,
    barajaPalosBarajada: str,
    contadorNumeroCarta: int,
    cartasJugadorNumero: str,
    cartasJugadorPalo: str,
    valorManoJugador: int,
    asCambiadoJugador: bool,
    asManoJugador: bool,
):
    """Gives a player a card.

    Takes 2 strings representing the playing deck shuffled as well as the value of the players hand and a counter for which card is the next in play, with that it adds the new card to the players hand and calculates the new value of the players hand depending on which card the player has been dealt. It also takes 2 bool values which represent whether the player has an ace in his hand or not and whether that ace's value is 11 or 1.

    Args:
        barajaNumerosBarajada:
            A string made up of all the possible numbers in a deck of cards shuffled.  
        barajaPalosBarajada:
            A string made up of all the possible colors in a deck of cards repeated for each card of the deck shuffled. 
        contadorNumeroCarta:
            An integer that represents how many cards have been dealt. 
        cartasJugadorNumero: 
            A string made up of the card numbers in the player's hand.
        cartasJugadorPalo:
            A string made up of the card colors in the player's hand. 
        valorManoJugador:
            An integer that represents the current value of the player's hand. 
        asCambiadoJugador:
            A boolean that represents whether the player has changed the value of the ace in his hand from 11 to 1. 
        asManoJugador: 
            A boolean that represents whether the player has an ace in his hand or not. 
    Returns:
       A string made up of the new contadorNumeroCarta, the new cartasJugadorNumero, the new cartasJugadorPalo, the new ValorManoJugador, the new or unchanged asCambiadoJugador and asManoJugador with a '&' in between each. 
    """
    cartasJugadorNumero += barajaNumerosBarajada[contadorNumeroCarta]
    cartasJugadorPalo += barajaPalosBarajada[contadorNumeroCarta]
    if (
        barajaNumerosBarajada[contadorNumeroCarta] == "0"
        or barajaNumerosBarajada[contadorNumeroCarta] == "J"
        or barajaNumerosBarajada[contadorNumeroCarta] == "Q"
        or barajaNumerosBarajada[contadorNumeroCarta] == "K"
    ):
        if (
            valorManoJugador + 10 > 21
            and asCambiadoJugador == False
            and asManoJugador == True
        ):
            asCambiadoJugador = True
            valorManoJugador += 10 - 10
        else:
            valorManoJugador += 10
    elif barajaNumerosBarajada[contadorNumeroCarta] == "A":
        asManoJugador = True
        if (
            valorManoJugador + 11 > 21
            and asCambiadoJugador == False
            and asManoJugador == True
        ):
            asCambiadoJugador = True
            valorManoJugador += 11 - 10
        else:
            valorManoJugador += 11
    else:
        if (
            valorManoJugador + int(barajaNumerosBarajada[contadorNumeroCarta]) > 21
            and asCambiadoJugador == False
            and asManoJugador == True
        ):
            asCambiadoJugador = True
            valorManoJugador += int(barajaNumerosBarajada[contadorNumeroCarta]) - 10
        else:
            valorManoJugador += int(barajaNumerosBarajada[contadorNumeroCarta])
    contadorNumeroCarta += 1
    darCartaStr = (
        str(contadorNumeroCarta)
        + "&"
        + cartasJugadorNumero
        + "&"
        + cartasJugadorPalo
        + "&"
        + str(valorManoJugador)
        + "&"
        + str(asCambiadoJugador)
        + "&"
        + str(asManoJugador)
    )
    return darCartaStr


def imprimir_Mano(
    cartasJugadorNumero: str,
    cartasJugadorPalo: str,
    asCambiadoJugador: bool,
    asManoJugador: bool,
    valorManoJugador: int,
):
    """Makes a string with the value of the players hand and all the name of their cards.

    Takes 2 strings representing the player's current hand as well as the value of the players hand and 2 bool values which represent whether the player has an ace in his hand or not and whether that ace's value is 11 or 1, then it creates a new string whith the names of each card in the hand and the value of said hand.

    Args:
        cartasJugadorNumero: 
            A string made up of the card numbers in the player's hand.
        cartasJugadorPalo:
            A string made up of the card colors in the player's hand.  
        asCambiadoJugador:
            A boolean that represents whether the player has changed the value of the ace in his hand from 11 to 1. 
        asManoJugador: 
            A boolean that represents whether the player has an ace in his hand or not. 
        valorManoJugador:
            An integer that represents the current value of the player's hand.

    Returns:
       A string made up of all the player's cards and the value of those cards.
    """
    manoStr = ""
    for i in range(0, len(cartasJugadorNumero)):
        if cartasJugadorNumero[i] == "A":
            if cartasJugadorPalo[i] == "C":
                manoStr += ("Un As de Corazones") + "\n"
            elif cartasJugadorPalo[i] == "T":
                manoStr += ("Un As de Tréboles") + "\n"
            elif cartasJugadorPalo[i] == "P":
                manoStr += ("Un As de Picas") + "\n"
            else:
                manoStr += ("Un As de Diamantes") + "\n"
        elif cartasJugadorNumero[i] == "K":
            if cartasJugadorPalo[i] == "C":
                manoStr += ("Un Rey de Corazones") + "\n"
            elif cartasJugadorPalo[i] == "T":
                manoStr += ("Un Rey de Tréboles") + "\n"
            elif cartasJugadorPalo[i] == "P":
                manoStr += ("Un Rey de Picas") + "\n"
            else:
                manoStr += ("Un Rey de Diamantes") + "\n"
        elif cartasJugadorNumero[i] == "Q":
            if cartasJugadorPalo[i] == "C":
                manoStr += ("Una Reina de Corazones") + "\n"
            elif cartasJugadorPalo[i] == "T":
                manoStr += ("Una Reina de Tréboles") + "\n"
            elif cartasJugadorPalo[i] == "P":
                manoStr += ("Una Reina de Picas") + "\n"
            else:
                manoStr += ("Una Reina de Diamantes") + "\n"
        elif cartasJugadorNumero[i] == "J":
            if cartasJugadorPalo[i] == "C":
                manoStr += ("Una Jota de Corazones") + "\n"
            elif cartasJugadorPalo[i] == "T":
                manoStr += ("Una Jota de Tréboles") + "\n"
            elif cartasJugadorPalo[i] == "P":
                manoStr += ("Una Jota de Picas") + "\n"
            else:
                manoStr += ("Una Jota de Diamantes") + "\n"
        elif cartasJugadorNumero[i] == "0":
            if cartasJugadorPalo[i] == "C":
                manoStr += ("Un 10 de Corazones") + "\n"
            elif cartasJugadorPalo[i] == "T":
                manoStr += ("Un 10 de Tréboles") + "\n"
            elif cartasJugadorPalo[i] == "P":
                manoStr += ("Un 10 de Picas") + "\n"
            else:
                manoStr += ("Un 10 de Diamantes") + "\n"
        else:
            if cartasJugadorPalo[i] == "C":
                manoStr += (f"Un {cartasJugadorNumero[i]} de Corazones") + "\n"
            elif cartasJugadorPalo[i] == "T":
                manoStr += (f"Un {cartasJugadorNumero[i]} de Tréboles") + "\n"
            elif cartasJugadorPalo[i] == "P":
                manoStr += (f"Un {cartasJugadorNumero[i]} de Picas") + "\n"
            else:
                manoStr += (f"Un {cartasJugadorNumero[i]} de Diamantes") + "\n"
    manoStr += "\n"
    if asCambiadoJugador == False and asManoJugador == True:
        if valorManoJugador + 10 > 21:
            manoStr += f"Valor mano: {valorManoJugador}\n"
        else:
            manoStr += f"Valor mano: {valorManoJugador} o {valorManoJugador - 10} dependiendo del valor del As\n"
    else:
        manoStr += f"Valor mano: {valorManoJugador}\n"
    manoStr += "__________________________"
    return manoStr


def comprobar_Ganador(
    valorManoJugador1: int,
    valorManoJugador2: int,
    ronda: int,
    nombreJ1: str,
    nombreJ2: str,
):
    """Checks for the winnig player and creates a string with the winning text.

    Takes the value of both player's hands and their names, checks who the winner is and which round it is and creates a string with the winner's name, the round it is and a winning text.

    Args:
        valorManoJugador1:
            An integer that represents the value of player1's hand.
        valorManoJugador2:
            An integer that represents the value of player2's hand.
        ronda:
            An integer that represents the round number.
        nombreJ1:
            A string that represents player1's name.
        nombreJ2:
            A string that represents player2's name.
    
    Returns:
        A string with the winner's name, the round it is and a winning text
    """
    if valorManoJugador1 > 21 or valorManoJugador2 > 21:
        if valorManoJugador1 > 21 and valorManoJugador2 > 21:
            ganadorStr1 = f"JUEGO TERMINADO - Ronda {ronda}"
            ganadorStr2 = f"Game over ¡Los dos os habéis pasado!"
            ganadorStr = ganadorStr1 + "&" + ganadorStr2
            return str(ganadorStr)
        elif valorManoJugador1 == valorManoJugador2:
            ganadorStr1 = "JUEGO TERMINADO - Ronda {ronda}"
            ganadorStr2 = f"¡Empate!"
            ganadorStr = ganadorStr1 + "&" + ganadorStr2
            return str(ganadorStr)
        elif valorManoJugador2 < valorManoJugador1:
            ganadorStr1 = f"JUEGO TERMINADO - Ronda {ronda}"
            ganadorStr2 = f"¡Gana J2 - {nombreJ2}!"
            ganadorStr = ganadorStr1 + "&" + ganadorStr2
            return str(ganadorStr)
        else:
            ganadorStr1 = f"JUEGO TERMINADO - Ronda {ronda}"
            ganadorStr2 = f"¡Gana J1 - {nombreJ1}!"
            ganadorStr = ganadorStr1 + "&" + ganadorStr2
            return str(ganadorStr)
    else:
        if valorManoJugador1 == valorManoJugador2:
            ganadorStr1 = f"JUEGO TERMINADO - Ronda {ronda}"
            ganadorStr2 = f"¡Empate!"
            ganadorStr = ganadorStr1 + "&" + ganadorStr2
            return str(ganadorStr)
        elif valorManoJugador2 > valorManoJugador1:
            ganadorStr1 = f"JUEGO TERMINADO - Ronda {ronda}"
            ganadorStr2 = f"¡Gana J2 - {nombreJ2}!"
            ganadorStr = ganadorStr1 + "&" + ganadorStr2
            return str(ganadorStr)
        else:
            ganadorStr1 = f"JUEGO TERMINADO - Ronda {ronda}"
            ganadorStr2 = f"¡Gana J1 - {nombreJ1}!"
            ganadorStr = ganadorStr1 + "&" + ganadorStr2
            return str(ganadorStr)


def main():

    # Crea 2 cadenas de caracteres, una con todos los posibles numeros de la baraja y otra con la inicial de cada palo de la baraja repetida tantas veces como cartas de dicho palo hay. De esta forma podemos generar una carta juntando las posiciones equivalentes de cada cadena de caracteres. Ejemplo: barajaNumeros[2] + barajaPalos[2] == 2C. 2C equivale al 2 de corazones.

     # Numeros de la baraja ordenada
    barajaNumeros = "A234567890JQKA234567890JQKA234567890JQKA234567890JQK"
    # Palos de la baraja ordenada
    barajaPalos = "CCCCCCCCCCCCCTTTTTTTTTTTTTPPPPPPPPPPPPPDDDDDDDDDDDDD"
    # Numero contador de la siguiente carta que tenemos que repartir, nos servira tambien para saber cuando hemos repartido mas del 50% de la baraja y tenemos que volver a barajar
    contadorNumeroCarta = 0 

    # Genera dos nuevas cadenas de caracteres iguales a la anterior pero con los caracteres ordenados de forma aleatoria con respecto a la anterior. La posicion de cada caracter en la cadena numeros equivale a la posicion de su palo de la baraja, de tal forma que no puede generarse la misma carta 2 veces.

    barajaStr = barajar_Baraja(barajaNumeros, barajaPalos)

    barajaNumerosBarajada = barajaStr[0 : barajaStr.find("&")]
    barajaPalosBarajada = barajaStr[barajaStr.find("&") + 1 : len(barajaStr)]

    borrar_Consola()
    print(
        f"""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                      █
█ Bienvenido al casino del grupo ValueError.                           █
█                                                                      █
█ Actualmente solo ofrecemos blackjack contra un compañero o contra    █
█ nuestra extremadamente avanzada inteligencia artificial.             █
█                                                                      █
█                                                                      █
█                                                                      █
█ Esperemos que disfrute la experiencia.                               █
█                                                                      █
█                                                                      █
█                                                                      █
█ Seleccione una opción.                                               █
█                                                                      █          
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀█
█ 1. Jugar contra otro jugador █ 2. Jugar contra la máquina █ 3. Salir █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄█              
"""
    )
    opcionModo = pedir_Opcion(3)

    # Creamos un bucle while que mantendra el programa en funcionamiento mientras el usuario no inserte la opcion de cerrado del programa.

    partidasJugadas = 0
    # Variable booleana que usaremos para saber cuando debemos cerrar el programa, el bucle se mantendra activo mientras su valor sea False.
    final = False  
    while final == False:
        if partidasJugadas != 0:
            print(
                f"""              
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                      █
█ {ganadorStr1:69}█
█ {ganadorStr2:69}█
█                                                                      █
█                                                                      █
█                                                                      █
█                                                                      █
█                                                                      █
█                                                                      █
█                                                                      █
█                                                                      █
█                                                                      █
█ Seleccione una opción.            Partidas jugadas:              {partidasJugadas:3.0f} █
█                                                                      █          
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀▀▀▀▀▀▀▀▀▀█
█ 1. Jugar contra otro jugador █ 2. Jugar contra la máquina █ 3. Salir █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄█ 
"""
            )
            opcionModo = pedir_Opcion(3)
        if opcionModo == "3":
            borrar_Consola()
            print(
                """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                      █
█ Cerrando el programa Blackjack....                                   █
█                                                                      █
█ Vuelve pronto!                                                       █
█                                                                      █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
                  """
            )
            final = True

        elif opcionModo == "1":
            borrar_Consola()
            print(
                f"""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                      █
█ Opción seleccionada:                                                 █
█                                                                      █
█ Jugar contra otro jugador.                                           █
█                                                                      █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""
            )

            # Crea 2 cadenas de caracteres, una con el numero de cada carta y otra con el palo de dicha carta

            if contadorNumeroCarta > 25:
                barajaNumeros = "A234567890JQKA234567890JQKA234567890JQKA234567890JQK"
                barajaPalos = "CCCCCCCCCCCCCTTTTTTTTTTTTTPPPPPPPPPPPPPDDDDDDDDDDDDD"
                contadorNumeroCarta = 0

                barajaStr = barajar_Baraja(barajaNumeros, barajaPalos)

                barajaNumerosBarajada = barajaStr[0 : barajaStr.find("&")]
                barajaPalosBarajada = barajaStr[
                    barajaStr.find("&") + 1 : len(barajaStr)
                ]

            cartasJugador1Numero = ""
            cartasJugador2Numero = ""
            cartasJugador1Palo = ""
            cartasJugador2Palo = ""
            valorManoJugador1 = 0
            valorManoJugador2 = 0
            asCambiadoJugador1 = False
            asCambiadoJugador2 = False
            asManoJugador1 = False
            asManoJugador2 = False

            # Pedir apodos de jugadores

            nombreJ1 = input("Introduzca el apodo del jugador 1: ")
            nombreJ2 = input("Introduzca el apodo del jugador 2: ")

            # Da 2 cartas al jugador1

            darCartaStr = dar_Carta(
                barajaNumerosBarajada,
                barajaPalosBarajada,
                contadorNumeroCarta,
                cartasJugador1Numero,
                cartasJugador1Palo,
                valorManoJugador1,
                asCambiadoJugador1,
                asManoJugador1,
            )
            contadorNumeroCarta = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador1Numero = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador1Palo = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            valorManoJugador1 = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asCambiadoJugador1 = bool(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asManoJugador1 = bool(darCartaStr)

            darCartaStr = dar_Carta(
                barajaNumerosBarajada,
                barajaPalosBarajada,
                contadorNumeroCarta,
                cartasJugador1Numero,
                cartasJugador1Palo,
                valorManoJugador1,
                asCambiadoJugador1,
                asManoJugador1,
            )
            contadorNumeroCarta = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador1Numero = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador1Palo = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            valorManoJugador1 = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asCambiadoJugador1 = bool(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asManoJugador1 = bool(darCartaStr)

            # Da 2 cartas al jugador2

            darCartaStr = dar_Carta(
                barajaNumerosBarajada,
                barajaPalosBarajada,
                contadorNumeroCarta,
                cartasJugador2Numero,
                cartasJugador2Palo,
                valorManoJugador2,
                asCambiadoJugador2,
                asManoJugador2,
            )
            contadorNumeroCarta = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador2Numero = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador2Palo = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            valorManoJugador2 = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asCambiadoJugador2 = bool(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asManoJugador2 = bool(darCartaStr)

            darCartaStr = dar_Carta(
                barajaNumerosBarajada,
                barajaPalosBarajada,
                contadorNumeroCarta,
                cartasJugador2Numero,
                cartasJugador2Palo,
                valorManoJugador2,
                asCambiadoJugador2,
                asManoJugador2,
            )
            contadorNumeroCarta = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador2Numero = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador2Palo = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            valorManoJugador2 = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asCambiadoJugador2 = bool(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asManoJugador2 = bool(darCartaStr)

            borrar_Consola()

            # Se imprime por pantalla las cartas que tiene el jugador1 y el jugador2 asi como el valor total de cada mano

            print(f"La mano del J1 - {nombreJ1} esta compuesta de: ")
            mostrarMano = imprimir_Mano(
                cartasJugador1Numero,
                cartasJugador1Palo,
                asCambiadoJugador1,
                asManoJugador1,
                valorManoJugador1,
            )
            print(mostrarMano)

            print(f"La mano del J2 - {nombreJ2} esta compuesta de: ")
            mostrarMano = imprimir_Mano(
                cartasJugador2Numero,
                cartasJugador2Palo,
                asCambiadoJugador2,
                asManoJugador2,
                valorManoJugador2,
            )
            print(mostrarMano)

            ronda = 1

            # Comprueba si algun jugador suman 21 con las 2 cartas iniciales

            if (valorManoJugador1 == 21) and (valorManoJugador2 == 21):
                ganadorStr1 = "JUEGO TERMINADO - Ronda 1"
                ganadorStr2 = "¡Empate!"

            elif valorManoJugador1 == 21:
                ganadorStr1 = f"JUEGO TERMINADO - Ronda 1"
                ganadorStr2 = f"¡Gana J1 - {nombreJ1}!"

            elif valorManoJugador2 == 21:
                ganadorStr1 = f"JUEGO TERMINADO - Ronda 1"
                ganadorStr2 = f"¡Gana J2 - {nombreJ2}!"

            # Pregunta al los jugadores si quieren plantarse con el valor que tienen o seguir pidiendo cartas

            else:
                jugador1Plantarse = False
                jugador2Plantarse = False
                while jugador1Plantarse == False or jugador2Plantarse == False:
                    if jugador1Plantarse == False:
                        print(
                            f"""J1 - {nombreJ1} seleccione una opción:
1) Pedir carta.
2) Plantarse."""
                        )
                        opcion = pedir_Opcion(2)
                        print("")
                        if opcion == "1":
                            print(f"J1 - {nombreJ1} pide otra carta.")
                            print("")
                            darCartaStr = dar_Carta(
                                barajaNumerosBarajada,
                                barajaPalosBarajada,
                                contadorNumeroCarta,
                                cartasJugador1Numero,
                                cartasJugador1Palo,
                                valorManoJugador1,
                                asCambiadoJugador1,
                                asManoJugador1,
                            )
                            contadorNumeroCarta = int(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            cartasJugador1Numero = darCartaStr[
                                0 : darCartaStr.find("&")
                            ]
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            cartasJugador1Palo = darCartaStr[0 : darCartaStr.find("&")]
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            valorManoJugador1 = int(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            asCambiadoJugador1 = bool(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            asManoJugador1 = bool(darCartaStr)
                            if valorManoJugador1 > 21:
                                print(f"J1 - {nombreJ1} se ha pasado.")
                                print("")
                                jugador1Plantarse = True
                        else:
                            print(f"J1 - {nombreJ1} se planta.")
                            print("")
                            jugador1Plantarse = True
                    if jugador2Plantarse == False:
                        print(
                            f"""J2 - {nombreJ2} seleccione una opción:
1) Pedir carta.
2) Plantarse."""
                        )
                        opcion = pedir_Opcion(2)
                        print("")
                        if opcion == "1":
                            print(f"J2 - {nombreJ2} pide otra carta.")
                            print("")
                            darCartaStr = dar_Carta(
                                barajaNumerosBarajada,
                                barajaPalosBarajada,
                                contadorNumeroCarta,
                                cartasJugador2Numero,
                                cartasJugador2Palo,
                                valorManoJugador2,
                                asCambiadoJugador2,
                                asManoJugador2,
                            )
                            contadorNumeroCarta = int(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            cartasJugador2Numero = darCartaStr[
                                0 : darCartaStr.find("&")
                            ]
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            cartasJugador2Palo = darCartaStr[0 : darCartaStr.find("&")]
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            valorManoJugador2 = int(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            asCambiadoJugador2 = bool(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            asManoJugador2 = bool(darCartaStr)
                            if valorManoJugador2 > 21:
                                print(f"J2 - {nombreJ2} se ha pasado.")
                                print("")
                                jugador2Plantarse = True
                        else:
                            print(f"J2 - {nombreJ2} se planta.")
                            print("")
                            jugador2Plantarse = True
                    # Se imprime por pantalla las cartas que tiene el jugador asi como el valor total de la mano

                    borrar_Consola()

                    print(f"La mano del J1 - {nombreJ1} esta compuesta de: ")
                    mostrarMano = imprimir_Mano(
                        cartasJugador1Numero,
                        cartasJugador1Palo,
                        asCambiadoJugador1,
                        asManoJugador1,
                        valorManoJugador1,
                    )
                    print(mostrarMano)

                    print(f"La mano del J2 - {nombreJ2} esta compuesta de: ")
                    mostrarMano = imprimir_Mano(
                        cartasJugador2Numero,
                        cartasJugador2Palo,
                        asCambiadoJugador2,
                        asManoJugador2,
                        valorManoJugador2,
                    )
                    print(mostrarMano)

                    ronda += 1

                # Comprobar quien ha ganado

                ganadorStr = comprobar_Ganador(
                    valorManoJugador1, valorManoJugador2, ronda, nombreJ1, nombreJ2
                )
                ganadorStr1 = ganadorStr[0 : ganadorStr.find("&")]
                ganadorStr2 = ganadorStr[ganadorStr.find("&") + 1 : len(ganadorStr)]

        else:
            borrar_Consola()
            print(
                f"""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                                                                      █
█ Opción seleccionada:                                                 █
█                                                                      █
█ Jugar contra la máquina.                                             █
█                                                                      █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""
            )

            # Crea 2 cadenas de caracteres, una con el numero de cada carta y otra con el palo de dicha carta

            if contadorNumeroCarta > 25:
                barajaNumeros = "A234567890JQKA234567890JQKA234567890JQKA234567890JQK"
                barajaPalos = "CCCCCCCCCCCCCTTTTTTTTTTTTTPPPPPPPPPPPPPDDDDDDDDDDDDD"
                contadorNumeroCarta = 0

                barajaStr = barajar_Baraja(barajaNumeros, barajaPalos)

                barajaNumerosBarajada = barajaStr[0 : barajaStr.find("&")]
                barajaPalosBarajada = barajaStr[
                    barajaStr.find("&") + 1 : len(barajaStr)
                ]

            cartasJugador1Numero = ""
            cartasJugador2Numero = ""
            cartasJugador1Palo = ""
            cartasJugador2Palo = ""
            valorManoJugador1 = 0
            valorManoJugador2 = 0
            asCambiadoJugador1 = False
            asCambiadoJugador2 = False
            asManoJugador1 = False
            asManoJugador2 = False

            # Pedir apodos de jugadores

            nombreJ1 = input("Introduzca el apodo del jugador 1: ")
            nombreJ2 = "CPU"

            # Da 2 cartas al jugador1

            darCartaStr = dar_Carta(
                barajaNumerosBarajada,
                barajaPalosBarajada,
                contadorNumeroCarta,
                cartasJugador1Numero,
                cartasJugador1Palo,
                valorManoJugador1,
                asCambiadoJugador1,
                asManoJugador1,
            )
            contadorNumeroCarta = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador1Numero = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador1Palo = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            valorManoJugador1 = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asCambiadoJugador1 = bool(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asManoJugador1 = bool(darCartaStr)

            darCartaStr = dar_Carta(
                barajaNumerosBarajada,
                barajaPalosBarajada,
                contadorNumeroCarta,
                cartasJugador1Numero,
                cartasJugador1Palo,
                valorManoJugador1,
                asCambiadoJugador1,
                asManoJugador1,
            )
            contadorNumeroCarta = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador1Numero = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador1Palo = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            valorManoJugador1 = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asCambiadoJugador1 = bool(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asManoJugador1 = bool(darCartaStr)

            # Da 2 cartas al jugador2

            darCartaStr = dar_Carta(
                barajaNumerosBarajada,
                barajaPalosBarajada,
                contadorNumeroCarta,
                cartasJugador2Numero,
                cartasJugador2Palo,
                valorManoJugador2,
                asCambiadoJugador2,
                asManoJugador2,
            )
            contadorNumeroCarta = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador2Numero = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador2Palo = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            valorManoJugador2 = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asCambiadoJugador2 = bool(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asManoJugador2 = bool(darCartaStr)

            darCartaStr = dar_Carta(
                barajaNumerosBarajada,
                barajaPalosBarajada,
                contadorNumeroCarta,
                cartasJugador2Numero,
                cartasJugador2Palo,
                valorManoJugador2,
                asCambiadoJugador2,
                asManoJugador2,
            )
            contadorNumeroCarta = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador2Numero = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            cartasJugador2Palo = darCartaStr[0 : darCartaStr.find("&")]
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            valorManoJugador2 = int(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asCambiadoJugador2 = bool(darCartaStr[0 : darCartaStr.find("&")])
            darCartaStr = darCartaStr[darCartaStr.find("&") + 1 : len(darCartaStr)]
            asManoJugador2 = bool(darCartaStr)

            borrar_Consola()

            # Se imprime por pantalla las cartas que tiene el jugador asi como el valor total de la mano

            print(f"La mano del J1 - {nombreJ1} esta compuesta de: ")
            mostrarMano = imprimir_Mano(
                cartasJugador1Numero,
                cartasJugador1Palo,
                asCambiadoJugador1,
                asManoJugador1,
                valorManoJugador1,
            )
            print(mostrarMano)

            print(f"La mano del J2 - {nombreJ2} esta compuesta de: ")
            mostrarMano = imprimir_Mano(
                cartasJugador2Numero,
                cartasJugador2Palo,
                asCambiadoJugador2,
                asManoJugador2,
                valorManoJugador2,
            )
            print(mostrarMano)

            ronda = 1

            # Comprueba si los jugadores suman 21 con las 2 cartas iniciales

            if (valorManoJugador1 == 21) and (valorManoJugador2 == 21):
                ganadorStr1 = "JUEGO TERMINADO - Ronda 1"
                ganadorStr2 = "¡Empate!"

            elif valorManoJugador1 == 21:
                ganadorStr1 = f"JUEGO TERMINADO - Ronda 1"
                ganadorStr2 = f"¡Gana J1 - {nombreJ1}!"

            elif valorManoJugador2 == 21:
                ganadorStr1 = f"JUEGO TERMINADO - Ronda 1"
                ganadorStr2 = f"¡Gana J2 - {nombreJ2}!"

            # Pregunta al jugador si quiere plantarse con el valor que tiene o seguir pidiendo cartas

            else:
                jugador1Plantarse = False
                jugador2Plantarse = False
                while jugador1Plantarse == False or jugador2Plantarse == False:
                    if jugador1Plantarse == False:
                        print(
                            f"""J1 - {nombreJ1} seleccione una opción:
1) Pedir carta.
2) Plantarse."""
                        )
                        opcion = pedir_Opcion(2)
                        if opcion == "1":
                            print(f"J1 - {nombreJ1} pide otra carta.")
                            print("")
                            darCartaStr = dar_Carta(
                                barajaNumerosBarajada,
                                barajaPalosBarajada,
                                contadorNumeroCarta,
                                cartasJugador1Numero,
                                cartasJugador1Palo,
                                valorManoJugador1,
                                asCambiadoJugador1,
                                asManoJugador1,
                            )
                            contadorNumeroCarta = int(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            cartasJugador1Numero = darCartaStr[
                                0 : darCartaStr.find("&")
                            ]
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            cartasJugador1Palo = darCartaStr[0 : darCartaStr.find("&")]
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            valorManoJugador1 = int(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            asCambiadoJugador1 = bool(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            asManoJugador1 = bool(darCartaStr)
                            if valorManoJugador1 > 21:
                                print(f"J1 - {nombreJ1} se ha pasado.")
                                print("")
                                jugador1Plantarse = True
                        else:
                            print(f"J1 - {nombreJ1} se planta.")
                            print("")
                            jugador1Plantarse = True
                    if jugador2Plantarse == False:
                        if valorManoJugador2 < 17 or (
                            valorManoJugador1 < 22
                            and valorManoJugador2 < valorManoJugador1
                        ):
                            print(f"J2 - {nombreJ2} pide otra carta.")
                            print("")
                            darCartaStr = dar_Carta(
                                barajaNumerosBarajada,
                                barajaPalosBarajada,
                                contadorNumeroCarta,
                                cartasJugador2Numero,
                                cartasJugador2Palo,
                                valorManoJugador2,
                                asCambiadoJugador2,
                                asManoJugador2,
                            )
                            contadorNumeroCarta = int(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            cartasJugador2Numero = darCartaStr[
                                0 : darCartaStr.find("&")
                            ]
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            cartasJugador2Palo = darCartaStr[0 : darCartaStr.find("&")]
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            valorManoJugador2 = int(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            asCambiadoJugador2 = bool(
                                darCartaStr[0 : darCartaStr.find("&")]
                            )
                            darCartaStr = darCartaStr[
                                darCartaStr.find("&") + 1 : len(darCartaStr)
                            ]
                            asManoJugador2 = bool(darCartaStr)
                            if valorManoJugador2 > 21:
                                print(f"J2 - {nombreJ2} se ha pasado.")
                                print("")
                                jugador2Plantarse = True
                        else:
                            jugador2Plantarse = True
                            print(f"J2 - {nombreJ2} se planta.")
                            print("")
                    # Se imprime por pantalla las cartas que tiene el jugador asi como el valor total de la mano

                    borrar_Consola()

                    print(f"La mano del J1 - {nombreJ1} esta compuesta de: ")
                    mostrarMano = imprimir_Mano(
                        cartasJugador1Numero,
                        cartasJugador1Palo,
                        asCambiadoJugador1,
                        asManoJugador1,
                        valorManoJugador1,
                    )
                    print(mostrarMano)

                    print(f"La mano del J2 - {nombreJ2} esta compuesta de: ")
                    mostrarMano = imprimir_Mano(
                        cartasJugador2Numero,
                        cartasJugador2Palo,
                        asCambiadoJugador2,
                        asManoJugador2,
                        valorManoJugador2,
                    )
                    print(mostrarMano)

                    ronda += 1

                # Comprobar quien ha ganado

                ganadorStr = comprobar_Ganador(
                    valorManoJugador1, valorManoJugador2, ronda, nombreJ1, nombreJ2
                )
                ganadorStr1 = ganadorStr[0 : ganadorStr.find("&")]
                ganadorStr2 = ganadorStr[ganadorStr.find("&") + 1 : len(ganadorStr)]

        if partidasJugadas < 999:
            partidasJugadas += 1


if __name__ == "__main__":
    main()
    