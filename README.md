## Collaboration method for processing the survey data

1. Clone this repo
2. Download the spreadsheet `definitely-final-results-for-satre-tre-op-2023-05-16-1359.xlsx` from the private SATRE filestore and put it in the the local copy of the repo
3. Build the conda environment
4. Use `load_survey_data.load_data` to get a dataframe that can be easily used for further manipulations (see `summary-so-far.ipynb`)
5. Run `pre-commit install` in the local copy of the repo to ensure the git hook for stripping notebook output is installed. Note that it operates on `git commit`, and removes all output from the local copy of the notebook

## Data files

The original survey results contain sensitive data, but a sanitised version is available:

- [`data/public-results-for-satre-tre-op-2023-05-16-1359.csv`](data/public-results-for-satre-tre-op-2023-05-16-1359.csv) contains the ranked answers from the survey, along with:
  - manually categorised roles and institutions types
  - extracted tokenised answers for some free text questions (e.g. software packages) using [`categorical_free_text.ipynb`](categorical_free_text.ipynb)
- [`data/free-text-summaries.md`](data/free-text-summaries.md) contains a manual summary of the remaining collated free text answers
