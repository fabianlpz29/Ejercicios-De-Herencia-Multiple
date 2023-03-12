from Tipo import Tipo 
from Tipo import tipoCategoria

class Peliculas(Tipo):
    pass

    def __init__(self,peliculaAccion, peliculaComedia,PeliculaTerror):
        self.peliculaAccion = peliculaAccion #nombre de la poelicula de accion
        self.peliculaComedia = peliculaComedia #nombre de la pelicula de comedia
        self.PeliculaTerror = PeliculaTerror #nombre de  la pelicula de terror

    def CategoriaAccion(self):
        return 'La pelicula {} es de categoria {}'.format(self.peliculaAccion,tipoCategoria.cateegoriaA)
    
    def CategoriaComedia(self):
        return 'La pelicula {} es de categoria {}'.format(self.peliculaComedia,tipoCategoria.cateegoriaC)
    
    def CategoriaTerror(self):
        return 'La pelicula {} es de categoria {}'.format(self.PeliculaTerror,tipoCategoria.cateegoriaT)
    
tipoPelicula = Peliculas("Baby Driver","Los 3 chiflados", "It")