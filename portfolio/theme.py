from nicegui import ui
from contextlib import contextmanager
from . import config


@contextmanager
def frame():
    # Global Style with Warm Earthy Colors from config
    ui.add_head_html(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@300;400;600;700&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300;400;700;900&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
            
            body {{
                font-family: 'Crimson Pro', 'Merriweather', 'Outfit', serif;
                background-color: {config.COLOR_5};
                color: {config.COLOR_1};
                overflow-x: hidden;
            }}
        </style>
    """)
    with ui.column().classes("w-full min-h-screen items-center"):
        yield
