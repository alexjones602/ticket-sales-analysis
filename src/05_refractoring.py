print("Refactored code for data cleaning and processing using pandas library")
print("Refactored code for data cleaning:")
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

print("Refactored functions for data analysis:")
def events_over_100_tickets(df):
    """Return events that sold more than 100 tickets."""

    result = df[df["tickets_sold"] > 100]

    return result

def highest_priced_event(df):
    """Return the event with the highest ticket price."""

    result = df.sort_values(
        "ticket_price",
        ascending=False
    ).head(1)

    return result
     
def average_attendance_by_venue(df):
    """Calculate average tickets sold by venue."""

    result = (
        df.groupby("venue")["tickets_sold"]
        .mean()
        .sort_values(ascending=False)
    )

    return result

def add_revenue(df):
    """Add estimated ticket revenue to the dataset."""

    df = df.copy()

    df["revenue"] = (
        df["tickets_sold"] *
        df["ticket_price"]
    )

    return df

def highest_revenue_event(df):
    """Return the event with the highest estimated ticket revenue."""

    df = add_revenue(df)

    result = df.sort_values(
        "revenue",
        ascending=False
    ).head(1)

    return result

def add_capacity_utilisation(df):
    """Add percentage of venue capacity sold."""

    df = df.copy()

    df["capacity_utilisation"] = (
        df["tickets_sold"] /
        df["capacity"]
    ) * 100

    return df   

def highest_capacity_utilisation(df):
    """Return the event with the highest capacity utilisation."""

    df = add_capacity_utilisation(df)

    result = df.sort_values(
        "capacity_utilisation",
        ascending=False
    ).head(1)

    return result

def sold_out_events(df):
    """Return events where ticket sales reached capacity."""

    result = df[
        df["tickets_sold"] >= df["capacity"]
    ]

    return result

def average_ticket_price(df):
    """Calculate the average ticket price."""

    return df["ticket_price"].mean()

def total_tickets_sold(df):
    """Calculate total tickets sold across all events."""

    return df["tickets_sold"].sum()