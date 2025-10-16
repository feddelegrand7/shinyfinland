from shiny import App, ui, render, reactive
import seaborn as sns
import matplotlib.pyplot as plt
from time import sleep
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
    ui.layout_columns(
        ui.card(ui.h3("Coffee Data Table"), ui.output_data_frame("coffee_tbl")),
        ui.card(ui.h3("Coffee Consumption Barplot"), ui.output_plot("coffee_plot")),
        col_widths=[6, 6],
    ),
    ui.br(),
    ui.h5("Data source: International Coffee Organization"),
    ui.br(),
    ui.input_action_button(id="display_contact_info", label="Contact Info"),
)


def server(input, output, session) -> None:
    @output
    @render.data_frame
    def coffee_tbl():
        sleep(1)
        return coffee_data.head(input.num_rows())

    @output
    @render.plot
    def coffee_plot():
        sleep(1)
        sns.barplot(
            data=coffee_data.head(input.num_rows()),
            x="cups_per_year",
            y="country",
            palette="viridis",
        )
        plt.title("Coffee Consumption by Country")
        plt.xlabel("Cups per Year")
        plt.ylabel("Country")


app = App(app_ui, server)
