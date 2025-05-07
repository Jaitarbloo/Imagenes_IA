import reflex as rx

class State(rx.State):

    favicon_rotando: bool = False

    def girar_favicon(self):
        self.favicon_rotando = True

    def detener_favicon(self):
        self.favicon_rotando = False

def Favicon_rotando():

    return rx.center(
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
                        margin_bottom="1.5em",
                      
                    ),
                    align="center",      # Centra verticalmente
                    justify="center",    # Centra horizontalmente
                    height="100vh",
                    width="100vw", 


    )

app = rx.App()
app.add_page(Favicon_rotando, title="Favicon Rotando")
