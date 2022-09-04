def getReq():
    return "Você fez um get"


def postReq():
    return "Você fez um post"


formato = {
    "id": "12345",
    "image": "path",
    "info": {
        "nome": "Donatello",
        "espécie": "Ninja",
        "curiosidades": "..."
    }
}

# dados = [formato]


class Turtle:

    # default constructor
    def __init__(self):
        self.id = ""
        self.image = ""
        self.nome = ""
        self.info = {
            "especie": "",
            "curiosidades": ""
        }

    # a method for printing data members
    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def set_image(self, image):
        self.image = image

    def set_info(self, info):
        self.info = info

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_image(self):
        return self.image

    def get_info(self):
        return self.info

# creating object of the class
turtle = Turtle()
print(turtle.get_nome())
turtle.set_nome("Donatello")
# calling the instance method using the object obj
print(turtle.get_nome())
