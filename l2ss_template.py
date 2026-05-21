# Schablone Testbeispiele und Testcode für Sudoku-Lösen 
# Teil von Algorithmen und Datenstrukturen 2. Kantijahr
# Andreas Döring, Mai 2026

# Teil 1: Beispiele zur Erläuterung
# Ein Sudoku-Rätsel wird durch eine Liste der vorbelegten Felder angegeben:
# in dem Format (Zeile,Spalte,Wert),
# Zeile, Spalte,Wert sind integer 1-9

# wird für Tests benötigt
import sys

sudoku_beispiel1 = [(1,1,8),(1,7,2),(1,8,9),(1,9,3),
                    (2,4,6),(2,6,5),
                    (3,1,7),(3,5,2),(3,6,9),(3,8,4),
                    (4,1,5),(4,2,9),(4,3,2),(4,8,3),
                    (5,1,1),(5,3,4),(5,5,8),(5,7,5),(5,9,6),
                    (6,2,6),(6,7,7),(6,8,1),(6,8,9),
                    (7,2,8),(7,4,3),(7,5,4),(7,9,1),
                    (8,4,7),(8,6,8),
                    (9,1,2),(9,2,4),(9,9,7)
                   ]

# Einige Konstanten
# einsbisneun wird so oft gebraucht, das wird abgekürzt
eb9 = list(range(1,10))

# Die wichtigste Datenstruktur: das (teilgelöste) Feld

# Das GesamtFeld ist eine  Liste von Zeilen, jede Zeile ist eine Liste von Feldern, 
# jedes Feld ist eine Liste von möglichen Werten. 
# Zu Anfang sind in jedem Feld alle Werte möglich 
gesamtfeld = [[eb9[:] for r in eb9[:]] for c in eb9[:]]

# -----------------------------------------------------------------
# Zu erstellen von Gruppe "Gesamtfeld":
# bearbeiten Sie zuerst Lies_Feld 
 
# Wichtigste Operationen fuer das Gesamtfeld:
# Auslesen eines einzelfeldes
# Aktualisieren eines Einzelfeldes: dabei Testen, ob sich die Liste des Einzelfeldes  verkleinert,
# es dürfen keine neuen Werte hinzukommen
# Falls das Feld dann leer ist ...
# Es wird ein paar zurueckgegeben, (feld_wurde_kleiner,feld_ist_jetzt_leer)
#  !!!!!!!!!
# Achtung: die Indizes des Gesamtfelds beginnen bei 0, aber die Numerierung von 
# Zeilen und Spalten beginnt bei 1!

def Lies_Feld(zeile,spalte):
    # ersetze durch Befehle, so dass aus der Variable "gesamtfeld" das Feld in Zeile/Spalte gelesen wird
    return [1]

def Aktualisiere_Feld(zeile,spalte,neuer_wert):
    alter_wert = lies_feld(zeile,spalte)
    # Beginne mit einer leeren Ergebnisliste 
    # gehe die Liste alter_wert durch, teste für jeden Eintrag, ob element in neuer_wert enthalten ist, 
    # falls ja, füge an Ergebnisliste an. 
    # (1) vergleiche Länge der Ergebnisliste mit Laenge von alter_wert.
    # (2) Prüfe ob Ergebnisliste leer ist.
    # Berechne Differenz der Länge von alter_wert und Länge von Ergebnisliste. 
    # Ziehe diese Differenz von SummeFeldGroessen ab.
    # Gib die zwei bedingungen zurueck.
    return [False,False]

# wenn man die Summe der Längen der Einzelfelder mitführt, kann man einfach 
# feststellen, ob das Sudoku gelöst ist. 
# richtiger Initialwert muss eingesetzt werden
# Der Initialwert ist für ein ganz leeres Sudoku, es sind also zunächst gar keine 
# Vorgaben ausgefüllt
SummeFeldGroessen = 0
# 

def ist_geloest():
    # ersetze "False" durch richtigen Test, verwende SummeFeldGroessen 
    return False
    

# ----------------------------------------------------
# Gruppe Anzeigen
# Um das sudoku-gesamtfeld anzuzeigen, 
# muss ein einzelnes Feld angezeigt werden. 
# die gesamte Menge anzuzeigen, wäre etwas unübersichtlich,
# deshalb soll bei einem einzigen Wert dieser Angezeigt werden, bei zwei Werten ein Doppelpunkt,
# bei drei bis 8 werten ein *
# und bei 9 Werten ein " " (Leerzeichen)  
def Zeichen_Einzelfeld(zeile,spalte):
    # diese Funktion liefert das Zeichen zurück, das beim Ausgeben eines Feldes angezeigt wird
    # verwende die Funktion lies_feld um die Werte-Liste des Feldes zu erhalten. 
    return " "

def Zeige_Zwischenzeile():
    # Um ein Gesamtfeld anzuzeigen werden Abwechselnd Zwischenzeilen aus "-" 
    # Da ein gesamtfeld aus 9 Einzelfeldern besteht, und jeweils ein Trenner zwischen 
    # zwei Feldern gezeigt wird, und es einen Rand geben soll, ist eine Zwischenzeile ... Zeichen lang
    print()

def Zeige_Wertezeile(zeile):
    # Zeige eine Zeile des gesamtfelds an, so dass am Anfang ein "|" steht, und dann abwechelnd ein Zeichen 
    # nach der Funktion Zeichen_Einzelfeld
    print()
    
def Zeige_Gesamtfeld():
    # Zeige Abwechselnd eine Zwischenzeile und eine Wertezeile.
    return 
    
# -------------------------------------------

# Gruppe Zeile/Spalte
# Für viele schlussfolgerungen müssen alle Felder in der gleichen Zeile oder gleichen Spalte  
#  von einem gegebenen Feld  ohne das Feld selbst geprüft werden. 
# Dafür gibt es zwei Funktionen, die eine Liste der Koordinaten zurückgeben
# Beispielé 
# print(Andere_Zeilen_Felder(4,2)) 
# [(4,1),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9)]

def Andere_Zeilen_Felder(zeile,spalte):
    Ergebnis = []
    # Ergänze eine Schleife, die Ergebnis füllt
    return Ergebnis
    
def Andere_Spalten_Felder(zeile,spalte):
    Ergebnis = []
    # Ergänze eine Schleife, die Ergebnis füllt
    return Ergebnis

# -------------------------------------
# Gruppe Quadrat
# Das selbe wie für Zeilen/Spalten nur für das Quadrat
# Beispiel: 
# print(Andere_Zeilen_Felder(4,2))
# 
def Andere_Quadrat_Felder(zeile,spalte):
    Ergebnis = []
    # ...
    return Ergebnis

# Gemeinsam für alle schlussfolgerungs-Funktionen:
# Die Funktion gibt drei Boole-sche Werte zurueck, 
# der erste Wert, ob die Schlussfogerung möglich war, 
# falls der falsch, sind auch die anderen beiden Werte falsch,
# falls es wahr ist, die Schlussfolgerung also angewendet werden konnte, 
# werden die beiden Rückgabewerte von Aktualasiere_Feld zurueckgegeben.

# --------------------------------------
# Gruppe Schlussfolgerung 1
def Schlussfolgerung_1(zeile,spalte):
    # Teste, ob für das Feld Schlussfolgerung 1 gilt, das heisst nur noch ein möglicher Wert 
    # vorhanden ist. Falls ja, aktualisiere alle Felder in der gleichen Spalte, gleichen Zeile,
    # und dem gleichen Quadrat (verwende die Funktionen oben) durch Streichen des 
    # einzigen Werts. Verwende die Funktion Aktualisiere_Feld.     
    return (False,False,False)    
# --------------------------------------
# Gruppe Schlussfolgerung 2
def Schlussfolgerung_2_Liste(zeile,spalte,l):
    # Hilfsfunktion: bestimme die Liste der Elemente des Feldes (zeile,spalte), die 
    # in keinem anderen Feld der Liste l vorkommen. 
    # Hat diese Liste nur ein Element, ist die Schlussfolgerung 2 anwendbar.
    return []

def Schlussfolgerung_2(zeile,spalte):
    # Teste, ob fuer dieses Feld eine Ziffer zulässig ist, die in der zugehörigen Zeile/Spale/Quadrat 
    # in keinem anderen Feld möglich ist. 
    # Falls ja, Aktualisiere dieses Feld mit der Funktion "Aktualisiere_Feld".
    # Verwende die Funktion Schlussfolgerung_2_Liste auf Zeile/Spalte/Quadrat und 
    # prüfe, ob das Ergebnis nur genau ein Element enthält.
    return (False,False,False)    
       
# --------------------------------------
# Gruppe Schlussfolgerung 3
def Schlussfolgerung_3():    
    # In einem Quadrat bleiben für eine Ziffer mehrere Felder, 
    # aber in derselben Zeile/Spalte. Dann kann diese Ziffer 
    # in den anderen Quadraten in derselben Zeile/Spalte entfernt werden
    return (False,False,False)    


# --------------------------------------
# Gruppe Schlussfolgerung 4
def Schlussfolgerung_4():
    # In der Zeile/Spalte/Quadrat sind zwei Felder mit den selben zwei möglichen Ziffern,
    # und diese zwei Ziffern sind noch in anderen Feldern der Zeile/Spalte/Quadrat möglich. 
    # Sie können dort gestrichen werden.
    return (False,False,False)    

# --------------------------------
# end of code for students
# --------------------------------    
# -----------------------------------------------------------------------------
# gesamt-schleife
# 1. Einlesen von Vorgaben
# Die Vorgaben sind eine Liste von (zeile,spalte,wert)
def bearbeite_vorgaben(l):
    global SummeFeldGroessen
    for vi in l:
        # spater Aktualisiere_Feld
        assert len(vi) == 3
        assert vi[0] in eb9
        assert vi[1] in eb9
        assert vi[2] in eb9
        gesamtfeld[vi[0]-1][vi[1]-1] = [vi[2]]
    SummeFeldGroessen = SummeFeldGroessen - 8 * len(l)



def suche_loesung():
    # die einfachste Variante ist, kontinuierlich alle Felder durchzugehen, 
    # und auf mögliche Schlussfolderung zu testen. Erst wenn bei einem kompletten Durchgang keine Schlussfolgerung 
    # mehr gefunden wird, muss man aufgeben    
    # die arbeitsliste wird nicht verwendet:
    eine_schlussfolgerung_gefunden = True
    unloesbar = False
    while eine_schlussfolgerung_gefunden and not unloesbar and not ist_geloest():
       eine_schlussfolgerung_gefunden = False
       for zeile in eb9:
         for spalte in eb9:
            (f1,f2,f3) = Schlussfolgerung_1(zeile,spalte)
            if f1:
                print("l2ss.Schlussfolgerung_1(",zeile,",",spalte,")")
            eine_schlussfolgerung_gefunden = eine_schlussfolgerung_gefunden or f1
            unloesbar = unloesbar or f3
            (f1,f2,f3) = Schlussfolgerung_2(zeile,spalte)
            if f1:
                print("l2ss.Schlussfolgerung_2(",zeile,",",spalte,")")
            eine_schlussfolgerung_gefunden = eine_schlussfolgerung_gefunden or f1
            unloesbar = unloesbar or f3
            # ebenso Schlussfolgerung_3 und Schlussfolgerung_4 falls vorhanden


# Mehr Beispiele:
sudoku_beispiel2 = [
(1,3,2),(1,4,7),(1,8,8),(1,9,3),
 (2,3,3),(2,4,2),
 (3,3,7),(3,6,1),(3,8,9),(3,9,5),
 (4,1,8),(4,6,4),
 (5,1,7),(5,2,6),(5,5,1),(5,8,4),(5,9,2),
 (6,4,9),(6,9,1),
 (7,1,3),(7,2,1),(7,3,5),(7,1,6),
 (8,6,6),(8,7,1),
 (9,1,2),(9,2,9),(9,6,3),(9,7,5)
]

# "Tele meisterlich"
sudoku_beispiel3 = [
 (1,4,6),(1,6,3),(1,9,5),
 (2,3,9),(2,8,2),(2,9,8),
 (3,2,1),(3,3,4),(3,6,8),
 (4,4,1),(4,8,9),
 (5,1,1),(5,5,6),(5,9,3),
 (6,2,5),(6,6,9),
 (7,4,4),(7,7,3),(7,8,7),
 (8,1,7),(8,2,8),(8,7,4),
 (9,1,2),(9,4,9),(9,6,5)]
 
# anderes Teleheft
sudoku_beispiel4 = [
(1,4,4),(1,6,1),
(2,1,6),(2,2,1),(2,8,9),(2,9,5),
(3,6,5),(3,7,1),(3,9,8),
(4,1,9),(4,2,5),(4,5,4),(4,6,2),(4,7,8),(4,9,3),
(5,3,7),(5,5,8),(5,7,9),
(6,1,3),(6,3,2),(6,4,6),(6,5,1),(6,8,5),(6,9,7),
(7,1,2),(7,3,8),(7,4,1),
(8,1,5),(8,2,7),(8,8,2),(8,9,4),
(9,4,3),(9,6,7)] 

sudoku_beispiel5 = [
(1,2,5),(1,7,2),(1,9,1),
(2,1,1),(2,4,8),(2,7,4),(2,8,6),
(3,5,3),(3,6,7),(3,8,9),
(4,3,3),(4,5,5),(4,9,4),
(5,2,1),(5,5,9),(5,8,7),
(6,1,6),(6,5,1),(6,7,9),
(7,2,6),(7,4,4),(7,5,8),
(8,2,9),(8,3,5),(8,6,1),(8,9,6),
(9,1,4),(9,3,7),(9,8,1)]

sudoku_beispiel6 = [
(1,4,8),(1,6,3),(1,9,5),
(2,3,7),(2,8,8),(2,9,4),
(3,2,4),(3,3,3),(3,6,5),
(4,4,6),(4,8,3),
(5,1,7),(5,5,9),(5,9,2),
(6,2,8),(6,6,1),
(7,4,5),(7,7,7),(7,8,6),
(8,1,4),(8,2,7),(8,7,2),
(9,1,3),(9,4,1),(9,6,6)]

sudoku_beispiel7 = [
(1,1,4),(1,3,7),(1,7,6),(1,8,2),
(2,2,1),
(3,2,6),(3,3,2),(3,4,8),(3,6,3),(3,8,9),(3,9,7),
(4,2,5),(4,3,8),(4,6,9),(4,8,4),
(5,1,2),(5,5,5),(5,9,9),
(6,2,9),(6,4,1),(6,7,5),(6,8,7),
(7,1,9),(7,2,2),(7,4,4),(7,6,1),(7,7,8),(7,8,3),
(8,8,1),
(9,2,4),(9,3,5),(9,7,7),(9,9,2)]


# Test functions. Partially by github copilot (Claude Haiku 4.5
def reset_sudoku():
    """Reset the global gesamtfeld and SummeFeldGroessen"""
    global gesamtfeld, SummeFeldGroessen
    gesamtfeld = [[eb9[:] for r in eb9[:]] for c in eb9[:]]
    SummeFeldGroessen = 9*9*9

def assert_equal(actual, expected, msg=""):
    """Simple assertion function"""
    if actual != expected:
        print(f"   Fehler: {msg}")
        print(f"   Erwartet: {expected}")
        print(f"   Tatsaechlich:      {actual}")
        return False
    else:
        print(f"  Bestanden: {msg}")
        return True


# poor man's unittest mock
def Ausfuehren_mit_ersatz(ident,ersatz,f,*fargs):
   save_orig = sys.modules['l2ss'].__dict__[ident]
   res = "Fehlgeschlagen"
   try:
      sys.modules['l2ss'].__dict__[ident] = ersatz
      res = f(*fargs)
   finally:
      sys.modules['l2ss'].__dict__[ident] = save_orig       
   return res



def test_lies_feld():
    """Test Lies_Feld (read field)"""
    reset_sudoku()
    
    # Test reading initial field (should contain all values 1-9)
    feld = Lies_Feld(1, 1)
    assert_equal(feld, eb9, "Field (1,1) sollte [1-9] enthalten")
    
    # Test reading different positions
    feld_middle = Lies_Feld(5, 5)
    assert_equal(feld_middle, eb9, "Field (5,5) should contain [1-9]")
    
    gesamtfeld[2][3] = [7]
    feld_neuer_wert = Lies_Feld(3, 4)
    assert_equal(feld_middle, [7], "Field (3,4) sollte [7] enthalten")
    
    feld_corner = Lies_Feld(9, 9)
    assert_equal(feld_corner, eb9, "Field (9,9) should contain [1-9]")

def test_aktualisiere_feld_mitlf():
    # dieser Test nummt an, dass Lies_Feld funktioniert
    # Test reducing possibilities
    result = Aktualisiere_Feld(1, 1, [1, 2, 3])
    feld = gesamtfeld(0, 0)
    assert_equal(feld, [1, 2, 3], "Feld sollte reduziert sein auf [1,2,3]")
    assert_equal(result[0], True, "Feld Groesse verkleinert (first flag True)")
    assert_equal(result[1], False, "Feld ist nicht leer (second flag False)")
    
    # Test further reduction
    result = Aktualisiere_Feld(1, 1, [1,4,5])
    feld = gesamtfeld(0, 0)
    assert_equal(feld, [1], "Field should be reduced to [1]")
    
    # Test intersecting lists
    reset_sudoku()
    Aktualisiere_Feld(2, 2, [3, 4, 5])
    feld = Lies_Feld(2, 2)
    assert_equal(feld, [3, 4, 5], "Field (2,2) should be [3,4,5]")
    # TODO check SummeFeldGroessen

# Haengt von dem Test oben ab!
mockf11 = eb9[:]
mockf22 = eb9[:]
def mocklf_4_test_af(z,s):
    global mockf11,mockf22
    if z == 1:
        return mockf11
    elif z == 2:
        return mockf22

def test_aktualisiere_feld():
    """Test Aktualisiere_Feld (update field)
       unabhaengig von Lies_Feld"""
    global mockf11
    mockf11 = eb9[:]
    Ausfuehren_mit_ersatz('Lies_Feld',mocklf_4_test_af,test_aktualisiere_feld_mitlf) 
    
def test_ist_geloest():
    """Test ist_geloest (check if solved)"""
    reset_sudoku()
    
    # Initially not solved
    assert_equal(ist_geloest(), False, "Fresh puzzle should not be solved")
    
    # Manually set all fields to single values (simulate solved state)
    reset_sudoku()
    global SummeFeldGroessen
    for zeile in eb9:
        for spalte in eb9:
            gesamtfeld[zeile-1][spalte-1] = [((zeile + spalte) % 9) + 1]
    SummeFeldGroessen = 81
    
    assert_equal(ist_geloest(), True, "Sudoku mit Feldsumme 81 ist gelöst")

# =========================================================================
# TESTS FÜR GRUPPE: ANZEIGEN (Display functions)
# =========================================================================


def test_zeichen_einzelfeld_ohnelf():
    """Test Zeichen_Einzelfeld (get display character)"""
    reset_sudoku()
    
    # Test 9 values -> space
    zeichen = Zeichen_Einzelfeld(1, 1)
    assert_equal(zeichen, " ", "9 values should display as space")
    
    # Test 1 value -> digit
    reset_sudoku()
    gesamtfeld[0][0] = [5]
    zeichen = Zeichen_Einzelfeld(1, 1)
    assert_equal(zeichen, "5", "1 Wert (5) Sollte als  '5' angezeigt werden")
    
    # Test 2 values -> colon
    reset_sudoku()
    gesamtfeld[0][0] = [3, 7]
    zeichen = Zeichen_Einzelfeld(1, 1)
    assert_equal(zeichen, ":", "2 values should display as ':'")
    
    # Test 3-8 values -> asterisk
    reset_sudoku()
    gesamtfeld[0][0] =  [1, 2, 3, 4]
    zeichen = Zeichen_Einzelfeld(1, 1)
    assert_equal(zeichen, "*", "4 values should display as '*'")





# ---------- Dies benötigt ein funktionierendes "Lies_Feld"
# Beispiel 7 nach einer Reihe von Schlussfolgerungen:
test_gesamtfeld_data = [
[[4], [3, 8], [7], [5, 9], [1, 9], [1, 5], [6], [2], [1, 3, 5, 8]], 
[[3, 5, 8], [1], [3, 5, 9], [2, 4, 5, 6, 7, 9], [2, 4, 6, 7, 9], [2, 4, 5, 6, 7], 
 [3, 4, 8], [3, 5, 8], [3, 4, 5, 8]], 
[[5], [6], [2], [8], [1, 4], [3], [1, 4], [9], [7]], 
[[1, 3, 6, 7], [5], [8], [2, 3, 6, 7], [2, 3, 6, 7], [9], [1, 2, 3], [4], [1, 2, 3, 6]], 
[[2], [3, 4, 7], [1, 3, 4, 6], [3, 4, 6, 7], [5], [4, 6, 7, 8], [1, 3, 8], [1, 3, 6, 8], [9]], 
[[3, 6], [9], [3, 4, 6], [1], [2, 3, 4, 6, 8], [2, 4, 6, 8], [5], [7], [2, 3, 6, 8]], 
[[9], [2], [1, 3, 4, 5, 6], [4], [1, 2, 3, 4, 6, 7, 8], [1], [8], [3], [1, 2, 3, 4, 5, 6, 8]], 
[[1, 3, 5, 6, 7, 8], [2, 3, 4, 7, 8], [1, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7, 9], 
 [1, 2, 3, 4, 6, 7, 8, 9], [1, 2, 4, 5, 6, 7, 8], [1, 2, 3, 4, 7, 8, 9], [1], 
 [1, 2, 3, 4, 5, 6, 8]], 
[[1, 3, 5, 6, 7, 8], [4], [5], [2, 3, 4, 5, 6, 7, 9], [1, 2, 3, 4, 6, 7, 8, 9], 
 [1, 2, 4, 5, 6, 7, 8], [7], [1, 3, 5, 6, 8], [2]]
 ]

def test_zeige_gesamtfeld():
    """Test Zeige_Gesamtfeld (display entire board)"""
    reset_sudoku()
    gesamtfeld = test_gesamtfeld_data  
    
    print("\nGesamtfeld-A§nzeige")
    Zeige_Gesamtfeld()
    print("\nGesamtfeld sollte so aussehen")
    print("-------------------")
    print("|4|:|7|:|:|:|6|2|*|")
    print("-------------------")
    print("|*|1|*|*|*|*|*|*|*|")
    print("-------------------")
    print("|5|6|2|8|:|3|:|9|7|")
    print("-------------------")
    print("|*|5|8|*|*|9|*|4|*|")
    print("-------------------")
    print("|2|*|*|*|5|*|*|*|9|")
    print("-------------------")
    print("|:|9|*|1|*|*|5|7|*|")
    print("-------------------")
    print("|9|2|*|4|*|1|8|3|*|")
    print("-------------------")
    print("|*|*|*|*|*|*|*|1|*|")
    print("-------------------")
    print("|*|4|5|*|*|*|7|*|2|")
    print("-------------------")
    
def test_andere_zeilen_felder():
    """Test Andere_Zeilen_Felder (get other fields in row)"""
    
    result = Andere_Zeilen_Felder(4, 2)
    expected = [(4,1), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9)]
    assert_equal(result, expected, "Row 4, column 2: should get 8 other fields")
    
    result = Andere_Zeilen_Felder(1, 1)
    expected = [(1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9)]
    assert_equal(result, expected, "Row 1, column 1: should get columns 2-9")

def test_andere_spalten_felder():
    """Test Andere_Spalten_Felder (get other fields in column)"""
    
    result = Andere_Spalten_Felder(4, 2)
    expected = [(1,2), (2,2), (3,2), (5,2), (6,2), (7,2), (8,2), (9,2)]
    assert_equal(result, expected, "Row 4, column 2: should get 8 other fields in column 2")
    
    result = Andere_Spalten_Felder(1, 1)
    expected = [(2,1), (3,1), (4,1), (5,1), (6,1), (7,1), (8,1), (9,1)]
    assert_equal(result, expected, "Row 1, column 1: should get rows 2-9 in column 1")

def test_andere_quadrat_felder():
    """Test Andere_Quadrat_Felder (get other fields in 3x3 box)"""
    
    # Top-left box (rows 1-3, cols 1-3)
    result = Andere_Quadrat_Felder(1, 1)
    # Should include all 8 other fields in top-left 3x3 box
    assert_equal(len(result), 8, "Box should have 8 other fields")
    assert_equal((1,2) in result, True, "Should contain (1,2)")
    assert_equal((2,3) in result, True, "Should contain (2,3)")
    assert_equal((1,1) in result, False, "Should not contain itself (1,1)")
    
    # Center box (rows 4-6, cols 4-6)
    result = Andere_Quadrat_Felder(5, 5)
    assert_equal(len(result), 8, "Center box should have 8 other fields")
    assert_equal((5,5) in result, False, "Should not contain itself (5,5)")
    assert_equal((4,4) in result, True, "Should contain (4,4)")
    assert_equal((6,6) in result, True, "Should contain (6,6)")
    
    # Bottom-right box (rows 7-9, cols 7-9)
    result = Andere_Quadrat_Felder(9, 9)
    assert_equal(len(result), 8, "Bottom-right box should have 8 other fields")

# =========================================================================
# TESTS FÜR GRUPPE: SCHLUSSFOLGERUNG 1 (Constraint propagation rule 1)
# =========================================================================

def test_schlussfolgerung_1():
    """Test Schlussfolgerung_1 (if field has one value, remove from related fields)"""
    reset_sudoku()
    
    # Set field (1,1) to value 8
    Aktualisiere_Feld(1, 1, [8])
    
    # Apply rule 1
    result = Schlussfolgerung_1(1, 1)
    assert_equal(result[0], True, "Rule should be applicable (has single value)")
    
    # Check that 8 was removed from same row
    feld_row = Lies_Feld(1, 5)
    assert_equal(8 in feld_row, False, "8 should be removed from row 1")
    
    # Check that 8 was removed from same column
    feld_col = Lies_Feld(5, 1)
    assert_equal(8 in feld_col, False, "8 should be removed from column 1")
    
    # Check that 8 was removed from same box
    feld_box = Lies_Feld(2, 2)
    assert_equal(8 in feld_box, False, "8 should be removed from top-left box")

def test_schlussfolgerung_1_no_change():
    """Test Schlussfolgerung_1 when field has multiple values"""
    reset_sudoku()
    
    # Field with multiple values
    result = Schlussfolgerung_1(1, 1)
    assert_equal(result[0], False, "Rule should not apply (multiple values)")
    assert_equal(result[1], False, "No changes should be made")
    assert_equal(result[2], False, "No conflicts should be found")

# =========================================================================
# TESTS FÜR GRUPPE: SCHLUSSFOLGERUNG 2 (Constraint propagation rule 2)
# =========================================================================

def test_schlussfolgerung_2_liste():
    """Test Schlussfolgerung_2_Liste (helper function)"""
    reset_sudoku()
    
    # Set field to have value 7
    Aktualisiere_Feld(1, 1, [7, 6])
    # Set other fields in row to exclude 7
    Aktualisiere_Feld(1, 2, [1, 2, 3])
    Aktualisiere_Feld(1, 3, [2, 3, 4])
    Aktualisiere_Feld(1, 4, [1, 5, 6])
    Aktualisiere_Feld(1, 5, [1, 8, 9])
    Aktualisiere_Feld(1, 6, [1, 8, 9])
    Aktualisiere_Feld(1, 7, [1, 8, 9])
    Aktualisiere_Feld(1, 8, [1, 8, 9])
    Aktualisiere_Feld(1, 9, [1, 8, 9])
    
    other_fields = Andere_Zeilen_Felder(1, 1)
    result = Schlussfolgerung_2_Liste(1, 1, other_fields)
    assert_equal(result, [7], "Should find 7 as unique value in this field for the row")

def test_schlussfolgerung_2_no_unique():
    """Test Schlussfolgerung_2_Liste when no unique value exists"""
    reset_sudoku()
    
    # Set field to [5, 6]
    Aktualisiere_Feld(1, 1, [5, 6])
    # Make sure both 5 and 6 appear in other fields
    Aktualisiere_Feld(1, 2, [5, 7])
    Aktualisiere_Feld(1, 3, [6, 8])
    
    other_fields = Andere_Zeilen_Felder(1, 1)
    result = Schlussfolgerung_2_Liste(1, 1, other_fields)
    assert_equal(result, [], "Should return empty list when no unique value")

def test_schlussfolgerung_2():
    """Test Schlussfolgerung_2 (complete rule 2)"""
    reset_sudoku()
    
    # Create a scenario where field (1,1) should have unique value in row
    Aktualisiere_Feld(1, 1, [7,6])
    Aktualisiere_Feld(1, 2, [1, 2, 6])
    Aktualisiere_Feld(1, 3, [2, 3])
    Aktualisiere_Feld(1, 4, [1, 5])
    Aktualisiere_Feld(1, 5, [1, 8])
    Aktualisiere_Feld(1, 6, [1, 9])
    Aktualisiere_Feld(1, 7, [1, 2])
    Aktualisiere_Feld(1, 8, [2, 3])
    Aktualisiere_Feld(1, 9, [3, 4])
    
    result = Schlussfolgerung_2(1, 1)
    # Should find that 7 is unique in this field for the row
    assert_equal(result[0], True, "Rule 2 should apply")



def test_schlussfolgerung_2():
    """Test Schlussfolgerung_2 (complete rule 2)"""
    reset_sudoku()
    
    # Create a scenario where field (1,1) should have unique value in row
    Aktualisiere_Feld(1, 1, [7,6])
    Aktualisiere_Feld(1, 2, [1, 2,6])
    Aktualisiere_Feld(1, 3, [2, 3])
    Aktualisiere_Feld(1, 4, [1, 5])
    Aktualisiere_Feld(1, 5, [1, 8])
    Aktualisiere_Feld(1, 6, [1, 9])
    Aktualisiere_Feld(1, 7, [1, 2])
    Aktualisiere_Feld(1, 8, [2, 3])
    Aktualisiere_Feld(1, 9, [3, 4])
    
    result = Schlussfolgerung_2(1, 1)
    # Should find that 7 is unique in this field for the row
    assert_equal(result[0], True, "Rule 2 should apply")
