class emio:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Employee Destroyed.")
el = emio()
print("This is the middle of the program")