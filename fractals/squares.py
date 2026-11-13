import turtle

# Inicjalizacja zolwia oraz okna
t = turtle.Turtle('turtle')
window = turtle.Screen()
t.speed(0)  # Maksymalna predkosc rysowania

# Defaultowe ustawienie kata zolwia
t.left(90)

# Rekurencyjna funkcja do rysowania fraktalnych kwadratow
def draw_squares(bok, min):
    # Warunek koncowy rekurencji
    if bok < min:
        return
    # Glowna petla funkcji
    for i in range(2):
        # "Boki" kwadratu
        t.forward(bok / 4)     
        t.left(90)             
        draw_squares(bok / 2, min)    
        t.right(90)            
        t.forward(3 * bok / 4) 
        t.right(90)      
        # "Podstawy" kwadratu   
        t.forward(bok)         
        t.right(90)            

# Wywolanie funkcji z poczatkowa dlugoscia boku 200 i minimalna 100
draw_squares(200, 100)

# Zamkniecie okna po kliknieciu
window.exitonclick()
