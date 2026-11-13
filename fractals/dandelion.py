import turtle

# Inicjalizacja zolwia oraz okna
t = turtle.Turtle('turtle')
window = turtle.Screen()
t.speed(0)  # Maksymalna predkosc rysowania

# Defaultowe ustawienie kata zolwia
t.left(90)

# Rekurencyjna funkcja do rysowania fraktalnych dmuchawcow
def draw_dandelion(bok, min):
    # Warunek koncowy rekurencji
    if bok < min:
        return
    
    # Glowna czesc funkcji, zolw najpierw idzie do przodu, a pozniej w petli rekurencyjnie rysuje sie przod-tyl oraz znak "x" 
    t.forward(bok)  
    for i in range(6):
        draw_dandelion(bok / 2, min)  
        t.right(60)          
    t.backward(bok)         

# Wywolanie funkcji z poczatkowa dlugoscia boku 200 i minimalna 100
draw_dandelion(200, 100)

# Zamkniecie okna po kliknieciu
window.exitonclick()
