# Die Klasse Tokenizer erzeugt bei der Überprüfung der Eingabe gewisse formale Regeln. Tritt ein Fehler auf,
# so wird eine passende Exception geworfen.
# Diese Exceptions sind hier zu deklarieren.
# OperationException meldet (undifferenziert), dass ein falsches Operationszeichen vorliegt.
# NumberFormatException meldet einen Fehler in der Umsetzung der Zeichenkette in eine Zahl. Dazu wird hier die
# falsche Zeichenkette mitgeliefert.
# Passen Sie den Code unten nun so an, dass der Konstruktor der Oberklasse mit der passenden Meldung
# initialisiert wird.

class OperationException(Exception):
    def __init__(self):
        super().__init__('ERROR: ungültiges Operationszeichen eingegeben!')


class NumberFormatException(Exception):
    def __init__(self, value):
        super().__init__(f'ERROR: {value} Text ist ein ungültiger Zahlenwert')
