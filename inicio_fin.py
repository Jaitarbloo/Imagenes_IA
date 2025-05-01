import reflex as rx
from state import State

def inicio_y_fin():

    return rx.flex(
                rx.vstack( 
                    rx.heading( "Su Primer Vuelo", size="6",color="black"),
                    rx.image ("/concorde 6.jpg",width="50%", height="300px"),
                    rx.text ("En febrero de 1965, empezó la construcción "
                             "de dos prototipos: el Concorde 001, cons-"
                             "truido por Aérospatiale en Toulouse y el 002"
                             "por BAC en Filton,Bristol. El Concorde 001 "
                             "hizo su primer vuelo de prueba el 2 de marzo"
                             "de 1969, en Toulouse, pilotado por André "
                             "Turcat.18....",rx.link("leer más", color="black",
                               font_weight="bold",
                               href="https://es.wikipedia.org/wiki/Concorde"),
                    color="black",
                    width="70%",
                    height="400px"),
                            
                width="50%",
                height="700px",
                max_width="500px",
                padding="1em",
                margin="1em",
                border_radius="0.5em",
                align="center",
                background="white"),

                rx.divider(orientation="vertical", size="4"),

                rx.vstack( 
                    rx.heading( "Su Último Vuelo", size="6",color="black"),
                    rx.image ("/concorde 5.jpg",width="50%",height="300px"),
                    rx.text ("El 10 de abril de 2003, Air France y British Airways "
                             "anunciaron al mismo tiempo que retirarían el Concorde"
                             "a finales de año. Las razones dadas para retirarlo   "
                             "fueron los siguientes: el bajo número de pasajeros   "
                             "tras el accidente del 25 de julio de 2000, el aumento"
                             " de los costes de mantenimiento y la caída de los... ",
                              rx.link("leer más", color="black",font_weight="bold",
                                  href="https://es.wikipedia.org/wiki/Concorde"),
                    color="black",
                    width="70%",
                    height="400px"),                              
                width="50%",
                height="700px",
                max_width="500px",
                padding="1em",
                margin="1em",
                border_radius="0.5em",
                align="center",
                background="white"),
             ) 