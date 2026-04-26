from pathlib import Path
import pandas as pd


def build_star(cleaned: pd.DataFrame, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    # DimGame: one row per matched game, keyed on app_id
    dim_game = cleaned[["app_id", "steam_name", "rawg_name", "matched_name", "pc_only"]].copy()
    dim_game = dim_game.rename(columns={"app_id": "game_id"}).drop_duplicates("game_id")

    # DimDate: one row per distinct release_date
    dates = cleaned[["release_date", "release_year", "release_month"]].dropna(subset=["release_date"])
    dim_date = dates.drop_duplicates("release_date").sort_values("release_date").reset_index(drop=True)
    dim_date = dim_date.rename(columns={"release_date": "release_date", "release_year": "year", "release_month": "month"})
    dim_date.insert(0, "date_id", range(1, len(dim_date) + 1))

    # DimGenre: one row per distinct genre across all games
    exploded = (
        cleaned.assign(genre=cleaned["genres"].fillna("").str.split("|"))
        .explode("genre")
    )
    exploded["genre"] = exploded["genre"].str.strip()
    exploded = exploded[exploded["genre"] != ""]

    dim_genre = (
        pd.DataFrame({"genre_name": sorted(exploded["genre"].unique())})
        .reset_index(drop=True)
    )
    dim_genre.insert(0, "genre_id", range(1, len(dim_genre) + 1))

    # BridgeGameGenre: many-to-many between game and genre
    genre_lookup = dict(zip(dim_genre["genre_name"], dim_genre["genre_id"]))
    bridge = pd.DataFrame({
        "game_id": exploded["app_id"].values,
        "genre_id": exploded["genre"].map(genre_lookup).values,
    }).drop_duplicates().reset_index(drop=True)

    # FactGame: one fact per game, with FKs to DimGame and DimDate
    date_lookup = dict(zip(dim_date["release_date"], dim_date["date_id"]))
    fact = pd.DataFrame({
        "game_id": cleaned["app_id"].values,
        "date_id": cleaned["release_date"].map(date_lookup).astype("Int64").values,
        "price": cleaned["price"].values,
        "average_playtime": cleaned["average_playtime"].values,
        "median_playtime": cleaned["median_playtime"].values,
        "rating": cleaned["rating"].values,
        "ratings_count": cleaned["ratings_count"].values,
        "suggestions_count": cleaned["suggestions_count"].values,
    })
    fact.insert(0, "fact_id", range(1, len(fact) + 1))

    dim_game.to_csv(out_dir / "dim_game.csv", index=False)
    dim_date.to_csv(out_dir / "dim_date.csv", index=False)
    dim_genre.to_csv(out_dir / "dim_genre.csv", index=False)
    bridge.to_csv(out_dir / "bridge_game_genre.csv", index=False)
    fact.to_csv(out_dir / "fact_game.csv", index=False)

    return {
        "dim_game": dim_game,
        "dim_date": dim_date,
        "dim_genre": dim_genre,
        "bridge_game_genre": bridge,
        "fact_game": fact,
    }
