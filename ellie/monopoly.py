from random import randint

class Player:
    def __init__(self, player_name, player_token):
        self.name = player_name
        self.token = player_token
        self.money = 1500
        self.properties = []
        self.position = 0
        self.in_jail = False
        self.is_turn = False
    
    def __repr__(self):
        return f"This player, {self.name}, is playing as the {self.token}. \n{self.name} has ${self.money}, is currently on {board[self.position]}, and owns these properties: {self.properties}"

    def roll_dice(self):
        # Roll two dice and return the results
        die1 = randint(1,6)
        die2 = randint(1,6)
        result = die1 + die2
        print(f"{self.name} rolled a {result} with a {die1} and a {die2}!")
        return [die1, die2, result]
    
    def update_position(self):
        # Check the dice roll and update position on the board.
        result = self.roll_dice()
        while result[2] > 0:
            self.position += 1
            result[2] -= 1
            # Wrap around board
            if self.position >= 40:
                self.position = 0
                self.money += 200
                print(f"{self.name} passed Go and collects $200.")
        if result[0] != result[1]:
            self.is_turn = False
        return result
    
    def take_turn(self):
        self.is_turn = True
        turn_count = 0
        # Rolls dice and repeats if doubles are achieved, unless it's done three times in a row
        while self.is_turn or turn_count < 3:
            turn_count += 1
            self.update_position()
            if self.is_turn and turn_count < 3:
                print(f"{self.name} rolled doubles! {self.name} goes again!")
            elif turn_count >= 3:
                print(f"{self.name} rolled doubles three times in a row! {self.name} goes to jail!")
                self.position = 10
                self.in_jail = True


class Property:
    def __init__(self, property_name, property_cost, property_house_cost, property_rent0, property_rent1, property_rent2, property_rent3, property_rent4, property_rent5, property_mortgage):
        self.name = property_name
        self.cost = property_cost
        self.house_cost = property_house_cost
        self.houses = 0
        self.rent0 = property_rent0
        self.rent1 = property_rent1
        self.rent2 = property_rent2
        self.rent3 = property_rent3
        self.rent4 = property_rent4
        self.rent5 = property_rent5
        self.mortgage = property_mortgage
    
    def __repr__(self):
        return f"{self.name}: ${self.cost}. \nRent ${self.rent0}. \nWith 1 House: ${self.rent1}. \nWith 2 Houses: ${self.rent2}. \nWith 3 Houses: ${self.rent3}. \nWith 4 Houses: ${self.rent4}. \nWith Hotel: ${self.rent5}. \n\nMortgage Value: ${self.mortgage}. \nHouses cost ${self.house_cost} each. \nHotels, ${self.house_cost} plus 4 houses. \nIf a player owns ALL the lots in any Color-Group, the rent is Doubled on Unimproved Lots in that group."
    
    def buy_property(self, player):
        if player.money < self.cost:
            print(f"You don't have enough money to afford this property.")
            return
        else:
            player.properties.append(self)

    def buy_house(self, player):
        if player.money < self.house_cost:
            print(f"You don't have enough money to afford a house here.")
            return
        else:
            if self.houses < 5:
                self.houses += 1
            else:
                print(f"This property already has a hotel.")
        
    def charge_rent(self, owner, renter):
        if self.houses <= 0:
            owner.money += self.rent0
            renter.money -= self.rent0
            print(f"You landed on {self.name}. Rent with {self.houses} houses costs ${self.rent0}.")
            print(f"{renter.name} paid {owner.name} ${self.rent0}.")
        elif self.houses == 1:
            owner.money += self.rent1
            renter.money -= self.rent1
            print(f"You landed on {self.name}. Rent with {self.houses} houses costs ${self.rent1}.")
            print(f"{renter.name} paid {owner.name} ${self.rent1}.")
        elif self.houses == 2:
            owner.money += self.rent2
            renter.money -= self.rent2
            print(f"You landed on {self.name}. Rent with {self.houses} houses costs ${self.rent2}.")
            print(f"{renter.name} paid {owner.name} ${self.rent2}.")
        elif self.houses == 3:
            owner.money += self.rent3
            renter.money -= self.rent3
            print(f"You landed on {self.name}. Rent with {self.houses} houses costs ${self.rent3}.")
            print(f"{renter.name} paid {owner.name} ${self.rent3}.")
        elif self.houses == 4:
            owner.money += self.rent4
            renter.money -= self.rent4
            print(f"You landed on {self.name}. Rent with {self.houses} houses costs ${self.rent4}.")
            print(f"{renter.name} paid {owner.name} ${self.rent4}.")
        elif self.houses >= 5:
            owner.money += self.rent5
            renter.money -= self.rent5
            print(f"You landed on {self.name}. Rent with 1 hotel costs ${self.rent5}.")
            print(f"{renter.name} paid {owner.name} ${self.rent5}.")

mediterranean_ave = Property("Mediterranean Avenue", 60, 50, 2, 10, 30, 90, 160, 250, 30)
baltic_ave = Property("Baltic Avenue", 60, 50, 4, 20, 60, 180, 320, 450, 30)
oriental_ave = Property("Oriental Avenue", 100, 50, 6, 30, 90, 270, 400, 550, 50)
vermont_ave = Property("Vermont Avenue", 100, 50, 6, 30, 90, 270, 400, 550, 50)
connecticut_ave = Property("Connecticut Avenue", 120, 50, 8, 40, 100, 300, 450, 600, 60)
st_charles_place = Property("St. Charles Place", 140, 100, 10, 50, 150, 450, 625, 750, 70)
states_ave = Property("States Avenue", 140, 100, 10, 50, 150, 450, 625, 750, 70)
virginia_ave = Property("Virginia Avenue", 160, 100, 12, 60, 180, 500, 700, 900, 80)
st_james_place = Property("St. James Place", 180, 100, 14, 70, 200, 550, 750, 950, 90)
tennessee_ave = Property("Tennessee Avenue", 180, 100, 14, 70, 200, 550, 750, 950, 90)
new_york_ave = Property("New York Avenue", 200, 100, 16, 80, 220, 600, 800, 1000, 100)
kentucky_ave = Property("Kentucky Avenue", 220, 150, 18, 90, 250, 700, 875, 1050, 110)
indiana_ave = Property("Indiana Avenue", 220, 150, 18, 90, 250, 700, 875, 1050, 110)
illinois_ave = Property("Illinois Avenue", 240, 150, 20, 100, 300, 750, 925, 1100, 120)
atlantic_ave = Property("Atlantic Avenue", 260, 150, 22, 110, 330, 800, 975, 1150, 130)
ventnor_ave = Property("Ventnor Avenue", 260, 150, 22, 110, 330, 800, 975, 1150, 130)
marvin_gardens = Property("Marvin Gardens", 280, 150, 24, 120, 360, 850, 1025, 1200, 140)
pacific_ave = Property("Pacific Avenue", 300, 200, 26, 130, 390, 900, 1100, 1275, 150)
north_carolina_ave = Property("North Carolina Avenue", 300, 200, 26, 130, 390, 900, 1100, 1275, 150)
pennsylvania_ave = Property("Pennsylvania Avenue", 320, 200, 28, 150, 450, 1000, 1200, 1400, 160)
park_place = Property("Park Place", 350, 200, 35, 175, 500, 1100, 1300, 1500, 175)
boardwalk = Property("Boardwalk", 400, 200, 50, 200, 600, 1400, 1700, 2000, 200)

brown_group = [mediterranean_ave, baltic_ave]
light_blue_group = [oriental_ave, vermont_ave, connecticut_ave]
pink_group = [st_charles_place, states_ave, virginia_ave]
orange_group = [st_james_place, tennessee_ave, new_york_ave]
red_group = [kentucky_ave, indiana_ave, illinois_ave]
yellow_group = [atlantic_ave, ventnor_ave, marvin_gardens]
green_group = [pacific_ave, north_carolina_ave, pennsylvania_ave]
dark_blue_group = [park_place, boardwalk]

board = ["Go", mediterranean_ave, "Community Chest", baltic_ave, "Income Tax", "Reading Railroad", oriental_ave, "Chance", vermont_ave, connecticut_ave, "Jail", st_charles_place, "Electric Company", states_ave, virginia_ave, "Pennsylvania Railroad", st_james_place, "Community Chest", tennessee_ave, new_york_ave, "Free Parking", kentucky_ave, "Chance", indiana_ave, illinois_ave, "B. & O. Railroad", atlantic_ave, ventnor_ave, "Water Works", marvin_gardens, "Go To Jail", pacific_ave, north_carolina_ave, "Community Chest", pennsylvania_ave, "Short Line Railroad", "Chance", park_place, "Luxury Tax", boardwalk]

print(boardwalk)
