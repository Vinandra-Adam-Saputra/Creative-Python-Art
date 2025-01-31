import turtle

# Mengatur layar
window = turtle.Screen()
window.bgcolor('black')
window.title("Galactic Flower - Modified Version")

# Fungsi untuk menggambar lingkaran bertingkat
def draw_circles(t, size, repeat, decrement):
    for _ in range(repeat):
        for _ in range(4):  # Menggambar 4 lingkaran dalam satu iterasi
            t.circle(size)
            size -= decrement
        t.right(360 / repeat)

# Membuat objek turtle pertama
t1 = turtle.Turtle()
t1.speed(20)
t1.color('cyan')
draw_circles(t1, 150, 10, 5)

# Membuat objek turtle kedua
t2 = turtle.Turtle()
t2.speed(20)
t2.color('magenta')
draw_circles(t2, 120, 8, 10)

# Membuat objek turtle ketiga
t3 = turtle.Turtle()
t3.speed(20)
t3.color('orange')
draw_circles(t3, 90, 6, 15)

# Membuat objek turtle keempat
t4 = turtle.Turtle()
t4.speed(20)
t4.color('lime')
draw_circles(t4, 60, 4, 20)

# Membuat objek turtle kelima
t5 = turtle.Turtle()
t5.speed(20)
t5.color('pink')
draw_circles(t5, 30, 3, 25)

# Menyelesaikan penggambaran
turtle.done()