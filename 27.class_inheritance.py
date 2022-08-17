class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})" # the !r calls the rpr method of self.name so that it shows up with quotes already in it.

    def disconnect(self):
        self.connected = False


# printer = Device("Printer", "USB")
# print(printer)

# We don't want to add printer-specific stuff to Device, so...


class Printer(Device): #what adding the () and putting device into it means is that your putting in a new class called printer and it inherites from "device", which is the function above.
    def __init__(self, name, connected_by, capacity):
        # super(Printer, self).__init__(name, connected_by)  - Python2.7
        super().__init__(name, connected_by)  # Python3+. what this does is gets the parent class and calls the init method of that super class i.e parent class.
        self.capacity = capacity #maximum capacity
        self.remaining_pages = capacity #current capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
          print("Device is disconnected at this time, cannot print.")
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.print(50)
print(printer)
printer.disconnect()
printer.print(30)  # Error