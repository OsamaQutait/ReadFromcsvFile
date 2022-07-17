class Employee:
    def __init__(self, ID, name, salary, address, department, email, phone):
        self.ID = ID
        self.name = name
        self.salary = salary
        self.address = address
        self.department = department
        self.email = email
        self.phone = phone

    def getID(self):
        return self.ID
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    def getAddress(self):
        return self.address
    def getDepartment(self):
        return self.department
    def getEmail(self):
        return self.email
    def getPhone(self):
        return self.phone
