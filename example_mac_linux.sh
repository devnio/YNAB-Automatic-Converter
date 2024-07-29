#!/bin/bash
source /path/to/your/project/venv/bin/activate
python3 automate_ynab_csv.py /path/to/yourfile.csv /path/to/download_dir --start_row 10 --date_col_name "Date" --payee_col_name "Payee" --memo_col_name "Memo" --outflow_col_name "Outflow" --inflow_col_name "Inflow"