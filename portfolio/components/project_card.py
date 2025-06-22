import reflex as rx
from portfolio.states.portfolio_state import ProcessedProject
from typing import Dict

_PROJECT_CARD_BASE_CLASSES = "bg-white rounded-xl shadow-lg hover:shadow-2xl transition-all duration-300 ease-in-out flex flex-col border border-slate-200 overflow-hidden transform hover:scale-[1.02] hover:border-indigo-400"


def project_card(
    project: ProcessedProject,
    additional_classes: str | rx.Var[str] = "",
    style: rx.Var[Dict[str, str]] | Dict[str, str] | None = None,
) -> rx.Component:
    return rx.el.div(
        rx.cond(
            project["image_url"],
            rx.el.img(
                src=project["image_url"],
                alt=project["title"],
                class_name="w-full h-52 object-cover",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        tag="image_off",
                        class_name="w-16 h-16 text-slate-400",
                    ),
                    class_name="flex items-center justify-center h-full",
                ),
                class_name="w-full h-52 bg-slate-100 flex items-center justify-center",
            ),
        ),
        rx.el.div(
            rx.el.h3(
                project["display_title"],
                class_name="text-2xl font-bold text-slate-800 mb-3 tracking-tight h-16 overflow-hidden",
            ),
            rx.el.p(
                project["display_description"],
                class_name="text-slate-600 text-base mb-5 leading-relaxed flex-grow min-h-[80px] h-24 overflow-hidden",
            ),
            rx.el.div(
                rx.el.h4(
                    "Key Technologies:",
                    class_name="text-sm font-semibold text-slate-500 mb-2 uppercase tracking-wider",
                ),
                rx.el.div(
                    rx.foreach(
                        project["display_technologies"],
                        lambda tech: rx.el.span(
                            tech,
                            class_name="inline-block bg-indigo-100 text-indigo-700 px-3 py-1.5 rounded-md text-xs font-semibold mr-2 mb-2 shadow-sm",
                        ),
                    ),
                    class_name="flex flex-wrap mb-5 h-16 overflow-hidden",
                ),
            ),
            rx.el.div(
                rx.cond(
                    project["repo_url"],
                    rx.el.a(
                        rx.icon(
                            tag="github",
                            class_name="w-4 h-4 mr-2",
                        ),
                        "View Code",
                        href=project["repo_url"],
                        is_external=True,
                        class_name="inline-flex items-center text-sm text-slate-700 hover:text-indigo-600 font-medium py-2.5 px-4 rounded-lg hover:bg-slate-100 transition-all duration-200 border border-slate-300 hover:border-indigo-300 shadow-sm",
                    ),
                    rx.fragment(),
                ),
                rx.el.a(
                    rx.icon(
                        tag="book_text",
                        class_name="w-4 h-4 mr-2",
                    ),
                    "Read More",
                    href="#",
                    class_name="inline-flex items-center text-sm text-white bg-indigo-600 hover:bg-indigo-700 font-semibold py-2.5 px-5 rounded-lg transition-all duration-200 shadow-md hover:shadow-lg transform hover:scale-105",
                ),
                class_name="flex items-center mt-auto pt-5 border-t border-slate-200 space-x-3",
            ),
            class_name="p-6 flex flex-col flex-grow",
        ),
        class_name=[
            _PROJECT_CARD_BASE_CLASSES,
            additional_classes,
        ],
        style=rx.cond(
            rx.Var.create(style).is_none(),
            {"height": "auto", "min_height": "550px"},
            style,
        ),
    )
