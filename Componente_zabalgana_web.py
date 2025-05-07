import reflex as rx
from state import State

def Zabalgana_web_estatica_Vercel():
    fotos = [
        {"src": "20250413_113851.jpg", "texto": "Desarrollo de sitios web rápidos y modernos."},
        {"src": "python.webp", "texto": "Diseño responsivo para móviles y escritorio."},
        {"src": "Visual-Studio-Code-Toolkit.jpg", "texto": "Trato directo con el cliente."},
        {"src": "visual-studio-code.jpg", "texto": "Soporte y mantenimiento personalizado."},
    ]
    return rx.vstack(
        rx.heading("Desarrollador Web Freelancer", size="8"),
        rx.text("Hola, soy desarrollador web freelance, y me dedico a crear sitios web modernos, funcionales y optimizados que impulsan negocios e ideas."),
        rx.grid(
            *[
                rx.vstack(
                    rx.image(src=f["src"], width="400px"),
                    rx.text(f["texto"], align="center"),
                ) for f in fotos
            ],
            columns="2",
            spacing="6",
            padding="2em",
        ),
        rx.divider(),
        rx.heading("Contáctame", size="6"),
        rx.form(
            rx.vstack(
                rx.input(placeholder="Tu nombre", name="nombre", required=True),
                rx.input(placeholder="Tu email", name="email", required=True, type="email"),
                rx.text_area(placeholder="¿En qué te puedo ayudar?", name="mensaje", required=True, rows="4"),
                rx.button("Enviar", type="submit", color_scheme="indigo"),
            ),
            # No on_submit ni reset_on_submit
            width="100%",
            max_width="400px",
            align="center",
        ),
        align="center",
        spacing="2",
        padding="2em"
    ) 
