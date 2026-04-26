import pandas as pd


def clean(merged):
    out = pd.DataFrame()

    out["app_id"] = merged["AppID"]
    out["steam_name"] = merged["Name"]
    out["rawg_name"] = merged["name"]
    out["matched_name"] = merged["match_key"]

    steam_date = pd.to_datetime(merged["Release date"], errors="coerce")
    rawg_date = pd.to_datetime(merged["released"], errors="coerce")
    out["release_date"] = steam_date.fillna(rawg_date)
    out["release_year"] = out["release_date"].dt.year.astype("Int64")
    out["release_month"] = out["release_date"].dt.month.astype("Int64")

    # rawg platforms looks like "PC|macOS|Linux"
    plats = merged["platforms"].fillna("")
    out["pc_only"] = plats == "PC"

    out["price"] = merged["Price"]
    out["average_playtime"] = merged["Average playtime forever"].astype("Int64")
    out["median_playtime"] = merged["Median playtime forever"].astype("Int64")

    out["rating"] = merged["rating"]
    out["ratings_count"] = merged["ratings_count"].astype("Int64")
    out["suggestions_count"] = merged["suggestions_count"].astype("Int64")

    # unify genres: steam uses commas, rawg uses pipes. normalize to pipe-separated
    g_steam = merged["Genres"].fillna("").str.replace(",", "|")
    g_rawg = merged["genres"].fillna("").str.replace(",", "|")
    out["genres"] = g_steam.where(g_steam != "", g_rawg)

    return out
