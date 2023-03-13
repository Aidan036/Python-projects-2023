import aidan
import person

aidan = person.Person("Aidan",True,True,False,"Hazel","M",70,120,17,"a+","dirtyBlonde","Caucasian")
kaine = person.Person("Kaine",True,False,False,"brown","M",72,145,16,"o+","Rainbow","yes")
landon = person.Person("Landon")
landon.speak("Hi My name is"+landon.name)
landon.die()
print(landon.isAlive)

print(aidan)
print(kaine)
print(landon)