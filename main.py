from nicegui import ui
import portfolio.config as config
import portfolio.theme as theme


@ui.page("/")
async def main():
    with theme.frame():
        # Your page content goes here - it will be inserted where the yield is
        ui.label("Welcome to my portfolio").classes("text-4xl font-bold")
        ui.label("This is where your content goes").classes("text-xl mt-4")

        ui.label("Welcome - Merriweather (default)").classes("text-4xl font-bold")
        ui.label("Welcome - Crimson Pro").classes("text-4xl font-bold font-crimson")
        ui.label("Welcome - Lora").classes("text-4xl font-bold font-lora")
        ui.label("Welcome - Quattrocento").classes(
            "text-4xl font-bold font-quattrocento"
        )
        ui.label("Welcome - Bitter").classes("text-4xl font-bold font-bitter")
        ui.label("Welcome - Inter (sans)").classes("text-4xl font-bold font-inter")
        ui.label("Welcome - DM Sans").classes("text-4xl font-bold font-dmsans")


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title=config.SITE_TITLE,
        port=config.PORT,
        reload=config.RELOAD,
        show=config.SHOW_BROWSER,
    )
