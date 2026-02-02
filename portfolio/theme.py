from nicegui import ui
from contextlib import contextmanager
from . import config


@contextmanager
def frame():
    # Global Style with Warm Earthy Colors from config
    ui.add_head_html(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@300;400;600;700&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300;400;700;900&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&display=swap');
            
            body {{
                font-family: 'Crimson Pro', 'Merriweather', 'Outfit', serif;
                background-color: {config.COLOR_5};
                color: {config.TEXT_COLOR};
                overflow-x: hidden;
            }}

             /* Hero */
            .container {{
                width: 100%;
                max-width: 1120px;
                margin: 0 auto;
                padding: 0 20px;
            }}
            .hero {{
                padding: 84px 0 56px;
            }}
            .hero-grid {{
                display: grid;
                grid-template-columns: 0.75fr 1.25fr;
                gap: 28px;
                align-items: start;
            }}
            @media (max-width: 980px) {{
                .hero-grid {{grid - template - columns: 1fr; }}
            }}
            .headline {{
                font-size: clamp(48px, 7vw, 92px);
                line-height: 0.92;
                letter-spacing: -0.05em;
                font-weight: 800;
                margin: 18px 0 12px;
                color: rgba(248, 250, 252, 0.96);
            }}
            .headline-outline {{
                color: transparent;
                -webkit-text-stroke: 1px rgba(248, 250, 252, 0.35);
                text-stroke: 1px rgba(248, 250, 252, 0.35);
            }}
            .subhead {{
                font-size: 18px;
                line-height: 1.55;
                color: rgba(248, 250, 252, 0.72);
                max-width: 64ch;
                margin: 0 0 20px;
            }}
            .stats {{
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 12px;
                margin-top: 18px;
            }}
            @media (max-width: 700px) {{
                .stats {{grid - template - columns: 1fr; }}
            }}
            .stat {{
                padding: 14px 14px;
                border-radius: 16px;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.10);
            }}
            .stat-k {{
                font-size: 26px;
                font-weight: 800;
                letter-spacing: -0.03em;
                color: rgba(248, 250, 252, 0.96);
            }}
            .stat-l {{
                font-size: 12px;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                font-weight: 700;
                color: rgba(248, 250, 252, 0.55);
                margin-top: 3px;
            }}
            .side-card {{
                border-radius: 22px;
                padding: 16px;
                background: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.12);
            }}

            /* Profile card (hero left card) */
            .profile-card {{
                border-radius: 26px;
                padding: 18px;
                background: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.12);
                box-shadow: 0 22px 70px rgba(0, 0, 0, 0.45);
            }}
            .profile-photo {{
                width: 100%;
                aspect-ratio: 1 / 1;
                border-radius: 22px;
                border: 1px solid rgba(255, 255, 255, 0.14);
                overflow: hidden;
                background:
                    radial-gradient(circle at 30% 25%, rgba(34, 211, 238, 0.35), transparent 45%),
                    radial-gradient(circle at 70% 80%, rgba(124, 58, 237, 0.35), transparent 55%),
                    linear-gradient(135deg, rgba(255, 255, 255, 0.12), rgba(255, 255, 255, 0.02));
                position: relative;
            }}
            .profile-photo::after {{
                content: "";
                position: absolute;
                inset: 0;
                background:
                    radial-gradient(circle at 55% 35%, rgba(0, 0, 0, 0.50), transparent 55%),
                    radial-gradient(circle at 50% 120%, rgba(0, 0, 0, 0.65), transparent 55%);
                mix-blend-mode: overlay;
                pointer-events: none;
            }}
            .profile-name {{
                margin-top: 16px;
                font-size: 34px;
                line-height: 1.05;
                font-weight: 800;
                letter-spacing: -0.04em;
                color: rgba(248, 250, 252, 0.96);
            }}
            .profile-icon {{
                width: 36px;
                height: 36px;
                border-radius: 999px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                background: linear-gradient(135deg, var(--accent), var(--accent2));
                border: 1px solid rgba(255, 255, 255, 0.14);
                box-shadow: 0 18px 35px rgba(124, 58, 237, 0.22);
                margin: 14px auto 0;
            }}
            .profile-bio {{
                margin-top: 14px;
                text-align: center;
                font-size: 15px;
                line-height: 1.45;
                color: rgba(248, 250, 252, 0.66);
                padding: 0 10px;
            }}
            .socials {{
                display: flex;
                justify-content: center;
                gap: 14px;
                margin-top: 18px;
                padding-top: 14px;
                border-top: 1px solid rgba(255, 255, 255, 0.10);
            }}
            .social-link {{
                width: 38px;
                height: 38px;
                border-radius: 999px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.10);
                transition: transform 160ms ease, background 160ms ease, border-color 160ms ease;
            }}
            .social-link:hover {{
                transform: translateY(-1px);
                background: rgba(255, 255, 255, 0.08);
                border-color: rgba(124, 58, 237, 0.35);
            }}
            .social-link svg {{
                width: 18px;
                height: 18px;
                fill: rgba(248, 250, 252, 0.75);
            }}
            .social-link:hover svg {{
                fill: rgba(248, 250, 252, 0.92);
            }}

            /* Signature */
            .signature-wrap {{
                margin-top: 14px;
                padding-top: 14px;
                border-top: 1px dashed rgba(255, 255, 255, 0.12);
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 12px;
            }}
            .signature {{
                font-family: 'Dancing Script', 'Outfit', sans-serif;
                font-size: 26px;
                line-height: 1;
                color: rgba(248, 250, 252, 0.82);
                letter-spacing: -0.01em;
                transform: rotate(-1deg);
                white-space: nowrap;
            }}
            .signature-meta {{
                font-size: 11px;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                font-weight: 700;
                color: rgba(248, 250, 252, 0.55);
            }}
        </style>
    """)
    with ui.column().classes("w-full min-h-screen items-center"):
        yield
