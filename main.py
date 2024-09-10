import sys

if len(sys.argv) < 2:
    print("Передайте длину стороны квадрата.")
    exit() # выход из программы не полностью, все что ниже выполнено не будет.

square_side = sys.argv[1]

if not square_side.isnumeric():
    print("Передайте число в качестве строны квадрата.")
    exit()

perimeter = int(square_side) * 4
print(f"Периметр квадрата со стороной {square_side} равен {perimeter}")
