from shiny import App, ui, render
from utilities import get_coffee_data

coffee_data = get_coffee_data()

app_ui = ui.page_fluid(
    ui.br(),
    ui.h2("Coffee Consumption in Finland"),
    ui.hr(),
    ui.p("Finland drinks more coffee per person than any other country in the world."),
    ui.p("On average, a Finn drinks about 4 cups of coffee per day."),
    ui.hr(),
    ui.output_data_frame("coffee_tbl"),
    ui.hr(),
    ui.h5("Data source: International Coffee Organization"),
)


def server(input, output, session) -> None:
    @output
    @render.data_frame
    def coffee_tbl():
        return coffee_data.head(10)


app = App(app_ui, server)
