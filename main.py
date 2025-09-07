from nicegui import ui, app
from sections import hero, welcome

# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")
    
# link external icons to the head
ui.add_head_html('''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
                 <link rel="stylesheet" href="/assets/reset.css"/>
                 <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Caveat:wght@400..700&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&display=swap" rel="stylesheet">
                 ''') 


hero.render()
welcome.render()

ui.run()