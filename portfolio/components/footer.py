import reflex as rx
from portfolio.states.portfolio_state import PortfolioState
import datetime


def footer() -> rx.Component:
    current_year = datetime.date.today().year
    return rx.el.footer(
        rx.el.div(
            rx.el.p(
                f"© {current_year} {PortfolioState.name}. All Rights Reserved.",
                class_name="text-sm text-slate-600",
            ),
            rx.el.div(
                rx.el.p(
                    "Built with ",
                    rx.el.a(
                        "Reflex",
                        href="https://reflex.dev",
                        is_external=True,
                        class_name="text-indigo-600 hover:text-indigo-700 font-semibold",
                    ),
                    " & ",
                    rx.el.a(
                        "Tailwind CSS",
                        href="https://tailwindcss.com",
                        is_external=True,
                        class_name="text-sky-600 hover:text-sky-700 font-semibold",
                    ),
                    ".",
                    class_name="text-sm text-slate-600",
                ),
                class_name="flex items-center space-x-4 mt-2 sm:mt-0",
            ),
            class_name="container mx-auto px-4 sm:px-6 py-8 text-center sm:flex sm:justify-between sm:items-center",
        ),
        class_name="bg-slate-100 border-t border-slate-200",
    )
