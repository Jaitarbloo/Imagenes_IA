import reflex as rx
from state import State

def Fotos_giradas_con_link(): 
    return rx.center(
                    rx.link(
                        rx.box(
                              rx.image("/concorde 2.jpg"),
                              transform="rotate(25deg)",
                              width=rx.cond(
                                        State.expandida,
                                        "400px",
                                        "200px",
                                            ),
                              height=rx.cond(
                                        State.expandida,
                                        "400px",
                                        "200px",
                                             ),
                              background_color="blue") ,
                              cursor="pointer",
                              on_click=State.cambiar_tamano,
                              transition="all 0.3s ease-in-out",
                    ),

                    rx.link(
                        rx.box(
                             "Contenido del Box",
                              transform="rotate(45deg)",
                              width="200px",
                              height="200px",
                              background_color="white") , 
                    
                    
                    href="https://reflex.dev/"),
            width="auto",
            height="600px"
                    ) 
