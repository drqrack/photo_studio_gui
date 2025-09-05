from nicegui import ui

def render():
    with ui.element("div").classes("w-screen h-screen flex flex-row justify-center items-center"):
        with ui.element("div").classes("w-1/2 px-10 py-10"):
            ui.label("Melinda Studio")
            ui.label("WELCOME")
            ui.label("Let's create man in our own image...we are beautiful")
            ui.link("Our Story", "/")

        with ui.element("div").classes("w-1/2 px-10 py-10"):
            ui.image("/assets/welcome.jpg").classes()