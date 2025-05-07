import reflex as rx
from rxconfig import config


class State(rx.State):

    image_src: str = "/20250413_113851 (2).jpg"
    
    def cambiar_imagen(self):
        self.image_src = "python.webp"

    def restaurar_imagen(self):
        self.image_src = "/20250413_113851 (2).jpg" 

    ...
def Cambio_imagen():
    return rx.center(
                rx.image(
                        src=State.image_src,
                        width=["95vw", "550px"],  # Más grande y responsivo
                        max_width="550px",
                        height="auto",
                        margin_bottom="1.5em",
                        style={"boxShadow": "0 4px 32px rgba(0,0,0,0.5)"},
                        on_mouse_enter=State.cambiar_imagen,
                        on_mouse_leave=State.restaurar_imagen,
                    ),
                    align="center",      # Centra verticalmente
                    justify="center",    # Centra horizontalmente
                    height="100vh",
                    width="100vw",

    )

app = rx.App()
app.add_page(Cambio_imagen, title="Cambio de Imagen")
