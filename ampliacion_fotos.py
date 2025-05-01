import reflex as rx
from state import State

def Ampliacion_fotos():
    return rx.box(
                rx.hstack(
                    rx.link(
                        rx.box(
                            rx.image("/coche.jpg",height="100%",border_radius="7px"),
                        position="absolute",  # Posición absoluta
                        left="100px",  # Posición fija desde la izquierda
                        width=rx.cond(
                        State.expanded_coche,
                        "400px",
                        "250px"),
                        height=rx.cond(
                        State.expanded_coche,
                        "400px", 
                        "250px"),
                        align="center",
                        on_mouse_enter=State.toggle_size_coche,
                        on_mouse_leave=State.toggle_size_coche,
                        transition="all 1s ease-in-out",
                        z_index=rx.cond(  # z-index condicional
                            State.expanded_coche,
                            "2",
                            "1"
                                        )
                            ),
                         ),
                    
                    #rx.spacer(),

                    rx.link(
                        rx.box(
                            rx.image("/bici.jpg",height="100%",border_radius="7px"),
                        position="absolute",  # Posición absoluta
                        left="400px",  # Posición fija desde la izquierda
                        width=rx.cond(
                        State.expanded_bici,
                        "400px",
                        "250px"),
                        height=rx.cond(
                        State.expanded_bici,
                        "400px", 
                        "250px"),
                        align="center",
                        on_mouse_enter=State.toggle_size_bici,
                        on_mouse_leave=State.toggle_size_bici,
                        transition="all 1s ease-in-out",
                        z_index=rx.cond(  # z-index condicional
                            State.expanded_bici,
                            "2",
                            "1"
                                        )
                            ),
                         ),    
            width="100%",
            height="50vh",
            padding_top="2em",
            spacing="2"
            ),
            position="relative",  # Contenedor con posición relativa
        width="100%",
        height="100vh"
    ) 