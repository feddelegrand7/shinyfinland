from shiny import App, ui, render, reactive
from utilities import get_coffee_data

coffee_data = get_coffee_data()

app_ui = ui.page_fluid(
    ui.br(),
    ui.h2("Coffee Consumption in Finland"),
    ui.br(),
    ui.p("Finland drinks more coffee per person than any other country in the world."),
    ui.p("On average, a Finn drinks about 4 cups of coffee per day."),
    ui.br(),
    ui.input_slider("num_rows", "Number of rows to display:", min=1, max=20, value=5),
    ui.br(),
    ui.output_data_frame("coffee_tbl"),
    ui.br(),
    ui.h5("Data source: International Coffee Organization"),
    ui.br(),
    ui.input_action_button(id="display_contact_info", label="Contact Info"),
)


def server(input, output, session) -> None:
    @output
    @render.data_frame
    def coffee_tbl():
        return coffee_data.head(input.num_rows())

    @reactive.effect
    @reactive.event(input.display_contact_info)
    def _():
        modal = ui.modal(
            "Please contact Mohamed El Fodil Ihaddaden. ",
            "Only if it's good news ;)",
            title="Contact Information",
            easy_close=True,
        )

        ui.modal_show(modal)


app = App(app_ui, server)
