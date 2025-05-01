import reflex as rx
from state import State

def imagenes_comunidad_madrid():

        return rx.flex(
                   rx.box(
                        rx.heading( "Bienvenidos a",size="8", margin="20px", color="black"),
                        rx.heading( "Comunidad.Madrid",size="9", margin="20px",color="red"),
                        rx.text("¿Qué estás buscando?",size="5", margin="20px", color="black"),
                        rx.box(
                                rx.input(placeholder="Search here...",  color="white", margin="10px"),
                                rx.button("Decrement",color_scheme="red"),
                        width="60%",margin="2%", background_color="black"
                               ),
                        width="100%",
                        background_color="white"),
                   rx.image("/coche.jpg",width="50%")) 