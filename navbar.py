import reflex as rx
from state import State

def Navbar() -> rx.Component:
    
    return rx.vstack(
                rx.hstack(  
                        rx.image("/logotipo air france.jpg",height="100px"),

                        rx.link(
                            rx.text("Desarrollo y Diseño",size="6", color_scheme="gray"),
                            href= "https://reflex.dev",),
                        rx.link(
                            rx.text("Caracteristicas Técnicas", size="6",color_scheme="gray"), 
                            href= "https://reflex.dev"),
                        rx.link(
                            rx.text("Operadores", size="6",color_scheme="gray"), 
                            href= "https://reflex.dev"),
                        rx.link(
                            rx.text("Exposiciones", size="6",color_scheme="gray"), 
                            href= "https://reflex.dev"),
                
                        rx.spacer(),

                        rx.image("/logotipo british airways.jpg",height="100px"),

                width="100%",
                height="100px",
                spacing="8", 
                background="linear-gradient(45deg, red, blue)",
                align="center",
                position="fixed",
                top="0"
                        ),
            background="linear-gradient(45deg, red, blue)",
            justify="center",
            align="center",
            width="100%",
            
            
                    ) 