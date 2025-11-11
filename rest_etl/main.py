import csv, pathlib, logging
from typing import List
import typer

app = typer.Typer(add_completion=False)
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

@app.command()
def transformar(entrada: str, salida: str):
    """Lee un CSV y genera otro normalizado (demo ETL sin Internet)."""
    in_path = pathlib.Path(entrada); out_path = pathlib.Path(salida)
    if not in_path.exists():
        logging.error("No encuentro el archivo: %s", entrada); raise SystemExit(1)

    with in_path.open(newline="", encoding="utf-8") as fin, out_path.open("w", newline="", encoding="utf-8") as fout:
        reader = csv.DictReader(fin)
        campos: List[str] = [c.strip() for c in (reader.fieldnames or [])]
        writer = csv.DictWriter(fout, fieldnames=campos); writer.writeheader()
        for row in reader:
            row = {k.strip(): (v.strip().title() if isinstance(v, str) else v) for k, v in row.items()}
            writer.writerow(row)

    logging.info("Archivo generado: %s", out_path)

if __name__ == "__main__":
    app()
