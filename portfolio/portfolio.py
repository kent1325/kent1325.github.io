import reflex as rx
from portfolio.pages.index import index
from portfolio.states.portfolio_state import PortfolioState

app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=[
        "/custom_styles.css",
        "https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css",
    ],
)
app.add_page(
    index,
    title=f"{PortfolioState.name} | Portfolio",
    description="A dynamic portfolio showcasing projects and skills of a Data Scientist, Machine Learning Engineer, and AI Engineer.",
    image="/assets/favicon.ico",
)
