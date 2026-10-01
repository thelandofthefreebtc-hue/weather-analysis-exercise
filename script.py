#!/usr/bin/env python

from pathlib import Path

import pandas as pd

from plotting import plot_temperature_and_precipitation


DATA_FILE = Path("weather_data.csv")
OUTPUT_DIRECTORY = Path("figures")
MONTHS = ("2024-01", "2024-02", "2024-03")


def load_weather_data(filename):
    """Read the weather data and create a datetime index."""

    data = pd.read_csv(filename)

    data["recorded_at"] = pd.to_datetime(
        data["date"] + " " + data["time"]
    )

    return data.set_index("recorded_at")


def get_month_data(data, month):
    """Return the records belonging to one month."""

    return data.loc[month]


def main():
    """Load the data and create monthly weather plots."""

    data = load_weather_data(DATA_FILE)

    for month in MONTHS:
        month_data = get_month_data(data, month)

        plot_temperature_and_precipitation(
            month_data,
            month,
            OUTPUT_DIRECTORY,
        )


if __name__ == "__main__":
    main()

