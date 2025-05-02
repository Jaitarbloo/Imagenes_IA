import reflex as rx
import asyncio

class State(rx.State):
    imagenes: list[str] = [
        "/concorde 1.jpg",
        "/concorde 2.jpg", 
        "/concorde 3.jpg",
        "/concorde 7.jpg"
    ]
    indice_actual: int = 0

    async def auto_slider(self):
        while True:
            await asyncio.sleep(3)
            self.indice_actual = (self.indice_actual + 1) % len(self.imagenes)
            yield

def index():
    return rx.box(
        rx.image(
            src=State.imagenes[State.indice_actual],
            width="800px",
            height="400px"
        ),
        display="flex",
        justify="center",
        align="center",
        height="100vh",
        width="100vw",
        margin_top="0"
    )

app = rx.App()
app.add_page(index, on_load=State.auto_slider)
