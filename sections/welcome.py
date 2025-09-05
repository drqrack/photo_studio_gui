from nicegui import ui

def render():
    with ui.element("div"):
        with ui.element("div"):
            ui.label("Melinda Studio")
            ui.label("WELCOME")
            ui.label("Let's create man in our own image...we are beautiful")
            ui.link("Our Story", "/")