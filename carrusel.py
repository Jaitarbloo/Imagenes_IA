import reflex as rx
from state import State

def carrusel_imagenes():
    return rx.box(
                    rx.image(src=State.imagenes[State.indice_actual],
                    width="800px", 
                    height="400px"),
            margin_top="8em"
                ) 