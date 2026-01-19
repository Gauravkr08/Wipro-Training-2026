class animal:
    def speak(self):
        print("animal makes sound")

class dog(animal):
    def barks(self):
        print("dog barks")
d=dog()
d.speak()
d.barks()