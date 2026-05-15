import unittest

from mychar import cadena_mas_larga

class TestCadenaMasLarga(unittest.TestCase):

    def test_caso_enunciado(self):
        lista = ["a", "ab", "abc", "dddd", "abcd"]
        resultado = cadena_mas_larga(lista)
        self.assertEqual(resultado, "abcd")

    def test_mayusculas_minusculas(self):
        lista = ["SATURNO", "jupiter"] 
        self.assertEqual(cadena_mas_larga(lista), "jupiter")

    def test_tildes_y_enye(self):
        lista = ["Ágora", "Beodo", "Ñandú"]
        resultado = cadena_mas_larga(lista)
        self.assertEqual(resultado, "Ágora")  

    def test_palabras_repetidas(self):
        lista = ["sol", "tierra", "tierra", "luna"]
        self.assertEqual(cadena_mas_larga(lista), "tierra")

    def test_misma_longitud(self):
        lista = ["venus", "marte", "urano"]
        self.assertEqual(cadena_mas_larga(lista), "marte")

    def test_lista_vacia(self):
        self.assertEqual(cadena_mas_larga([]), "")

    def test_todo_vacio(self):
        lista = ["", "", ""]
        self.assertEqual(cadena_mas_larga(lista), "")

    def test_mezcla_vacias_y_validas(self):
        lista = ["", "", "mercurio", ""]
        self.assertEqual(cadena_mas_larga(lista), "mercurio")

if __name__ == '__main__':
    unittest.main()

