from shiny import App, ui, render, reactive
import seaborn as sns
import matplotlib.pyplot as plt
from utilities import get_coffee_data
import pandas as pd

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
    ui.row(
        ui.column(
            12, ui.card(ui.h3("Coffee Data Table"), ui.output_data_frame("coffee_tbl"))
        )
    ),
    ui.row(
        ui.column(
            6,
            ui.card(
                ui.h3("Coffee Consumption Pie Plot"), ui.output_plot("coffee_pie_plot")
            ),
        ),
        ui.column(
            6,
            ui.card(ui.h3("Coffee Consumption Barplot"), ui.output_plot("coffee_plot")),
        ),
    ),
    ui.br(),
    ui.h5("Data source: International Coffee Organization"),
    ui.br(),
    ui.input_action_button(id="refresh", label="Refresh"),
)


def server(input, output, session) -> None:
    coffee_data = reactive.Value(pd.DataFrame())

    @reactive.effect
    @reactive.event(input.refresh)
    def _():
        df = get_coffee_data().head(input.num_rows())
        coffee_data.set(df)

    @output
    @render.data_frame
    def coffee_tbl():
        if coffee_data().shape[0] == 0:
            return None
        return coffee_data()

    @output
    @render.plot
    def coffee_plot():
        if coffee_data().shape[0] == 0:
            return

        sns.barplot(
            data=coffee_data(),
            x="cups_per_year",
            y="country",
            palette="viridis",
        )
        plt.title("Coffee Consumption by Country")
        plt.xlabel("Cups per Year")
        plt.ylabel("Country")

    @output
    @render.plot
    def coffee_pie_plot():
        if coffee_data().shape[0] == 0:
            return

        df = coffee_data()
        plt.pie(
            df["cups_per_year"],
            labels=df["country"],
            autopct="%1.1f%%",
            startangle=140,
        )
        plt.title("Share of Coffee Consumption by Country")


app = App(app_ui, server)
