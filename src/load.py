from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "dataset"
STEAM_CSV = DATA_DIR / "steam-games.csv"
RAWG_CSV = DATA_DIR / "rawg-games-dataset.csv"

# steam header has 39 cols but rows have 40
# "DiscountDLC count" in header is really Discount + DLC count merged
STEAM_COLUMNS = [
    "AppID", "Name", "Release date", "Estimated owners", "Peak CCU",
    "Required age", "Price", "Discount", "DLC count", "About the game",
    "Supported languages", "Full audio languages", "Reviews", "Header image",
    "Website", "Support url", "Support email", "Windows", "Mac", "Linux",
    "Metacritic score", "Metacritic url", "User score", "Positive", "Negative",
    "Score rank", "Achievements", "Recommendations", "Notes",
    "Average playtime forever", "Average playtime two weeks",
    "Median playtime forever", "Median playtime two weeks",
    "Developers", "Publishers", "Categories", "Genres", "Tags",
    "Screenshots", "Movies",
]

# User score is ~all zero in this dataset, skip it
STEAM_USECOLS = [
    "AppID", "Name", "Release date", "Estimated owners", "Peak CCU",
    "Price", "DLC count", "Windows", "Mac", "Linux",
    "Metacritic score",
    "Average playtime forever", "Median playtime forever",
    "Genres", "Developers", "Publishers",
]

RAWG_USECOLS = [
    "id", "slug", "name", "released", "rating", "rating_top",
    "ratings_count", "reviews_text_count", "suggestions_count",
    "platforms", "genres", "developers", "publishers",
    "metacritic", "twitch_count", "playtime", "parent_platforms",
]


def load_steam():
    return pd.read_csv(
        STEAM_CSV,
        header=0,
        names=STEAM_COLUMNS,
        usecols=STEAM_USECOLS,
        low_memory=False,
    )


def load_rawg():
    return pd.read_csv(RAWG_CSV, usecols=RAWG_USECOLS, low_memory=False)
