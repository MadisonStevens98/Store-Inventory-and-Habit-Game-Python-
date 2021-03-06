  
import math
import pickle

class dailytasks:

    def __init__(
        self,
        name,
        reward,
        penalty,
        ):

        self.name = name
        self.reward = reward
        self.penalty = penalty
        self.complete = False

    def markdone(self, money, level):
        self.complete = True
        level += self.reward
        print('Congrats! You earned ' + str(self.reward) \
            + ' dollars, and gained ' + str(self.reward) + 'levels!')
        return level

    def setmoney(self, money):
        money += self.reward
        return money

    def penalty(self, HP):
        HP -= self.penalty
        return 'You took damage!'

    def display(self):
        if self.complete == False:
            return self.name + '\nReward: ' + str(self.reward) \
                + '\nPenalty: ' + str(self.penalty) \
                + '''
Not completed
'''
        else:
            return self.name + '\nReward: ' + str(self.reward) \
                + '\nPenalty: ' + str(self.penalty) \
                + '''
Completed!
'''


class store:

    def display():
        print(potio.display())

    def buy(item, amount, money):
        spent = item.price * amount
        if money >= int(spent):
            item.owned += amount
            money -= spent
            print('Items added to Inventory. Back to Main!\n')
            return money
        else:
            print("You don't have enough money!\n")
            return money


class tasks:

    def __init__(self, lists):

        self.lists = lists

    def display(self):
        for x in range(len(self.lists)):
            y = self.lists[x]
            print(str(x + 1) + '. ' + y.display())


class inventory:

    def __init__(self, lists):

        self.lists = lists

    def display(self):
        for x in range(len(self.lists)):
            y = self.lists[x]
            print(str(x + 1) + '. ' + y.display())

class item:

    def __init__(
        self,
        name,
        desc,
        price,
        owned,
        ):

        self.name = name
        self.desc = desc  # String description of item
        self.price = price  # price of item in the store
        self.owned = owned  # number of that item the player owns

    def add(self, amount):  # used to add items to play inventory
        self.owned += amount  # adding item to inventory count for that item


class potion(item):

    def use(self, HP):
        if self.owned == 0:
            print("You don't have any of that item! \n")
            return HP
        else:
            HP += 5
            self.owned -= 1
            print('You use a potion and healed 5 pts!\n')
            return HP

    def display(self):
        return(self.name + '\nDescription: ' + self.desc + '\nPrice: ' \
            + str(self.price) + '\nTotal: ' + str(self.owned))

dailytask1 = dailytasks('Drink 2 bottles of water!', 2, 2)
potio = potion('Potion', 'Heals 5 pts of health', 5, 1)

tasklist = []
tasklist.append(dailytask1)

# dailylist = tasks(tasklist)

inventorylist = []
inventorylist.append(potio)

# inventor = inventory(inventorylist)

def main():

    tasktxt = open('Task.txt', 'rb')
    dailylist = pickle.load(tasktxt)
    tasktxt.close()

    invtxt = open('Inventory.txt', 'rb')
    inventor = pickle.load(invtxt)
    invtxt.close()

    Level = open('Level.txt', 'r')
    hp = open('HP.txt', 'r')
    Money = open('Money.txt', 'r')

    Level.close
    hp.close
    Money.close

    level = int(Level.read())
    HP = int(hp.read())
    money = int(Money.read())

    exitprogram = False

    while exitprogram != True:

        print('Your level is ' + str(level) + '\nYour health is ' \
            + str(HP) + '\nYou have $' + str(money) + '\n' + '\n' \
            + 'Dailies: ')

        print(dailylist.display())

        userinput = input('''What would you like to do? Type I to check inventory, S to go to
the store, C to create new daily task, or D to mark a daily as done.
Type E to save your progress and exit. \n 
''')

        if userinput == 'I' or userinput == 'i':
            inventor.display()
            useri = \
                input('Type the number of the item you want to use, or type anything else to go back to Main!'
                      )
            if useri == '1':
                HP = potio.use(HP)
                inventor = inventory(inventorylist)
                print('Back to Main! \n')
            else:
                print('Back to Main! \n')
        elif userinput == 'C' or userinput == 'c':

            dname = str(input('Enter name of task (ie drink water): \n'))
            dreward = int(input('Enter reward amount (INT), do a higher reward for the harder tasks: \n')) 
            dpenalty = int(input('Enter the penalty amount (INT), make it higher the easier the task: \n'))
            temp = dailytasks(dname, dreward, dpenalty)
            tasklist.append(temp)
            dailylist = tasks(tasklist)
            print('Added to your task! Back to Main! \n')
            
        elif userinput == 'E' or userinput == 'e':
            
            tasktxt = open('Task.txt', 'wb')
            pickle.dump(dailylist, tasktxt)
            tasktxt.close()
            inventorytxt = open('Inventory.txt', 'wb')
            pickle.dump(inventor, inventorytxt)
            inventorytxt.close()
            Levelw = open('Level.txt', 'w')
            Levelw.write(str(level))
            Levelw.close()
            hpw = open('HP.txt', 'w')
            hpw.write(str(HP))
            hpw.close()
            moneyw = open('Money.txt', 'w')
            moneyw.write(str(money))
            moneyw.close()
            exit()
            
        elif userinput == 'S' or userinput == 's':

            store.display()
            useri = input('Type B to Buy or anything else to return to Main!\n')
            
            if useri == 'B' or useri == 'b':
                useri = int(input('How many do you want to buy?'))
                money = store.buy(potio, useri, money)
                inventor = inventory(inventorylist)
            else:
                print('Back to Main!\n')
        elif userinput == 'D' or userinput == 'd':

            print(dailytask1.display())
            if dailytask1.complete == True:
                print('All tasks done! Back to Main! \n')
            else:
                useri = input('Would you like to mark this task as done? Type Yes or anything else to be sent back to Main! \n')
                if useri == 'Yes' or useri == 'yes':
                    level = dailytask1.markdone(money, level)
                    money = dailytask1.setmoney(money)
                    print('Marked done! Back to Main! \n')
                else:
                    print('Invalid Input! Back to Main! \n')
                    continue
        else:
            print('Invalid input try again! It should be I, S, D or E to exit. \n')

if __name__ == '__main__':
    main()
