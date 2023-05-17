## Collaboration method for processing the survey data

1. Clone this repo
2. Download the latest spreadsheet from [sharepoint](https://dmail.sharepoint.com/:f:/r/sites/SATRE/Shared%20Documents/WP1%20-%20Design/[wip](https://dmail.sharepoint.com/:f:/r/sites/SATRE/Shared%20Documents/WP1%20-%20Design/wip?csf=1&web=1&e=baCrJ9)?csf=1&web=1&e=baCrJ9) and put it in the the local copy of the repo
3. Build the conda environment
4.  Use `load_survey_data.load_data` to get a dataframe that can be easily used for further manipulations (see `summary-so-far.ipynb`)
5. Run `pre-commit install` in the local copy of the repo to ensure the git hook for stripping notebook output is installed. Note that it operates on `git commit`, and removes all output from the local copy of the notebook