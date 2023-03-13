from asciiArt import *
from settings import *

weather = "Cold"
Health = "Good"
HP = "100"
pace = "Steady"
Rations = "Filling"
day = 1
month = 3
year = 1897

def clearScreen():
    #clears the screen
    print(" "*10000)

    def getNumberInRange(question, min, max):
        while True:
            x = input(question)
            try:
                x = int(x)
            except:
                print("not a number")
                continue
            if x >= min and x <= max:
                return x
            else:
                print("not in Range")

def displayMenu(options,question):
    print(RIBBON)
    print(question)
    for i in range(len(options)):
        print(str.format("\t({0}) -------------------  {1:<30}",i+1,options[i]))
    print(RIBBON)
    while True:
        choice = input("What would you like to do: ")
        if choice.isnumeric():
            choice = int(choice)
            if choice <= len(options) and choice > 0:
                return choice
            else:
                print("not in the correct range")
        else:
            print("You need to enter a number between 1 and "+str(len(options))),



def showTitle():
    print(GAME_TITLE)


def quitGame():
    clearScreen()
    choice = displayMenu(["Yes,No"],"Are you sure you want to quit?")
    if choice == 1:
        print("Good Bye")
        input("Press Enter to Continue")
        quit()
    else:
        return







# Continue on the trail
# Check supplies
def checkInventory():
    print("Inventory")
    return
#Change pace
def changePace(pace):
    print("What Pace would you like to set")
    choice = displayMenu(["A fast Pace", "A normal pace", "A slow pace"], "Choose pace:")
    if choice == 1:
        pace = 1.5
    elif choice == 2:
        pace = 1
    elif choice == 3:
        pace = 0.5

        return pace
# select food rations
def rations(rations):
    print("What will your daily rations be")
    choice = displayMenu(["filling", "Meager", "bare bones"], "They may be")
    if choice == 1:
        rations = 1.5
    elif choice == 2:
        rations = 1
    elif choice == 3:
        rations = 0.5

    return rations

# stop to rest

# attempt to trade
# talk to people

def mainGameloop():
    while True:
        print(str.format("""
                   .....                                        ..'..                              ..',,,'..
                ..',;;;,,'...  ...                       ..'''',,;;;;,..                       ..',;;;;;;;;,,,'..
                ,;;,;;;;;,;;;,,,;,,...               ..',;;;;;,,;;;;;;;;,'..     ..''....',,'',,;;;;;;;;;;,;;;;;,'..
                ;;;;;;;;;;;;;;;;;;;;;,,....'..   ..',;;;;;;;;;;;;;;;;;;;;;;,'..',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
                ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,',,;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
                ''''''''''''''',,,''''.........'''''',,,''''''''''''',,;;;;;,,,,,,,,,,,,;;;;;;;;;;;;,,,''...'',,,;;;
                                                                      ........        ...............            ...
                 +-----------------------------+
                 |Date:{:_>24}|
                 |Weather:{:_>21}|           ..'''''''''''..                         ..''''''.
                 |Health:{:_>22}|          ,:ccccllllllllc::::,...  ......  ..,::::::clclllcc,.
                 |Miles Travled:{:_>15}|         .cc'.;cccclccccccccclc'.;cllllc;.'ccccccccccccclcl;.
                 |Miles To Go:{:_>17}|          .;c, .,:clcclclcclcclc'.clcccclc.'cccccccccccclll:.
                 |Food:{:_>24}|           .cc.  .';cccclcclcclc'.clcccclc.'cccccccccccccc:.
                 +-----------------------------+            ,:;.   'ccccccclcclc'.clcccclc.'cccccccccccccc'
                                 ..                         .;c;.   ,ccclccccllc'.clcccllc.'cccccclccllcc,
                          .,,. .'::.  ....                   .:c.   .clcccccclcc'.cccccclc.'cccccccccccc'
                           .,:::cl,..',';c;:;;;;:;;;'.        ',.   .:cccccccccc..:cccccc:.'ccccccccccc:.
                         .';clcccl,';;::ccccccccccccc:.       ....  ......,,,,'.  .............',,,,..','.
                          ...';:;,,;cccllcclcclccccccc........'.''.',...',.,;',,. .,','',,,  .,'';,','.''.
                                .;:clcclcccclllccccc:,.      ...',... .,'. ', .';. ..,',,.. .;. .,. .,,.
                                 .'clcccc::;'.,:lclc.         ..''    ';...;;...;'   ''''   ,;..';,..';.
                                  .cc,:c;..  .,cc,:c.                 .,'. ', .',.          .;. .,. .,,.
                                .':c,..;l'   .';:;:c.                  .',',;','.            .,,';,',.
                '..''.''''.'''.',:c:,'';:,''''',::::,'''''...'''''''''''',;;;;,''''''''''..'''';;;;;,'''.''''''''''.
                ;;;;;;;;;;;;;;,;;:::;;;::;,,;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;;
                ;;;;;;;;;;;;;;,;::::;;;:;;;;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;,;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,
                ;;;;;;;;;;;;;;;;;:::;;;::;;;;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;
                """, date, weather, health, miles_traveled, total_miles, food))

        choice = displayMenu(["Continue on the trail", "Check supplies", "Change Pace", "Change Food Rations",
                              "Stop to rest", "Attempt to trade"], "You may")
        if choice == 1:
            pass
        elif choice == 2:
            checkInventory()
            return
        elif choice == 3:
            changePace(pace)
            return pace
        elif choice == 4:
            rations(rations)
            return rations
        elif choice == 5:
            pass
        elif choice == 6:
            pass

def game():
    mainGameloop()


# #Game Code goes here
# showTitle()
# choice = displayMenu(["Travel the oregon trail", "Learn about the trail", "See the Oregon Top Ten","Turn off sound", "Choose Management Options" ,"End"], "You may:")
# if choice == 1:
#     print("character select")
# elif choice == 2:
#     print("""Try taking a journey by covered wagon across 2000 miles of plains, rivers, and mountains.
#             Try!
#             On the plains, will you slosh your oxen through mud and water filled ruts or will you plod through dust six inches deep?
#
#             How will you cross the rivers? If you have money , you might take a ferry (if there is a ferry).
#             Or, you can ford the river and hope you and your wagon aren't swallowed alive!
#
#             At the Dalles,  you can try navigating the Columbia River, but if running the rapids with a makeshift raft makes you queasy, better take the Barlow Road.
#
#             We totally made this all by our selves and totally didn't steal this from the original Oregon trail and remade it in python
#             Karol Runge, Aiden Pearce""")
#     input("Press enter to continue")
#     game()
# elif choice == 3:
#     print("There is no leaderboard we lied")
#     input("Press enter to continue")
#     game()
#
# elif choice == 4:
#     print("This is a program built by two high schoolers your asking for too much")
#     input("Press enter to continue")
#     game()
# elif choice == 5:
#     print("no")
#     input("Press enter to continue")
#     game()
# elif choice == 6:
#     print("Thanks for Playing")


