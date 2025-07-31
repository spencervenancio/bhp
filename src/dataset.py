from pathlib import Path

from loguru import logger
import pandas as pd
import typer

from src.config import (
    COLLEGE_SCORECARD,
    INTERIM_DATA_DIR,
    STD_COLS,
)

app = typer.Typer()


FIRST_YEAR = 1996
LATEST_YEAR = 2023


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APROPRIATE ----
    input_dir: Path = COLLEGE_SCORECARD,
    output_path: Path = INTERIM_DATA_DIR / "tuition.csv",
    # ----------------------------------------------
):
    columns = ["UNITID", "INSTNM", "TUITIONFEE_IN", "TUITIONFEE_OUT"]

    all_data = None
    for year in range(FIRST_YEAR, LATEST_YEAR):
        file_path = input_dir / f"MERGED{year}_{str(year + 1)[-2:]}_PP.csv"
        if not file_path.exists():
            logger.warning(f"File {file_path} does not exist.")
            # continue
        logger.info(f"Processing data for year {year}...")

        df = pd.read_csv(file_path, usecols=columns)
        df["year"] = year

        df.rename(columns=STD_COLS, inplace=True)
        if year == FIRST_YEAR:
            all_data = df
        else:
            all_data = pd.concat([all_data, df], ignore_index=True)

    all_data.dropna(subset=["tuition_in", "tuition_out"], inplace=True)
    all_data.to_csv(output_path, index=False)
    logger.info(f"Data saved to {output_path}")


if __name__ == "__main__":
    app()
