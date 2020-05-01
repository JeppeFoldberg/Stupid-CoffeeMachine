class CoffeeMachine:
    def __init__(self, money, water, milk, coffee_beans, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.action = "choose action"

    def input(self):
        while self.action != "exit":
            self.action = input("\nWrite action (buy, fill, take, remaining, exit): ")
            if self.action == "buy":
                self.buy()
            elif self.action == "fill":
                self.fill()
            elif self.action == "take":
                print("I gave you $" + str(self.money))
                self.money = 0
            elif self.action == "remaining":
                self.status()
            elif self.action == "exit":
                break
            else:
                print("\n I did not understand that. Please try again!")



    def buy(self):
        purchase = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        if purchase == "1":
            if self.water < 250:
                missing = "water"
                print("Sorry, not enough " + missing)
            elif self.coffee_beans < 16:
                missing = "coffee beans"
                print("Sorry, not enough " + missing)
            elif self.cups < 1:
                missing = "cups"
                print("Sorry, not enough " + missing)
                self.status()
            else:
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
                print("i have enough resources, making you a coffee")
        if purchase == "2":
            if self.water < 350:
                missing = "water"
                print("Sorry, not enough " + missing)
            elif self.milk < 75:
                missing = "milk"
                print("Sorry, not enough " + missing)
            elif self.coffee_beans < 20:
                missing = "coffee beans"
                print("Sorry, not enough " + missing)
            elif self.cups < 1:
                missing = "cups"
                print("Sorry, not enough " + missing)
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
                print("i have enough resources, making you a coffee")
        if purchase == "3":
            if self.water < 200:
                missing = "water"
                print("Sorry, not enough " + missing)
            elif self.milk < 100:
                missing = "milk"
                print("Sorry, not enough " + missing)
            elif self.coffee_beans < 12:
                missing = "coffee beans"
                print("Sorry, not enough " + missing)
            elif self.cups < 1:
                missing = "cups"
                print("Sorry, not enough " + missing)
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
                print("i have enough resources, making you a coffee")

    def fill(self):
        self.water += int(input("\nWrite how many ml of water you want to add: "))
        self.milk += int(input("Write how many ml of milk you want to add: "))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))

    def status(self):
        print("\nThe coffee machine has: \n" + str(self.water) + " of water \n" + str(self.milk) + " of milk \n"
          + str(self.coffee_beans) + " of coffeebeans \n" + str(self.cups) + " of disposable cups \n" + str(self.money) + " of money")


machine = CoffeeMachine(550, 400, 540, 120, 9)
machine.input()

# if __name__ == "__main__":
   # main()