# YNAB-Automatic-Converter

Accelerate the conversion of .csv files to work with YNABs conventions.

Initially I wanted to write the entire script myself, but then I found out there already exists another [project](https://github.com/aniav/ynab-csv) that does exactly this.
See [Converter](https://aniav.github.io/ynab-csv/).

After using it for a while I found it cumbersome to always set the parameters manually for multiple different formats, so this project was born.

This script essentially navigates the website and sets all the specified parameters for you and downloads the file at the end.

## Setup
1. Install [python](https://www.python.org/downloads/)
2. Install [pip](https://pip.pypa.io/en/stable/installation/) (python package installer)
3. Clone this project
4. Go to the directory of the project with a terminal and run `python -m venv env` to create a python environment
5. Activate the environment - on Mac run `source env/bin/activate`, on Windows run `.\env\Scripts\activate`
6. Run this command `pip install -r requirements.txt` to install the dependencies of the project

Now you are all set to run the script file.

## Running the script
The command is the following:
```
python3 automate_ynab_csv.py /path/to/yourfile.csv /path/to/download_dir --start_row 10 --date_col_name "Date" --payee_col_name "Payee" --memo_col_name "Memo" --outflow_col_name "Outflow" --inflow_col_name "Inflow"
```

Make sure to know which columns of your .csv file will be used for the configuration of YNAB. You can also use the website to first see which strings you have to set.

## Multiple setups for different formats
What if you have different accounts that have different formats?
For this we can create separate files that run our scripts with the correct parameters.

### Mac and Linux
You can take a look at the `example_max_linus.sh` to see the setup.
1. Change the first line to reflect the path of where you created the environment.
2. Change all the parameters in the second line for your needs.
3. With an open terminal, navigate to the directory of your project.
4. Run `chmod +x example_max_linus.sh` (or the name of your custom .sh file) to make sure the file has permissions to be run.
5. Run the Bash script `./example_max_linus.sh`

### Windows
You can take a look at the `example_windows.bat` to see the setup. Open it with the note app to modify it.
1. Change the first line to reflect the path of where you created the environment.
2. Change all the parameters in the second line for your needs.
3. Just double click the file to run it.

