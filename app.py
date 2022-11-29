import dash
from dash import html, dcc, Input, Output, State, html
import dash_bootstrap_components as dbc
from dash import page_registry, page_container

from dash_extensions.enrich import (
    DashProxy,
    MultiplexerTransform,
    html,
    dcc,
)

external_stylesheets = [dbc.themes.JOURNAL]

app = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    use_pages=True,
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)

server = app.server

GENLAC_LOGO = "/assets/genlac.png"

dropdown = dbc.Row([
    dbc.Col(
        dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Gaps between spouses", header=True),
            dbc.DropdownMenuItem("Age difference between spouses", href="/"),
            dbc.DropdownMenuItem("Education difference between spouses", href="/diferencia-educativa"),
            dbc.DropdownMenuItem("Difference in hours worked between spouses", href="/diferencia-horas"),
            dbc.DropdownMenuItem("Percentage of the spousal labor income contributed by each member", href="/porcen-ingreso-pareja"),
            dbc.DropdownMenuItem("Percentage of individuals with equal or greater education than spouse who are inactive", href="/porcentaje-mas-educacion"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Autonomía", header=True),
            dbc.DropdownMenuItem("Percentage of adults with zero income", href="/autonomia"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Household structure and headship", header=True),
            dbc.DropdownMenuItem("Self-reported female household headship", href="/jefatura-hogar-auto"),
            dbc.DropdownMenuItem("Economic female household headship", href="/jefatura-hogar-econ"),
            dbc.DropdownMenuItem("Percentage of single-parent households", href="/porcen-hog-mono"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Time use", header=True),
            dbc.DropdownMenuItem("Participation in household chores", href="/household-chores"),
            dbc.DropdownMenuItem("Weekly hours allocated to household chores", href="/hours-household-chores"),
            dbc.DropdownMenuItem("Participation in care activities", href="/care-activities"),
            dbc.DropdownMenuItem("Weekly hours allocated to care activities", href="/hours-care-activities"),
            dbc.DropdownMenuItem("Participation in childcare activities", href="/childcare-activities"),
            dbc.DropdownMenuItem("Weekly hours allocated to childcare activities", href="/hours-childcare-activities"),
            dbc.DropdownMenuItem("Participation in activities of support to other households", href="/activities-support"),
            dbc.DropdownMenuItem("Weekly hours allocated to provide support to other households", href="/hours-activities-support"),
            dbc.DropdownMenuItem("Participation in leisure activities", href="/activities-leisure"),
            dbc.DropdownMenuItem("Weekly hours allocated to leisure activities", href="/hours-activities-leisure"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Fertility", header=True),
            dbc.DropdownMenuItem("Fertility rate", href="/fertility-rate"),
            dbc.DropdownMenuItem("Desired fertility rate", href="/desired-fertility-rate"),
            dbc.DropdownMenuItem("Gap between actual and desired fertility", href="/gap-fertility-desired"),
            dbc.DropdownMenuItem("Gap in desired fertility between spouses", href="/gap-fertility-desired-spouse"),
            dbc.DropdownMenuItem("Percentage of women using contraception (any method)", href="/method-contraception"),
            dbc.DropdownMenuItem("Percentage of women using modern contraceptive methods", href="/modern-contraception-method"),
            dbc.DropdownMenuItem("Percentage of women without access to contraception", href="/without-contraception-access"),
            dbc.DropdownMenuItem("Early pregnancy", href="/early-pregnancy"),
            dbc.DropdownMenuItem("Early marriage", href="/early-marriage"),
        ],
        size="lg",
        nav=True,
        in_navbar=True,
        label="Indicators",
        className="ms-0",
        toggle_style={"color": "#460074"},
        align_end=False,
        style={'width':'100%'}

        )
    )
],
className="g-0 ms-auto flex-nowrap mt-5 mt-md-0",
align="center",
)


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                            dropdown, 
                            className="ml-auto",
                            id="navbar-collapse",
                            is_open=False,
                            navbar=True,
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
        ],
    fluid=True),
    #outline=True, 
    color="light",
    dark=True,
)
# Definimos el layout:
app.layout = html.Div(
    [
        dcc.Store(id="store", data='Argentina'),
        dbc.Container([
    dbc.Row(
        [
            navbar # Navbar
        ]
    ),
    html.Br(),        
    dbc.Row(
        [
            dash.page_container # Contenido de cada pagina
        ]
    )
], fluid=True)
    ]
)


if __name__ == "__main__":
    app.run_server()