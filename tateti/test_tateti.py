import unittest

from tablero import Tablero, PosOcupadaException
from tateti import Tateti
from jugador import Jugador


class TestTablero(unittest.TestCase):
    
    def setUp(self):
        self.tablero = Tablero()
    
    def test_tablero_inicial_vacio(self):
        for fila in self.tablero.contenedor:
            for casilla in fila:
                self.assertEqual(casilla, "")
    
    def test_poner_ficha_en_posicion_vacia(self):
        self.tablero.poner_la_ficha(0, 0, "Jugador X")
        self.assertEqual(self.tablero.contenedor[0][0], "Jugador X")
    
    def test_excepcion_posicion_ocupada(self):
        self.tablero.poner_la_ficha(1, 1, "Jugador X")
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(1, 1, "Jugador O")
    
    def test_verificar_ganador_fila(self):
        for col in range(3):
            self.tablero.poner_la_ficha(0, col, "Jugador X")
        self.assertEqual(self.tablero.verificar_ganador(), "Jugador X")
    
    def test_verificar_ganador_diagonal(self):
        for i in range(3):
            self.tablero.poner_la_ficha(i, i, "Jugador O")
        self.assertEqual(self.tablero.verificar_ganador(), "Jugador O")


class TestTateti(unittest.TestCase):
    
    def setUp(self):
        self.juego = Tateti()
    
    def test_cambio_de_turno(self):
        self.assertEqual(self.juego.turno, "Jugador X")
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.turno, "Jugador O")
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.assertEqual(self.juego.turno, "Jugador X")
    
    def test_deteccion_fin_juego_por_victoria(self):
        self.juego.ocupar_una_de_las_casillas(0, 0) 
        self.juego.ocupar_una_de_las_casillas(1, 0)  
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.ocupar_una_de_las_casillas(0, 2)  
        
        self.assertTrue(self.juego.juego_terminado)
        self.assertEqual(self.juego.ganador, "Jugador X")
        self.assertEqual(self.juego.obtener_estado_juego(), "¡Jugador X ha ganado!")


class TestJugador(unittest.TestCase):
    
    def test_crear_jugador(self):
        jugador = Jugador("Usuario", "Jugador X")
        self.assertEqual(jugador.nombre, "Usuario")
        self.assertEqual(jugador.ficha, "X")
        self.assertEqual(jugador.victorias, 0)


if __name__ == '__main__':
    unittest.main()
