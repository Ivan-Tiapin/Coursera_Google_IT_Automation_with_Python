""" Prints the floor where the elevator is located. """
class Elevator:
    def __init__(self, bottom, top, current):
        self.current = current
        self.top = top
        self.bottom = bottom

    # Increases the current floor number
    def up(self):
        if self.current < self.top:
            self.current += 1

    # Decreases the current floor number
    def down(self):
        if self.current > self.bottom:
            self.current -= 1

    # Sends elevator to specific floor
    def go_to(self, floor): #
        self.current = floor

    def __str__(self):
        return "Current floor: {}".format(self.current)


elevator = Elevator(0, 10, 0)
elevator.up()
print(str(elevator.current) + " " + "#should output 1")
elevator.down()
print(str(elevator.current) + " " + "#should output 0")
elevator.go_to(10)
print(str(elevator.current) + " " + "#should output 10")

elevator.go_to(10)
elevator.up()
elevator.down()
print(str(elevator.current) + " " + "#should output 9")

elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(str(elevator.current) + " " + "#should output 1")

elevator.go_to(5)
print(elevator)
