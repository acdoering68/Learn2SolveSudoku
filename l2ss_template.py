# Schablone Testbeispiele und Testcode für Sudoku-Lösen 
# Teil von Algorithmen und Datenstrukturen 2. Kantijahr
# Andreas Döring, Mai 2026

# Teil 1: Beispiele zur Erläuterung
# Ein Sudoku-Rätsel wird durch eine Liste der vorbelegten Felder angegeben:
# in dem Format (Zeile,Spalte,Wert),
# Zeile, Spalte,Wert sind integer 1-9

sudoku_beispiel1 = [(1,1,5),                  ]

# Einige Konstanten
# einsbisneun wird so oft gebraucht, das wird abgekürzt
eb9 = list(range(1,10))

geloest = 0
nichtloesbar = 1
aufgegeben = 2 # das hier verwendete Verfahren kann nicht alle Sudokus loesen

# Die Feldermengen mit gleichen Bedingungen, höhere Werte um Verwechslungen zu vermeiden
Zeile = 1000
Spalte = 1001
Quadrat = 1002

# Die zwei wichtigen Datenstrukturen: das (teilgelöste) Feld und die Arbeitsliste

# Das GesamtFeld ist eine  Liste von Zeilen, jede Zeile ist eine Liste von Feldern, 
# jedes Feld ist eine Liste von möglichen Werten. 
# Zu Anfang sind in jedem Feld alle Werte möglich 
gesamtfeld = [[eb9[:] for r in eb9[:]] for c in eb9[:]]