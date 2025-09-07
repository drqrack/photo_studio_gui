from nicegui import ui


def render():
   
    # Big container for all contents
    with ui.element("div").style("background-image: url('/assets/hero.jpg')").classes("h-screen w-screen flex flex-col bg-cover bg-center justify-center items-center"):
        
        with ui.element("nav").classes("flex flex row justify-between items-center w-full fixed left-0 top-0 px-20 py-5 shadow-xl shadow-orange-400").style("font-family: 'Josefin Sans', sans-serif; font-optical-sizing: auto; font-style: normal;"):
            ui.label("m-S").classes("text-orange-400 font-bold text-lg hover:text-red-700 cursor-pointer bg-green-900 rounded-[100%] p-2")

            navlinks = [{"title": "Home", "path": "/"}, 
                        {"title": "Menu", "path": "/"}, 
                        {"title": "Reservation", "path": "/"},
                        {"title": "Gallery", "path": "/"},
                        {"title": "About", "path": "/"},
                        {"title": "Blog", "path": "/"}
                        ]
            
            with ui.row():
                for item in navlinks:
                    ui.link(item["title"], item["path"]).classes("no-underline uppercase text-orange-600 hover:text-orange-300")

            with ui.row().classes("text-orange-400 text-xl"):
                ui.html('<i class="fa-brands fa-facebook"></i>').classes("text-blue-600 hover:text-blue-800 cursor-pointer")
                ui.html('<i class="fa-brands fa-instagram"></i>').classes("hover:text-orange-800 cursor-pointer")
                ui.html('<i class="fa-brands fa-twitter"></i>').classes("text-sky-400 hover:text-sky-800 cursor-pointer")

        with ui.element("div").classes("text-white font-bold text-center").style("font-family: 'Josefin Sans', sans-serif; font-optical-sizing: auto; font-style: normal;"):
            ui.label("Welcome to").classes("text-5xl mb-4")
            ui.label("Melinda's Studio").classes("text-8xl text-orange-500 mb-8")
            ui.button("Look Menu").props("color=black-4").classes("shadow-2xl shadow-green-500 hover:shadow-orange-700")

                
            