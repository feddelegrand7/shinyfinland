import pandas as pd


def get_coffee_data() -> pd.DataFrame:
    data = {
        "country": [
            "Finland",
            "Norway",
            "Iceland",
            "Denmark",
            "Netherlands",
            "Sweden",
            "Switzerland",
            "Belgium",
            "Luxembourg",
            "Canada",
            "Austria",
            "Germany",
            "France",
            "United States",
            "United Kingdom",
            "Brazil",
            "Japan",
            "Italy",
            "Spain",
            "South Korea",
        ],
        "cups_per_year": [
            1200,
            1100,
            1000,
            950,
            900,
            850,
            800,
            750,
            700,
            650,
            600,
            550,
            500,
            450,
            400,
            350,
            300,
            250,
            200,
            150,
        ],
    }

    df = pd.DataFrame(data)
    return df
