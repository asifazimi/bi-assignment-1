import re
import pandas as pd


def normalize(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower().strip())


def match_games(steam, rawg):
    steam = steam.copy()
    rawg = rawg.copy()
    steam["match_key"] = steam["Name"].map(normalize)
    rawg["match_key"] = rawg["name"].map(normalize)

    steam = steam[steam["match_key"] != ""]
    rawg = rawg[rawg["match_key"] != ""]

    # many re-releases / DLCs share names; keep one row per side for now
    steam_d = steam.drop_duplicates("match_key", keep="first")
    rawg_d = rawg.drop_duplicates("match_key", keep="first")

    merged = steam_d.merge(
        rawg_d, on="match_key", how="inner", suffixes=("_steam", "_rawg"),
    )
    return merged, steam_d, rawg_d
