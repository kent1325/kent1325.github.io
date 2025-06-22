import reflex as rx
from portfolio.states.portfolio_state import PortfolioState


def skill_list_item(skill: str) -> rx.Component:
    return rx.el.li(
        rx.el.span(
            rx.icon(
                tag="square_check",
                class_name="w-6 h-6 text-indigo-500 mr-3 flex-shrink-0",
            ),
            skill,
            class_name="flex items-center text-slate-700 text-base sm:text-lg leading-relaxed",
        ),
        class_name="mb-3",
    )


def about_me_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "About Me",
                class_name="text-4xl sm:text-5xl font-bold text-slate-900 mb-10 sm:mb-16 text-center tracking-tight",
            ),
            rx.el.p(
                PortfolioState.about_me_summary,
                class_name="text-slate-700 text-lg sm:text-xl text-center max-w-4xl mx-auto mb-12 sm:mb-20 leading-relaxed",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Technical Expertise",
                        class_name="text-2xl sm:text-3xl font-semibold text-slate-800 mb-8 text-center sm:text-left tracking-tight",
                    ),
                    rx.el.ul(
                        rx.foreach(
                            PortfolioState.hard_skills,
                            skill_list_item,
                        ),
                        class_name="space-y-1",
                    ),
                    class_name="bg-white p-6 sm:p-8 rounded-xl shadow-lg hover:shadow-2xl transition-shadow duration-300",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Professional Strengths",
                        class_name="text-2xl sm:text-3xl font-semibold text-slate-800 mb-8 text-center sm:text-left tracking-tight",
                    ),
                    rx.el.ul(
                        rx.foreach(
                            PortfolioState.soft_skills,
                            skill_list_item,
                        ),
                        class_name="space-y-1",
                    ),
                    class_name="bg-white p-6 sm:p-8 rounded-xl shadow-lg hover:shadow-2xl transition-shadow duration-300",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Passions & Pursuits",
                        class_name="text-2xl sm:text-3xl font-semibold text-slate-800 mb-8 text-center sm:text-left tracking-tight",
                    ),
                    rx.el.ul(
                        rx.foreach(
                            PortfolioState.interests,
                            skill_list_item,
                        ),
                        class_name="space-y-1",
                    ),
                    class_name="bg-white p-6 sm:p-8 rounded-xl shadow-lg hover:shadow-2xl transition-shadow duration-300",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8 sm:gap-12",
            ),
            class_name="container mx-auto px-4 sm:px-6 py-20 sm:py-28 lg:py-32",
        ),
        class_name="bg-slate-50",
        id="about",
    )
