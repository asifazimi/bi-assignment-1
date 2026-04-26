import time
import pandas as pd

from src.load import load_steam, load_rawg
from src.integrate import match_games


def summarize(df, name):
    print(f"\n--- {name} ---")
    print(f"rows: {len(df):,}  cols: {df.shape[1]}")
    mb = df.memory_usage(deep=True).sum() / 1024**2
    print(f"mem:  {mb:.1f} MB")
    print("\ndtypes:")
    print(df.dtypes.to_string())

    nulls = df.isna().sum()
    nulls = nulls[nulls > 0].sort_values(ascending=False)
    print("\nnulls:")
    if nulls.empty:
        print("  none")
    else:
        for col, n in nulls.items():
            print(f"  {col}: {n:,} ({100 * n / len(df):.1f}%)")


def years(steam, rawg):
    sy = pd.to_datetime(steam["Release date"], errors="coerce").dt.year
    ry = pd.to_datetime(rawg["released"], errors="coerce").dt.year
    print("\n--- release years ---")
    print(f"steam unparsed: {sy.isna().sum():,}")
    print(f"rawg  unparsed: {ry.isna().sum():,}")
    vc = sy.value_counts().sort_index()
    print("\nsteam earliest/latest 3:")
    print(vc.head(3).to_string())
    print(vc.tail(3).to_string())


def match_report(steam, rawg):
    print("\n--- matching on normalized name ---")
    t = time.perf_counter()
    merged, steam_d, rawg_d = match_games(steam, rawg)
    print(f"  {time.perf_counter() - t:.1f}s")

    print(f"steam rows (raw):      {len(steam):,}")
    print(f"steam rows (dedup):    {len(steam_d):,}  (lost {len(steam) - len(steam_d):,} dup names)")
    print(f"rawg  rows (raw):      {len(rawg):,}")
    print(f"rawg  rows (dedup):    {len(rawg_d):,}  (lost {len(rawg) - len(rawg_d):,} dup names)")
    print(f"matched (inner join):  {len(merged):,}")
    print(f"  {100 * len(merged) / len(steam_d):.1f}% of steam, "
          f"{100 * len(merged) / len(rawg_d):.1f}% of rawg")

    cols = [
        "rating", "ratings_count", "suggestions_count", "metacritic",
        "twitch_count", "playtime", "genres", "platforms",
        "reviews_text_count",
    ]
    print("\nfill rates in matched subset (RAWG cols):")
    for c in cols:
        if c in merged.columns:
            nn = merged[c].notna().sum()
            print(f"  {c:<22} {nn:>7,}  ({100 * nn / len(merged):5.1f}%)")

    print("\nfill rates in matched subset (Steam cols):")
    for c in ["Metacritic score", "User score", "Genres", "Price", "Estimated owners"]:
        if c in merged.columns:
            if merged[c].dtype.kind in "if":
                nn = (merged[c] > 0).sum()
                print(f"  {c:<22} {nn:>7,}  ({100 * nn / len(merged):5.1f}%) nonzero")
            else:
                nn = merged[c].notna().sum()
                print(f"  {c:<22} {nn:>7,}  ({100 * nn / len(merged):5.1f}%) notna")

    return merged


def main():
    t0 = time.perf_counter()

    print("loading steam...")
    t = time.perf_counter()
    steam = load_steam()
    print(f"  {time.perf_counter() - t:.1f}s")
    summarize(steam, "Steam")

    print("\nloading rawg...")
    t = time.perf_counter()
    rawg = load_rawg()
    print(f"  {time.perf_counter() - t:.1f}s")
    summarize(rawg, "RAWG")

    years(steam, rawg)
    match_report(steam, rawg)

    print(f"\ndone in {time.perf_counter() - t0:.1f}s")


if __name__ == "__main__":
    main()
