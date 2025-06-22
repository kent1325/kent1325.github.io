import reflex as rx
from portfolio.states.portfolio_state import PortfolioState
from portfolio.components.project_card import project_card


def projects_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Featured Projects",
                class_name="text-4xl sm:text-5xl font-bold text-slate-900 mb-12 sm:mb-16 text-center tracking-tight",
            ),
            rx.el.div(
                rx.cond(
                    PortfolioState.can_cycle_projects,
                    rx.el.button(
                        rx.icon(
                            tag="chevron_left",
                            class_name="w-7 h-7",
                        ),
                        on_click=lambda: PortfolioState.cycle_projects(-1),
                        class_name="p-3 rounded-full bg-indigo-600 text-white shadow-lg hover:bg-indigo-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 z-10 transform hover:scale-110 absolute top-1/2 -translate-y-1/2 left-[-2.5rem]",
                        aria_label="Previous projects",
                    ),
                    rx.el.div(class_name="w-12 h-12 flex-shrink-0"),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.foreach(
                            PortfolioState.processed_renderable_projects,
                            lambda p_with_key: project_card(
                                p_with_key,
                                additional_classes=PortfolioState.project_card_base_class_name,
                                style=PortfolioState.project_card_style,
                            ),
                        ),
                        style=PortfolioState.carousel_track_style,
                        class_name="flex gap-x-8",
                    ),
                    class_name="flex-grow overflow-hidden relative py-2 px-1",
                    on_mouse_enter=PortfolioState.pause_project_scrolling,
                    on_mouse_leave=PortfolioState.resume_project_scrolling,
                ),
                rx.cond(
                    PortfolioState.can_cycle_projects,
                    rx.el.button(
                        rx.icon(
                            tag="chevron_right",
                            class_name="w-7 h-7",
                        ),
                        on_click=lambda: PortfolioState.cycle_projects(1),
                        class_name="p-3 rounded-full bg-indigo-600 text-white shadow-lg hover:bg-indigo-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 z-10 transform hover:scale-110 absolute top-1/2 -translate-y-1/2 right-[-2.5rem]",
                        aria_label="Next projects",
                    ),
                    rx.el.div(class_name="w-12 h-12 flex-shrink-0"),
                ),
                class_name="flex items-center justify-between relative mx-auto max-w-10xl",
                on_mount=PortfolioState.start_project_auto_scroll,
            ),
            class_name="container mx-auto px-4 sm:px-6 py-20 sm:py-28 lg:py-32",
        ),
        class_name="bg-white",
        id="projects",
    )
