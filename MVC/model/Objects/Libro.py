class Libro:
    def __init__(self, titulo, autor, genero, disponible):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__disponible = disponible

    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autpr
    
    def get_genero(self):
        return self.__genero
    
    def get_disponible(self):
        return self.__disponible
    
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def set_autor(self, autor):
        self.__autor = autor
    
    def set_genero(self, genero):
        self.__genero = genero
    
    def set_disponible(self, disponible):
        self.__disponible = disponible

    def create_dictionary(self):
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "genero": self.__genero,
            "disponible": self.__disponible
        }