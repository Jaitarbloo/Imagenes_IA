import reflex as rx
from state import State

def Encabezado() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack( 
                rx.image("/favicon.ico"),
                rx.link(
                    rx.text("Inicio",size="5", color_scheme="gray"),
                    href= "https://reflex.dev/docs/library/layout/box/"),
                rx.link(
                    rx.text("Documentos", size="5",color_scheme="gray"), 
                    href= "https://reflex.dev/docs/library/layout/box/"),
                rx.spacer(),
                rx.card(rx.text("Example")),
                width="100%",
               spacing="5", 
      
    ) 