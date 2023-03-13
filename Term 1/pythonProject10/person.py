class Person(object):
    people_count = 0
    languages = ["Eng","Spn","Frn","Chi","Jap"]
    def __init__(self,name,alive=True,happy=False,mad=False,eyeColor="brown",gender="na",height=0,weight=0,age=0,bloodtype=0,hairColor="brown",race="na",):
        Person.people_count +=1
        self.name = name
        self.isAlive = alive
        self.happy = happy
        self.mad = mad
        self.language = ""
        self.eyeColor = eyeColor
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.bloodType = bloodtype
        self.allergies = []
        self.hairColor = hairColor
        self.race = race

    def speak(self,x):
        print(x)
    def walk(self):
        print("walking")
    def run(self):
        print("running")
    def die(self):
        self.isAlive = False
    def breath(self):
        pass
    def sleep(self):
        pass
    def jump(self):
        pass
    def grow(self):
        self.height += amount
    def gainWeight(self):
        self.wheight += amount
    def loseWheight(self):
        self.wheight -= amount

    def __str__(self):
        dis = self.name = "\n"
        dis += str(self.height) +" inches tall\n"
        dis += str(self.weight) +" pounds\n"
        dis += self.gender + "\n"
        dis += self.eyeColor + " eyes\n"
        dis += self.hairColor +" hair"

        return dis

