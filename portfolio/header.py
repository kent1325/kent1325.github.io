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
