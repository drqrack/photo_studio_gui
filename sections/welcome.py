from nicegui import ui


def render():
    with ui.element("div").classes(
        "w-screen h-screen flex flex-row justify-center items-center"
    ):
        with ui.element("div").classes("w-1/2 px-10 py-10 text-center items-center"):
            ui.label("Melinda Studio").style(
                'font-family: "Caveat", cursive; font-optical-sizing: auto; font-weight: <weight>; font-style: normal;'
            ).classes("text-4xl text-orange-500")
            ui.label("WELCOME").classes("text-5xl font-bold p-2").style(
                'font-family: "Archivo Black", sans-serif; font-weight: 400; font-style: normal;'
            )
            ui.label("Let's create man in our own image...we are beautiful").style(
                "font-family: 'Josefin Sans', sans-serif; font-optical-sizing: auto; font-style: normal;"
            ).classes("text-lg p-2 text-gray-500")
            ui.link("Our Story", "/").classes(
                "no-underline uppercase text-gray-500 hover:text-orange-400 hover:font-bold"
            ).style(
                "font-family: 'Josefin Sans', sans-serif; font-optical-sizing: auto; font-style: normal;"
            )

        with ui.element("div").classes("w-1/2 px-10 py-10"):
            ui.image("/assets/welcome.jpg").classes()
