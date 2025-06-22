import reflex as rx
from portfolio.states.portfolio_state import PortfolioState


def _input_field_class(
    has_error: rx.Var[bool],
) -> rx.Var[str]:
    base_class = "mt-1 block w-full px-4 py-3 bg-white border rounded-lg text-base shadow-sm placeholder-slate-400 focus:outline-none sm:text-sm transition-colors duration-200"
    error_class = f"{base_class} border-red-500 focus:ring-red-500 focus:border-red-500"
    normal_class = f"{base_class} border-slate-300 focus:ring-indigo-500 focus:border-indigo-500 hover:border-slate-400"
    return rx.cond(has_error, error_class, normal_class)


def contact_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Let's Connect",
                class_name="text-4xl sm:text-5xl font-bold text-slate-900 mb-6 sm:mb-8 text-center tracking-tight",
            ),
            rx.el.p(
                "Interested in collaborating or have a question? Feel free to reach out. I'm always open to discussing new projects and opportunities.",
                class_name="text-slate-700 text-lg sm:text-xl text-center max-w-2xl mx-auto mb-10 sm:mb-12 leading-relaxed",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Full Name",
                        html_for="contact_name",
                        class_name="block text-sm font-semibold text-slate-700 mb-1.5",
                    ),
                    rx.el.input(
                        id="contact_name",
                        name="contact_name",
                        type="text",
                        placeholder="e.g., Jane Doe",
                        default_value=PortfolioState.contact_name,
                        key=f"contact_name_key_{PortfolioState.contact_name}",
                        class_name=_input_field_class(
                            PortfolioState.contact_errors.contains("name")
                        ),
                    ),
                    rx.cond(
                        PortfolioState.contact_errors.contains("name"),
                        rx.el.p(
                            PortfolioState.contact_errors["name"],
                            class_name="text-red-600 text-xs mt-1.5",
                        ),
                        rx.fragment(),
                    ),
                    class_name="mb-5",
                ),
                rx.el.div(
                    rx.el.label(
                        "Email Address",
                        html_for="contact_email",
                        class_name="block text-sm font-semibold text-slate-700 mb-1.5",
                    ),
                    rx.el.input(
                        id="contact_email",
                        name="contact_email",
                        type="email",
                        placeholder="you@example.com",
                        default_value=PortfolioState.contact_email,
                        key=f"contact_email_key_{PortfolioState.contact_email}",
                        class_name=_input_field_class(
                            PortfolioState.contact_errors.contains("email")
                        ),
                    ),
                    rx.cond(
                        PortfolioState.contact_errors.contains("email"),
                        rx.el.p(
                            PortfolioState.contact_errors["email"],
                            class_name="text-red-600 text-xs mt-1.5",
                        ),
                        rx.fragment(),
                    ),
                    class_name="mb-5",
                ),
                rx.el.div(
                    rx.el.label(
                        "Your Message",
                        html_for="contact_message",
                        class_name="block text-sm font-semibold text-slate-700 mb-1.5",
                    ),
                    rx.el.textarea(
                        id="contact_message",
                        name="contact_message",
                        placeholder="How can I help you?",
                        on_change=PortfolioState.set_contact_message,
                        default_value=PortfolioState.contact_message,
                        rows=5,
                        max_length=PortfolioState.MAX_CONTACT_MESSAGE_LENGTH,
                        class_name=_input_field_class(
                            PortfolioState.contact_errors.contains("message")
                        ),
                    ),
                    rx.el.div(
                        rx.el.span(
                            PortfolioState.contact_message_length.to_string(),
                            class_name=rx.cond(
                                PortfolioState.contact_message_length
                                > PortfolioState.MAX_CONTACT_MESSAGE_LENGTH,
                                "text-red-600 font-medium",
                                "text-slate-600",
                            ),
                        ),
                        rx.el.span(
                            f" / {PortfolioState.MAX_CONTACT_MESSAGE_LENGTH} characters"
                        ),
                        class_name="text-xs text-slate-500 text-right mt-1.5",
                    ),
                    rx.cond(
                        PortfolioState.contact_errors.contains("message"),
                        rx.el.p(
                            PortfolioState.contact_errors["message"],
                            class_name="text-red-600 text-xs mt-1.5",
                        ),
                        rx.fragment(),
                    ),
                    class_name="mb-6",
                ),
                rx.el.button(
                    rx.cond(
                        PortfolioState.is_contact_submitting,
                        rx.el.div(
                            rx.spinner(class_name="mr-2.5 w-5 h-5 text-white"),
                            "Sending...",
                            class_name="flex items-center justify-center",
                        ),
                        "Send Message",
                    ),
                    type="submit",
                    disabled=PortfolioState.is_contact_submitting,
                    class_name="w-full bg-indigo-600 text-white px-8 py-3.5 rounded-lg font-semibold text-base hover:bg-indigo-700 transition-all duration-200 shadow-md hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-70 disabled:cursor-not-allowed transform hover:scale-105",
                ),
                on_submit=PortfolioState.handle_contact_submission,
                reset_on_submit=True,
                class_name="max-w-xl mx-auto bg-white p-8 sm:p-10 rounded-xl shadow-xl border border-slate-200",
            ),
            rx.el.div(
                rx.el.p(
                    "Or find me on these platforms:",
                    class_name="text-slate-700 text-lg text-center mt-10 sm:mt-12 mb-6",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon(
                            tag="linkedin",
                            class_name="w-6 h-6 mr-2",
                        ),
                        "LinkedIn",
                        href=PortfolioState.linkedin_url,
                        is_external=True,
                        class_name="inline-flex items-center bg-blue-600 text-white px-6 py-2.5 rounded-lg font-medium hover:bg-blue-700 transition-colors shadow-md hover:shadow-lg transform hover:scale-105 text-base mx-2 my-1",
                    ),
                    rx.el.a(
                        rx.icon(
                            tag="github",
                            class_name="w-6 h-6 mr-2",
                        ),
                        "GitHub",
                        href=PortfolioState.github_url,
                        is_external=True,
                        class_name="inline-flex items-center bg-slate-800 text-white px-6 py-2.5 rounded-lg font-medium hover:bg-slate-900 transition-colors shadow-md hover:shadow-lg transform hover:scale-105 text-base mx-2 my-1",
                    ),
                    class_name="flex justify-center items-center flex-wrap gap-y-3 gap-x-4",
                ),
                class_name="mt-12",
            ),
            class_name="container mx-auto px-4 sm:px-6 py-20 sm:py-28 lg:py-32",
        ),
        class_name="bg-slate-50",
        id="contact",
    )
