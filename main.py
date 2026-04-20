# 1
class Message:
    def __init__(self, text):
        self.text = text

    def send(self):
        print("Xabar yuborildi")

    def delete(self):
        print("Xabar o‘chirildi")


a = Message("Salom")
a.send()

# 2
class File:
    def __init__(self, name):
        self.name = name

    def open(self):
        print("file.txt ochildi")

    def close(self):
        print("file.txt yopildi")


a = File("file.txt")
a.open()

# 3
class DoorLock:
    def __init__(self, locked):
        self.lock = locked


    def unlock(self):
        print("Unlocking")

    def lock(self):
        print("Locking")


a = DoorLock(2)
a.unlock()

# 4
class Camera:
    def __init__(self, mode):
        self.mode = mode

    def capture(self):
        print("Rasm olindi")

    def switch_mode(self):
        print("Switch mode")


a = Camera("chikirik")
a.switch_mode()

# 5
class Email:
    def __init__(self, address):
        self.address = address


    def send(self):
        print("Email yuborildi")

    def receive(self):
        print("Email qabul qilindi")


a = Email("<EMAIL>")
a.send()
