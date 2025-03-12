from model.Objects.Usuario import Usuario
from dbConnection.FirebaseConnection import FirebaseConnection

class UsuarioDAO:
    def __init__(self):
        self.firebase_connection = FirebaseConnection()  # Initialize connection
        if self.firebase_connection.db is not None:
            self.usuario_ref = self.firebase_connection.db.collection('usuarios')  # Set reference to the collection
        else:
            self.usuario_ref = None  # In case the connection could not be established

    def add_usuario(self, usuario):
        if self.usuario_ref is None:
            print("❌ Cannot connect to Firebase....")
            return

        try:
            if not isinstance(usuario, Usuario):
                raise ValueError("❌ The object is not an instance of Libro")
            self.usuario_ref.add(usuario.create_dictionary())  # Add to Firebase
        except Exception as e:
            print(f"❌ Error adding usuario: {e}")

    # Method to get all Nakamas
    def get_libros(self):
        if self.usuario_ref is None:
            print("❌ Cannot connect to Firebase.....")
            return []

        try:
            return [doc.create_dictionary() for doc in self.usuario_ref.stream()]
        except Exception as e:
            print(f"❌ Error retrieving libro from Firebase: {e}")
            return []







