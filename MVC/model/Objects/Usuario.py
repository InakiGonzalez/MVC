class Usuario:
    def __init__(self, iD, nombre, email):
        self.__iD = iD
        self.__nombre = nombre
        self.__email = email
    
    def get_iD(self):
        return self.__iD
    
    def get_nombre(self):
        return self.__nombre
    
    def get_email(self):
        return self.__email
    
    def set_iD(self, iD):
        return self.__iD
    
    def set_nombre(self, nombre):
        return self.__nombre
    
    def set_email(self, email):
        return self.__email
    
    def create_dictionary(self):
        return {
            "iD": self.__iD,
            "nombre": self.__nombre,
            "email": self.__email
        }