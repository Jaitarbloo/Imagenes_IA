import reflex as rx
import asyncio

class State(rx.State):

    bird_x: int = 0

    def mover_pajaro(self):
        if self.bird_x < 90:
            self.bird_x += 10
        else:
            self.bird_x = 0

    expanded_coche: bool = False
    expanded_bici: bool = False

    def toggle_size_coche(self):
        self.expanded_coche = not self.expanded_coche

    def toggle_size_bici(self):
        self.expanded_bici = not self.expanded_bici

    imagenes: list[str] = [
        "/concorde 1.jpg",
        "/concorde 2.jpg", 
        "/concorde 3.jpg",
        "/concorde 7.jpg"
    ]
    indice_actual: int = 0

    expandida: bool = False
    
    def cambiar_tamano(self):
        # Alterna entre True y False
        self.expandida = not self.expandida
    
    async def auto_slider(self):
        while True:
            await asyncio.sleep(3)
            self.indice_actual = (self.indice_actual + 1) % len(self.imagenes)
            yield
            
    image_src: str = "20250413_113851 (2).jpg"
    favicon_rotando: bool = False

    carousel_images: list[str] = [
        "concorde 3.jpg", "concorde 4.jpg", "concorde 5.jpg"
    ]
    carousel_texts: list[str] = [
        "Desarrollo Frontend: Experiencia en React, HTML, CSS y UI modernas.",
        "Backend robusto: Python, Node.js, APIs REST y bases de datos SQL/NoSQL.",
        "DevOps & Cloud: Automatización, despliegue en la nube y CI/CD."
    ]
    carousel_index: int = 0

    def cambiar_imagen(self):
        self.image_src = "python.webp"

    def restaurar_imagen(self):
        self.image_src = "20250413_113851 (2).jpg"

    def girar_favicon(self):
        self.favicon_rotando = True

    def detener_favicon(self):
        self.favicon_rotando = False

    def siguiente_imagen(self):
        if self.carousel_index < len(self.carousel_images) - 1:
            self.carousel_index += 1

    def anterior_imagen(self):
        if self.carousel_index > 0:
            self.carousel_index -= 1 