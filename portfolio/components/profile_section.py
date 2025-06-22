import reflex as rx
from portfolio.states.portfolio_state import PortfolioState


def profile_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.img(
                    src=PortfolioState.profile_picture_url,
                    alt=PortfolioState.name,
                    class_name="w-64 h-64 sm:w-80 sm:h-80 rounded-full object-cover mx-auto shadow-2xl border-2 border-white transform hover:scale-110 transition-transform duration-300",
                ),
                rx.el.h1(
                    PortfolioState.name,
                    class_name="text-4xl sm:text-6xl font-extrabold text-slate-900 mt-8 text-center tracking-tight",
                ),
                rx.el.div(
                    rx.el.p(
                        PortfolioState.displayed_title_text,
                        class_name="text-2xl sm:text-3xl font-semibold text-indigo-600 mt-2 text-center h-10 sm:h-12",
                    ),
                    class_name="min-h-[3rem] sm:min-h-[3.5rem]",
                    on_mount=PortfolioState.typewriter_effect_loop,
                ),
                rx.el.p(
                    PortfolioState.bio,
                    class_name="text-slate-700 mt-6 text-lg sm:text-xl text-center max-w-3xl mx-auto leading-relaxed",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon(
                            tag="linkedin",
                            class_name="w-5 h-5 mr-2.5",
                        ),
                        "Connect on LinkedIn",
                        href=PortfolioState.linkedin_url,
                        is_external=True,
                        class_name="inline-flex items-center justify-center px-8 py-3 border border-transparent text-base font-semibold rounded-lg text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105",
                    ),
                    class_name="mt-10 text-center",
                ),
            ),
            class_name="container mx-auto px-4 sm:px-6 py-20 sm:py-28 lg:py-32",
        ),
        class_name="bg-white",
        id="profile",
    )
