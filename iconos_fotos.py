import reflex as rx
from state import State

def iconos_dentro_fotos():
        
        return rx.box(
                        rx.image("/arbol.jpg", width="100%", height="100%"),
                        rx.link(
                                rx.icon("clipboard-plus", 
                                        size=50,
                                        position="absolute",
                                        top="75%",
                                        left="25%",
                                        transform="translate(-50%, -50%)",
                                        color="orange",
                                        underline="always"
                                        
                                        ),
                               href="https://reflex.dev/"),

                        rx.link(
                                rx.icon("church", 
                                        size=50,
                                        position="absolute",
                                        top="75%",
                                        left="50%",
                                        transform="translate(-50%, -50%)",
                                        color="cyan"
                                        ),
                               href="https://reflex.dev/"),
                
                position="relative",
                width="100%",
                height="400px"
                        ) 