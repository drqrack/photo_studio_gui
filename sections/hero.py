from nicegui import ui


def render():
   
    # Big container for all contents
    with ui.element("div").style("background-image: url('/assets/hero.jpg')").classes("h-screen w-screen flex flex-col bg-cover bg-center justify-center items-center"):
        
        with ui.element("nav").classes("flex flex row justify-between items-center w-full fixed left-0 top-0 px-20 py-10"):
            ui.label("LOGO").classes("text-orange-400 font-bold text-2xl")

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

            with ui.row().classes("text-white"):
                ui.html('<i class="fa-brands fa-facebook"></i>')
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-twitter"></i>')

        with ui.element("div").classes("text-white font-bold text-center"):
            ui.label("Welcome to").classes("text-4xl mb-4")
            ui.label("Family's Studio").classes("text-8xl text-orange-500 mb-8")
            ui.button("Look Menu").props("color=red").classes("")

                
            