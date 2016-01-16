class Item(object):

    def __init__(self, itemCode, item, price, itemsLeft):
        """Creates an Item object, initializing its methods.
        input:
            1. itemCode - string - unique code identifying the product
            2. item - string - the name of the product
            3. price - float - the unit price of the product
            4. itemsLeft - int - discrete number values for the number of the product
               available in the store

        """

        # Initialize class variables from parameters
        self.itemCode = itemCode
        self.item = item
        self.price = price
        self.itemsLeft = itemsLeft

    def __str__(self):
        """Defines the default string of an object under this class.
        returns:
            1. string - the formatted string detailing product information

        """

        return "{0} {1} ${2:.2f} {3}x".format(self.itemCode,self.item,round(self.price,2),self.itemsLeft)

    # ----- Class Methods -----
    def checkInventory(self):
        """Checks how many of the product is left in the store.
        returns:
            1. itemsLeft - int - discrete number values for the number of the product
               available in the store

        """

        return self.itemsLeft

    def updateInventory(self,amount):
        """Changes the number of the product available in the store.
        input:
            1. amount - int - either 1 or -1, changes itemLeft by that amount

        """

        self.itemsLeft += amount

class Food(Item):

    def __init__(self, itemCode, item, price, itemsLeft, unit):
        """Creates a Food object, child of Item, initializing Item methods along with a unique
           string and extra parameters.
        input:
            1. itemCode - string - unique code identifying the product
            2. item - string - the name of the product
            3. price - float - the unit price of the product
            4. itemsLeft - int - discrete number values for the number of the product
               available in the store
            5. groupCode - string - specialized code without first two letters
            6. qualifier - string - the amount each food comes in

        """

        # Initialize extra class variables
        Item.__init__(self,itemCode,item,price,itemsLeft)
        self.groupCode = itemCode[2::]
        self.qualifier = unit

    def __str__(self):
        """Defines the default string of an object under this class.
        returns:
            1. string - the formatted string detailing product information

        """

        return "{0} {1} {2} ${3:.2f} {4}x".format(self.groupCode,self.item,self.qualifier,round(self.price,2),self.itemsLeft)

class Technology(Item):

    def __init__(self, itemCode, item, price, itemsLeft, specs):
        """Creates a Technology object, child of Item, initializing Item methods along with a unique
           string and extra parameters.
        input:
            1. itemCode - string - unique code identifying the product
            2. item - string - the name of the product
            3. price - float - the unit price of the product
            4. itemsLeft - int - discrete number values for the number of the product
               available in the store
            5. groupCode - string - specialized code without first two letters
            6. qualifier - string - the specifications of the technology item

        """

        # Initialize extra class variables
        Item.__init__(self,itemCode,item,price,itemsLeft)
        self.groupCode = itemCode[2::]
        self.qualifier = specs

    def __str__(self):
        """Defines the default string of an object under this class.
        returns:
            1. string - the formatted string detailing product information

        """

        return "{0} {1} {2} ${3:.2f} {4}x".format(self.groupCode,self.item,self.qualifier,round(self.price,2),self.itemsLeft)

class Medicine(Item):

    def __init__(self, itemCode, item, price, itemsLeft, quantity):
        """Creates a Medicine object, child of Item, initializing Item methods along with a unique
           string and extra parameters.
        input:
            1. itemCode - string - unique code identifying the product
            2. item - string - the name of the product
            3. price - float - the unit price of the product
            4. itemsLeft - int - discrete number values for the number of the product
               available in the store
            5. groupCode - string - specialized code without first two letters
            6. qualifier - string - the quantity each medicine item comes in

        """

        # Initialize extra class variables
        Item.__init__(self,itemCode,item,price,itemsLeft)
        self.groupCode = itemCode[2::]
        self.qualifier = quantity

    def __str__(self):
        """Defines the default string of an object under this class.
        returns:
            1. string - the formatted string detailing product information

        """

        return "{0} {1} {2} ${3:.2f} {4}x".format(self.groupCode,self.item,self.qualifier,round(self.price,2),self.itemsLeft)

class Clothing(Item):

    def __init__(self, itemCode, item, price, itemsLeft, size_color):
        """Creates a Clothing object, child of Item, initializing Item methods along with a unique
           string and extra parameters.
        input:
            1. itemCode - string - unique code identifying the product
            2. item - string - the name of the product
            3. price - float - the unit price of the product
            4. itemsLeft - int - discrete number values for the number of the product
               available in the store
            5. groupCode - string - specialized code without first two letters
            6. qualifier - string - the size or colour of the clothing item

        """

        # Initialize extra class variables
        Item.__init__(self,itemCode,item,price,itemsLeft)
        self.groupCode = itemCode[2::]
        self.qualifier = size_color

    def __str__(self):
        """Defines the default string of an object under this class.
        returns:
            1. string - the formatted string detailing product information

        """

        return "{0} {1} {2} ${3:.2f} {4}x".format(self.groupCode,self.item,self.qualifier,round(self.price,2),self.itemsLeft)

class Music(Item):

    def __init__(self, itemCode, item, price, itemsLeft, artist):
        """Creates a Music object, child of Item, initializing Item methods along with a unique
           string and extra parameters.
        input:
            1. itemCode - string - unique code identifying the product
            2. item - string - the name of the product
            3. price - float - the unit price of the product
            4. itemsLeft - int - discrete number values for the number of the product
               available in the store
            5. groupCode - string - specialized code without first two letters
            6. qualifier - string - the artist of the CD

        """

        # Initialize extra class variables
        Item.__init__(self,itemCode,item,price,itemsLeft)
        self.groupCode = itemCode[2::]
        self.qualifier = artist

    def __str__(self):
        """Defines the default string of an object under this class.
        returns:
            1. string - the formatted string detailing product information

        """

        return "{0} {1} by {2} ${3:.2f} {4}x".format(self.groupCode,self.item,self.qualifier,round(self.price,2),self.itemsLeft)

class Inventory(object):

    def __init__(self, items_file):
        """Creates an Inventory object, creating a general list of all products.
        input:
            1. items_file - string - the string name of the text file that hold all information
        returns:
            1. itemList - object list - list of all products described in the text file
               as objects

        """

        # Initialize extra class variables
        self.items_file = items_file
        # Create the list of products
        self.itemList = self.create_itemList()

    def create_itemList(self):
        """Creates a list of all products as objects.
        returns:
            1. items - object list - list of all products described in the text file
               as objects

        """

        # Open file for reading
        file = open(self.items_file,"r")
        # Split each line of text file as a string into a list
        fileList = file.readlines()
        file.close()
        # Initialize list of products
        items = []

        # Add all products from the file to the list
        for i in range(1, len(fileList)):
            item_data = fileList[i].split(',')
            item_data[4] = item_data[4][:-1]
            item = Item(item_data[0],item_data[1],float(item_data[3]),int(item_data[4]))
            items.append(item)

        return items

class FoodInventory(Inventory):

    def __init__(self, items_file):
        """Creates a FoodInventory object, creating a list of specific food products.
        input:
            1. items_file - string - the string name of the text file that hold all information
        returns:
            1. foodList - object list - list of food products described in the text file
               as objects

        """

        # Initialize parent class
        Inventory.__init__(self,items_file)
        # Create the list of food
        self.foodList = self.create_foodList()

    def create_foodList(self):
        """Creates a list of food products as objects.
        returns:
            1. foodList - object list - list of food products described in the text file
               as objects

        """

        # Open file for reading
        file = open(self.items_file,"r")
        # Split each line of text file as a string into a list
        fileList = file.readlines()
        file.close()
        # Initialize list of food
        foodList = []

        # Add food from the file to the list
        for i in range(1, len(fileList)):
            if fileList[i][0:2] == "Fd":
                food_data = fileList[i].split(',')
                food_data[4] = food_data[4][:-1]
                food = Food(food_data[0],food_data[1],float(food_data[3]),int(food_data[4]),food_data[2])
                foodList.append(food)

        return foodList

class TechInventory(Inventory):

    def __init__(self, items_file):
        """Creates a TechInventory object, creating a list of specific technology products.
        input:
            1. items_file - string - the string name of the text file that hold all information
        returns:
            1. techList - object list - list of technology products described in the text file
               as objects

        """

        # Initialize parent class
        Inventory.__init__(self,items_file)
        # Create the list of technology
        self.techList = self.create_techList()

    def create_techList(self):
        """Creates a list of technology products as objects.
        returns:
            1. techList - object list - list of technology products described in the text file
               as objects

        """

        # Open file for reading
        file = open(self.items_file,"r")
        # Split each line of text file as a string into a list
        fileList = file.readlines()
        file.close()
        # Initialize list of technology
        techList = []

        # Add technology from the file to the list
        for i in range(1, len(fileList)):
            if fileList[i][0:2] == "Tc":
                tech_data = fileList[i].split(',')
                tech_data[4] = tech_data[4][:-1]
                tech = Technology(tech_data[0],tech_data[1],float(tech_data[3]),int(tech_data[4]),tech_data[2])
                techList.append(tech)

        return techList

class MedicineInventory(Inventory):

    def __init__(self, items_file):
        """Creates a MedicineInventory object, creating a list of specific medicinal products.
        input:
            1. items_file - string - the string name of the text file that hold all information
        returns:
            1. medList - object list - list of medicinal products described in the text file
               as objects

        """

        # Initialize parent class
        Inventory.__init__(self,items_file)
        # Create the list of medicine
        self.medList = self.create_medList()

    def create_medList(self):
        """Creates a list of medicinal products as objects.
        returns:
            1. medList - object list - list of medicinal products described in the text file
               as objects

        """

        # Open file for reading
        file = open(self.items_file,"r")
        # Split each line of text file as a string into a list
        fileList = file.readlines()
        file.close()
        # Initialize list of technology
        medList = []

        # Add medicine from the file to the list
        for i in range(1, len(fileList)):
            if fileList[i][0:2] == "Md":
                med_data = fileList[i].split(',')
                med_data[4] = med_data[4][:-1]
                med = Medicine(med_data[0],med_data[1],float(med_data[3]),int(med_data[4]),med_data[2])
                medList.append(med)

        return medList

class ClothingInventory(Inventory):

    def __init__(self, items_file):
        """Creates a ClothingInventory object, creating a list of specific clothing products.
        input:
            1. items_file - string - the string name of the text file that hold all information
        returns:
            1. clothingList - object list - list of clothing products described in the text file
               as objects

        """

        # Initialize parent class
        Inventory.__init__(self,items_file)
        # Create the list of clothing
        self.clothingList = self.create_clothingList()

    def create_clothingList(self):
        """Creates a list of clothing products as objects.
        returns:
            1. medList - object list - list of clothing products described in the text file
               as objects

        """

        # Open file for reading
        file = open(self.items_file,"r")
        # Split each line of text file as a string into a list
        fileList = file.readlines()
        file.close()
        # Initialize list of clothing
        clothingList = []

        # Add clothing from the file to the list
        for i in range(1, len(fileList)):
            if fileList[i][0:2] == "Cl":
                clothing_data = fileList[i].split(',')
                clothing_data[4] = clothing_data[4][:-1]
                clothing = Clothing(clothing_data[0],clothing_data[1],float(clothing_data[3]),int(clothing_data[4]),clothing_data[2])
                clothingList.append(clothing)

        return clothingList

class MusicInventory(Inventory):

    def __init__(self, items_file):
        """Creates a MusicInventory object, creating a list of specific music/CD products.
        input:
            1. items_file - string - the string name of the text file that hold all information
        returns:
            1. musicgList - object list - list of music/CD products described in the text file
               as objects

        """

        # Initialize parent class
        Inventory.__init__(self,items_file)
        # Create the list of music
        self.musicList = self.create_musicList()

    def create_musicList(self):
        """Creates a list of music/CD products as objects.
        returns:
            1. musicList - object list - list of music/CD products described in the text file
               as objects

        """

        # Open file for reading
        file = open(self.items_file,"r")
        # Split each line of text file as a string into a list
        fileList = file.readlines()
        file.close()
        # Initialize list of music
        musicList = []

        # Add music from the file to the list
        for i in range(1, len(fileList)):
            if fileList[i][0:2] == "CD":
                cd_data = fileList[i].split(',')
                cd_data[4] = cd_data[4][:-1]
                music = Music(cd_data[0],cd_data[1],float(cd_data[3]),int(cd_data[4]),cd_data[2])
                musicList.append(music)

        return musicList

