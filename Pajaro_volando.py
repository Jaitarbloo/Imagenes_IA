import reflex as rx
from state import State

def Pajaro_volando():
    bird_svg = rx.html(
        '''
        <svg width="80" height="40" viewBox="0 0 80 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10 30 Q 40 10 70 30 Q 50 20 40 30 Q 30 20 10 30" fill="white" stroke="white" stroke-width="2"/>
        </svg>
        ''',
         style={
            "position": "absolute",
            "top": "20vh",
            "left": f"{State.bird_x}vw",
            "zIndex": 2,
            "pointerEvents": "none",
            "transition": "left 0.3s linear"
        }
    )

    return rx.box(
        rx.image(
            src="concorde 7.jpg",  # Cambia por la imagen que quieras
            style={
                "position": "absolute",
                "width": "100vw",
                "height": "100vh",
                "objectFit": "cover",
                "zIndex": 0,
            }
        ),
        bird_svg,
        rx.button(
            "Volar",
            on_click=State.mover_pajaro,
            style={
                "position": "absolute",
                "bottom": "2em",
                "left": "50%",
                "transform": "translateX(-50%)",
                "zIndex": 3,
                "fontSize": "2em",
                "padding": "1em 2em"
            }
        ),
        position="relative",
        width="100vw",
        height="100vh",
        overflow="hidden"
    ) 
