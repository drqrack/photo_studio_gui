from nicegui import ui


def render():
   
    # Big container for all contents
    with ui.element("div").style("background-image: url('/assets/hero.jpg')").classes("h-screen w-screen flex flex-col bg-cover bg-center justify-center items-center"):
        
        with ui.element("nav").classes("flex flex row justify-between items-center w-full fixed left-0 top-0 px-20 py-10"):
            ui.label("f-S").classes("text-orange-400 font-bold text-lg hover:text-white cursor-pointer bg-green-900 rounded-[100%] p-2")

            navlinks = [{"title": "Home", "path": "/"}, 
                        {"title": "Menu", "path": "/"}, 
                        {"title": "Reservation", "path": "/"},
                        {"title": "Gallery", "path": "/"},
                        {"title": "About", "path": "/"},
                        {"title": "Blog", "path": "/"}
                        ]
            
            with ui.row():
                for item in navlinks:
                    ui.link(item["title"], item["path"]).classes("no-underline uppercase text-white")

            with ui.row().classes("text-orange-400 text-lg"):
                ui.html('<i class="fa-brands fa-facebook"></i>').classes("hover:text-white cursor-pointer")
                ui.html('<i class="fa-brands fa-instagram"></i>').classes("hover:text-white cursor-pointer")
                ui.html('<i class="fa-brands fa-twitter"></i>').classes("hover:text-white cursor-pointer")

        with ui.element("div").classes("text-white font-bold text-center"):
            ui.label("Welcome to").classes("text-5xl mb-4")
            ui.label("Family's Studio").classes("text-8xl text-orange-500 mb-8")
            ui.button("Look Menu").props("color=black-4").classes("shadow-2xl shadow-green-500")

                
            