class Manager:
    def __init__(self, id, name, gender, DoB, password):
        self.id = id
        self.name = name
        self.gender = gender
        self.DoB = DoB
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
        print()
        print("Your Information")
        print("ID : \t\t" + self.id)
        print("Name : \t\t" + self.name)
        print("Gender : \t" + self.gender)
        print("DoB : \t\t" + self.DoB)
        print("Password : \t" + self.password)