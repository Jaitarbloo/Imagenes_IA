import reflex as rx

class State(rx.State):
    expanded_coche: bool = False
    expanded_bici: bool = False

    def toggle_size_coche(self):
        self.expanded_coche = not self.expanded_coche

    def toggle_size_bici(self):
        self.expanded_bici = not self.expanded_bici

def Ampliacion_fotos():
    return rx.flex( 
        rx.box(
            rx.image(
                src="/coche.jpg",
                border_radius="7px",
                width=rx.cond(State.expanded_coche, "400px", "250px"),
                height=rx.cond(State.expanded_coche, "400px", "250px"),
                transition="all 0.5s ease-in-out",
            ),
            on_mouse_enter=State.toggle_size_coche,
            on_mouse_leave=State.toggle_size_coche,
            align="center",
            justify="center",
        ),
        rx.box(
            rx.image(
                src="/bici.jpg",
                border_radius="7px",
                width=rx.cond(State.expanded_bici, "400px", "250px"),
                height=rx.cond(State.expanded_bici, "400px", "250px"),
                transition="all 0.5s ease-in-out",
            ),
            on_mouse_enter=State.toggle_size_bici,
            on_mouse_leave=State.toggle_size_bici,
            align="center",
            justify="center",
        ),
        spacing="4",
        justify="center",
        align="center",
        width="100%",
        height="70vh",
    )

app = rx.App()
app.add_page(Ampliacion_fotos, title="Ampliacion_fotos")
