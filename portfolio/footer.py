from nicegui import ui
import config


def create_footer():
    """Creates the footer section"""
    with (
        ui.footer()
        .classes("justify-center")
        .style(f"background-color: {config.PRIMARY_COLOR}")
    ):
        ui.label(f"© {config.COPYRIGHT_YEAR}. All rights reserved.")
