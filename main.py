from nicegui import ui
import portfolio.config as config
import portfolio.theme as theme
import portfolio.hero as hero


@ui.page("/")
async def main():
    with theme.frame():
        # Your page content goes here - it will be inserted where the yield is
        hero


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title=config.SITE_TITLE,
        port=config.PORT,
        reload=config.RELOAD,
        show=config.SHOW_BROWSER,
    )
