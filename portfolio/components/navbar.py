import reflex as rx
from portfolio.states.portfolio_state import PortfolioState


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.a(
                PortfolioState.name,
                href="/",
                class_name="text-3xl font-bold text-slate-900 hover:text-indigo-600 transition-colors duration-200",
            ),
            rx.el.div(
                rx.el.a(
                    "About",
                    href="#about",
                    class_name="text-slate-700 hover:text-indigo-600 transition-colors duration-200 px-4 py-2 rounded-md text-base font-medium hover:bg-indigo-50",
                ),
                rx.el.a(
                    "Projects",
                    href="#projects",
                    class_name="text-slate-700 hover:text-indigo-600 transition-colors duration-200 px-4 py-2 rounded-md text-base font-medium hover:bg-indigo-50",
                ),
                rx.el.a(
                    "Contact",
                    href="#contact",
                    class_name="text-slate-700 hover:text-indigo-600 transition-colors duration-200 px-4 py-2 rounded-md text-base font-medium hover:bg-indigo-50",
                ),
                class_name="flex items-center space-x-2 sm:space-x-4",
            ),
            class_name="container mx-auto flex items-center justify-between py-4 px-4 sm:px-6",
        ),
        class_name="bg-white/90 backdrop-blur-lg shadow-md sticky top-0 z-50 border-b border-slate-200",
    )
