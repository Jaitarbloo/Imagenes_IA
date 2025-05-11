import reflex as rx

def Reborde_llamativo():
    return rx.center(
        rx.vstack(
            rx.box(
                rx.image(
                    src="bici.jpg",
                    alt="Mi foto bonita",
                    width=["300px", "350px", "400px"],  # Ancho más grande
                    height=["200px", "250px", "300px"],  # Altura más pequeña para efecto ovalado
                    border_radius="50%",  # Mantiene los bordes redondeados
                    box_shadow="0 0 30px 0 #6cf",
                    transition="all 0.3s ease",
                    _hover={
                        "transform": "scale(1.1)",
                        "box_shadow": "0 0 60px 0 #6cf"
                    },
                    object_fit="cover",
                    margin="auto",
                ),
                display="flex",
                justify="center",
                align_items="center",
                width="100%",
                padding="2em"
            ),
            rx.heading("¡Hola! Soy [Tu Nombre]", font_size=["1.5em", "2em", "2.5em"], color="white"),
            rx.text(
                "Soy freelance y puedo ayudarte con tus proyectos. ¡Contáctame!", 
                font_size=["1em", "1.2em", "1.4em"], 
                color="white",
                text_align="center"  # Centra el texto
            ),
            align="center",
            spacing="4",
            width="100%",
            padding=["1em", "2em", "3em"]  # Padding responsive
        ),
        min_height="100vh",
        bg="#1a1a2e",
        width="100%"
    )

app = rx.App()
app.add_page(Reborde_llamativo, title="Reborde Llamativo")
