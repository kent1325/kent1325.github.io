import reflex as rx
from portfolio.components.navbar import navbar
from portfolio.components.profile_section import profile_section
from portfolio.components.about_me_section import about_me_section
from portfolio.components.projects_section import projects_section
from portfolio.components.contact_section import contact_section
from portfolio.components.footer import footer
from portfolio.states.portfolio_state import PortfolioState


def index() -> rx.Component:
    return rx.el.div(
        rx.el.title(f"{PortfolioState.name} | Portfolio"),
        navbar(),
        profile_section(),
        about_me_section(),
        projects_section(),
        contact_section(),
        footer(),
        class_name="bg-white",
    )
