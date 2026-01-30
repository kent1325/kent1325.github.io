from nicegui import ui
import config


def create_header():
    """Creates the navigation header"""
    with (
        ui.header()
        .classes("items-center justify-between")
        .style(f"background-color:{config.PRIMARY_COLOR}")
    ):
        ui.label(config.SITE_TITLE).classes("text-h5")
        with ui.row():
            ui.link("Home", "#home")
            ui.link("About", "#about")
            ui.link("Projects", "#projects")
            ui.link("Contact", "#contact")


def create_footer():
    """Creates the footer section"""
    with (
        ui.footer()
        .classes("justify-center")
        .style(f"background-color: {config.PRIMARY_COLOR}")
    ):
        ui.label(f"© {config.COPYRIGHT_YEAR}. All rights reserved.")


@ui.page("/")
def main_page():
    # Add custom CSS for sustainable green gradient background
    ui.add_head_html("""
        <style>
            body {
                background: linear-gradient(135deg, #2d5016 0%, #3d7b2f 25%, #5ca963 50%, #3d7b2f 75%, #2d5016 100%);
                background-attachment: fixed;
                background-size: 400% 400%;
                animation: gradientShift 15s ease infinite;
                min-height: 100vh;
            }
            
            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
        </style>
    """)

    create_header()
    # HERO Section here
    create_footer()


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title=config.SITE_TITLE,
        port=config.PORT,
        reload=config.RELOAD,
        show=config.SHOW_BROWSER,
    )
