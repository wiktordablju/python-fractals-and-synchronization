import turtle

# Inicjalizacja zolwia oraz okna
t = turtle.Turtle('turtle')
window = turtle.Screen()
t.speed(0)  # Maksymalna predkosc rysowania

# Ustawienie poczatkowego kata
t.left(60)

# Rekurencyjna funkcja do rysowania fraktalnego szesciokata
def draw_hexagons(bok, min):
    # Warunek koncowy rekurencji
    if bok < min:
        return
    # Glowna petla funkcji
    for i in range(6):
        draw_hexagons(bok / 3, min)  # Z kazda rekurencja bok zmniejszony jest o 1/3
        t.forward(bok)       
        t.right(60)          

# Wywolanie funkcji z poczatkowa dlugoscia boku 150 i minimalna 50
draw_hexagons(150, 50)

# Zamkniecie okna po kliknieciu
window.exitonclick()
