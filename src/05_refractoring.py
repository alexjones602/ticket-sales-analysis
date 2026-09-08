print("Refactored code for data cleaning and processing using pandas library.")
print("5.1 Refactored code for data cleaning")
import pandas as pd


def load_data(filepath):
    """Load a CSV file."""

    return pd.read_csv(filepath)


def clean_dates(df):
    """Convert event dates into a proper datetime format."""

    df["event_date"] = pd.to_datetime(
        df["event_date"],
        errors="coerce",
        dayfirst=True
    )

    return df


def clean_headliner(df):
    """Standardise headliner values to Yes or No."""

    df["headliner"] = (
        df["headliner"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df["headliner"] = df["headliner"].replace({
        "yes": "Yes",
        "y": "Yes",
        "no": "No",
        "n": "No"
    })

    df.loc[
        ~df["headliner"].isin(["Yes", "No"]),
        "headliner"
    ] = pd.NA

    return df


def clean_capacity(df):
    """Remove invalid negative capacity values."""

    df["capacity"] = pd.to_numeric(
        df["capacity"],
        errors="coerce"
    )

    df.loc[
        df["capacity"] < 0,
        "capacity"
    ] = pd.NA

    return df


def clean_tickets_sold(df):
    """Remove invalid negative ticket sales."""

    df["tickets_sold"] = pd.to_numeric(
        df["tickets_sold"],
        errors="coerce"
    )

    df.loc[
        df["tickets_sold"] < 0,
        "tickets_sold"
    ] = pd.NA

    return df


def clean_weather(df):
    """Standardise weather categories."""

    df["weather"] = (
        df["weather"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    df["weather"] = df["weather"].replace({
        "sun": "Sunny",
        "sunny": "Sunny",
        "sunshine": "Sunny",
        "rain": "Rain",
        "rainy": "Rain",
        "raining": "Rain",
        "cloud": "Cloudy",
        "cloudy": "Cloudy"
    })

    return df


def flag_capacity_errors(df):
    """Flag events where tickets sold exceeds capacity."""

    df["sales_exceed_capacity"] = (
        df["tickets_sold"] > df["capacity"]
    )

    return df   
def clean_days_advertised(df):
    """Convert days advertised to numeric and remove negative values."""

    df["days_advertised"] = pd.to_numeric(
        df["days_advertised"],
        errors="coerce"
    )

    df.loc[
        df["days_advertised"] < 0,
        "days_advertised"
    ] = pd.NA

    return df
def remove_duplicates(df):
    """Remove duplicate rows from the dataset."""

    df = df.drop_duplicates()

    return df
def clean_weather_clear(df):
    """Standardise weather categories."""

    df["weather"] = (
        df["weather"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    return df

def clean_data(df):
    """Run the complete data-cleaning process."""

    df = df.copy()


    df = clean_dates(df)
    df = clean_headliner(df)
    df = clean_capacity(df)
    df = clean_tickets_sold(df)
    df = clean_days_advertised(df)
    df = clean_weather(df)
    df = flag_capacity_errors(df)
    df = clean_days_advertised (df)
    df = remove_duplicates(df)
    df = clean_weather_clear(df)


    return df   
