from pathlib import Path
import time

from src.load import load_steam, load_rawg
from src.integrate import match_games
from src.clean import clean
from src.build_star import build_star

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
STAR_DIR = OUTPUT_DIR / "star"


def main():
    t0 = time.perf_counter()

    print("loading...")
    steam = load_steam()
    rawg = load_rawg()

    print("matching...")
    merged, _, _ = match_games(steam, rawg)
    print(f"  matched rows: {len(merged):,}")

    print("cleaning...")
    cleaned = clean(merged)

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "matched_clean.csv"
    cleaned.to_csv(out_path, index=False)
    print(f"  saved: {out_path}  ({len(cleaned):,} rows, {cleaned.shape[1]} cols)")

    print("building star schema...")
    tables = build_star(cleaned, STAR_DIR)
    for name, df in tables.items():
        print(f"  {name:20s} {len(df):>7,} rows")
    print(f"  saved to: {STAR_DIR}")

    print(f"\ntime: {time.perf_counter() - t0:.1f}s")


if __name__ == "__main__":
    main()
