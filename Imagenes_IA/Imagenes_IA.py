import reflex as rx
import asyncio
from state import State
from navbar import Navbar
from carrusel import carrusel_imagenes
from inicio_fin import inicio_y_fin
from fotos_giradas import Fotos_giradas_con_link
from ampliacion_fotos import Ampliacion_fotos
from iconos_fotos import iconos_dentro_fotos
from encabezado import Encabezado
from zabalgana_web import Zabalgana_web_estatica_Vercel
from madrid_imagenes import imagenes_comunidad_madrid
from pajaro import Pajaro_volando

def index():
    return rx.center(
            rx.box(
            # Fondo difuminado
            rx.image(
                src="concorde 7.jpg",
                style={
                    "position": "absolute",
                    "zIndex": "-1",
                    "width": "100vw",
                    "height": "100vh",
                    "objectFit": "cover",
                    "filter": "blur(16px) brightness(0.6)"
                }
            ),
            rx.center(
                rx.vstack(
                    Navbar(),
                    rx.heading(
                        "Desarrollador web freelancer",
                        font_size="3em",  # Más grande
                        color="white",
                        text_align="center",
                        max_width="90vw",
                        margin_top="1.5em"
                    ),
                    carrusel_imagenes(),
                    rx.text(
                        "Freelancer Fullstack: desarrollo web moderno, APIs, automatización y despliegue.",
                        font_size="1.7em",  # Más grande
                        color="white",
                        margin_bottom="2.5em",
                        text_align="center",
                        max_width="90vw"
                    ),
                    Fotos_giradas_con_link(),
                    Ampliacion_fotos(),
                    iconos_dentro_fotos(),
                    Encabezado(),
                    Zabalgana_web_estatica_Vercel(),
                    imagenes_comunidad_madrid(),
                    Pajaro_volando(),
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
                    inicio_y_fin(),
                    rx.image(
                        src="python.webp",
                        width=["70vw", "320px"],  # Más grande y cuadrada
                        height=["70vw", "320px"],
                        max_width="320px",
                        max_height="320px",
                        style={
                            "transition": "transform 0.5s",
                            "transform": rx.cond(State.favicon_rotando, "rotate(360deg)", "rotate(0deg)"),
                            "border_radius": "50%",
                            "object_fit": "cover",
                            "overflow": "hidden",
                            "boxShadow": "0 4px 32px rgba(0,0,0,0.5)"
                        },
                        on_mouse_enter=State.girar_favicon,
                        on_mouse_leave=State.detener_favicon,
                        margin_bottom="1.5em"
                    ),  # Llama a la función index de Ampliar_imagenes
                    rx.hstack(
                        rx.button("<", on_click=State.anterior_imagen, font_size="2em", padding="1em"),
                        rx.center(
                            rx.vstack(
                                rx.image(
                                    src=State.carousel_images[State.carousel_index],
                                    width=["95vw", "600px"],  # Más grande y responsivo
                                    max_width="600px",
                                    height="auto",
                                    border_radius="24px",
                                    box_shadow="0 4px 32px rgba(0,0,0,0.5)"
                                ),
                                rx.text(
                                    State.carousel_texts[State.carousel_index],
                                    text_align="center",
                                    color="white",
                                    margin_top="1.5em",
                                    font_size="1.5em",  # Más grande
                                    background="rgba(0,0,0,0.5)",
                                    border_radius="12px",
                                    padding="1em",
                                    max_width="600px",
                                ),
                            ),
                        ),
                        rx.button(">", on_click=State.siguiente_imagen, font_size="2em", padding="1em"),
                        spacing="4",
                        justify_content="center",
                        align_items="center"
                    ),
                    spacing="8",
                    justify_content="center",
                    align_items="center"
                ),
                width="100vw",
                min_height="100vh",
                padding="3em"
            ),
            position="relative",
            width="100vw",
            min_height="100vh",
            overflow_y="auto"
        )
    )


app = rx.App()
app.add_page(index)#on_load=State.auto_slider) IMPORTANTE...cuando lo activo se para el backend

