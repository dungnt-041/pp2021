class Salary:
    def __init__(self, id, name, office, working_hour, wage, total):
        self.id = id
        self.office = office
        self.working_hour = working_hour
        self.wage = wage
        self.total = total
        self.name = name
    
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
        print(self.office, end = "\t\t")
        print(self.working_hour, end = "h\t\t")
        print(self.wage, end = "$\t\t")
        print(self.total, end = "$\n")