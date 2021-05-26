class Staff:
    def __init__(self, id, name, gender, DoB, office, password):
        self.id = id
        self.name = name
        self.gender = gender
        self.DoB = DoB
        self.office =office
        self.password = password
    
    def adjust_printing_name(self):
        self.name = self.name.strip()
        if len(self.name) < 8:
            print(self.name, end = "\t\t\t\t")
        elif len(self.name) > 7 and len(self.name) < 16:
            print(self.name, end = "\t\t\t")
        elif len(self.name) > 15 and len(self.name) < 25:
            print(self.name, end = "\t\t")
        else:
            print(self.name, end = "\t")
    
    def display(self):
        print(self.id, end = "\t\t")
        self.adjust_printing_name()
        print(self.gender, end = "\t\t")
        print(self.DoB, end = "\t")
        print(self.office, end ="\t\t")
        print(self.password)
    
    def display2(self):
        print()
        print("Your Information")
        print("ID : \t\t" + self.id)
        print("Name : \t\t" + self.name)
        print("Gender : \t" + self.gender)
        print("DoB : \t\t" + self.DoB)
        print("Office : \t" + self.office)
        print("Password : \t" + self.password)