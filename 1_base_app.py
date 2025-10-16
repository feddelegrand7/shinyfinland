from shiny import App, ui

app_ui = ui.page_fluid(
    ui.br(),
    ui.h2("Coffee Consumption in Finland"),
    ui.br(),
    ui.p("Finland drinks more coffee per person than any other country in the world."),
    ui.p("On average, a Finn drinks about 4 cups of coffee per day."),
    ui.br(),
    ui.img(
        src="https://upload.wikimedia.org/wikipedia/commons/4/45/A_small_cup_of_coffee.JPG",
        alt="Cup of coffee",
        width="300",
        height="300",
    ),
    ui.br(),
    ui.p("Data source: International Coffee Organization"),
)


def server(input, output, session) -> None:
    return


app = App(app_ui, server)
