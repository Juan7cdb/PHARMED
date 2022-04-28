class Account:
    id = int
    name = str
    lastname = str
    email = str
    password = str
    university = str
    carrer = str
    semester = int
    
    def __init__(self, id, name, lastname, email, password, university, carrer, semester):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.university = university
        self.carrer = carrer
        self.semester = semester