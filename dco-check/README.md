# Non-DCO Commit Checker

This Python script identifies GitHub commits missing a “Signed-off-by” signature, highlighting commits that lack compliance with Developer Certificate of Origin (DCO) practices. The script clones repositories listed in a CSV file, analyzes commit history, and produces an Excel report with non-compliant commit details.

## Prerequisites

* Python 3.8+
* Git installed and configured
* GitHub token for API access (stored in `.env` as `GITHUB_TOKEN`)
* CSV files repos.csv and mail-ignored.csv

Install the libraries using:
```bash
pip install -r requirements.txt
```

## File Descriptions
### `repos.csv`
In this file add a list of all repos you want to scan. The format is `org`,`repo` eg. 
```
hiero-ledger,hiero
hiero-ledger,repo2
```
> [!WARNING]  
> The file should not have any empty lines

### `mail-ignored.csv` 

Lists emails to be ignored in the DCO check, one email per line.

> [!WARNING]  
> The file should not have any empty lines

## Setup

1. Clone this repository.
2. Create a `.env` file and add your GitHub token
3. Ensure `repos.csv` and `mail-ignored.csv` are filled correctly.

## Usage

Run the script with:
```bash
python3 dco.py
```


## Workflow

1.	Load Repository and Email Data: The script loads repository information from repos.csv and ignored email addresses from `mail-ignored.csv`.
2.	Clone and Analyze Commits:
      - Clones each repository into a temporary directory.
      - Executes `git log` to retrieve commit history.
      - Identifies commits missing the “Signed-off-by” line, ignoring commits by authors listed in `mail-ignored.csv`.
3. Fetch GitHub Usernames:
      - If a non-compliant commit is found, the script queries the GitHub API for the author’s username.
4. Generate Excel Report:
      - Saves non-compliant commit details in output.xlsx, with separate sheets for each author.

## Output

The Excel file `output.xlsx` contains:
* Summary sheet with links to each non-compliant commit.
* Separate sheets for each non-compliant author’s commits.

## Notes
Ensure API rate limits are managed by adding a GitHub token to the `.env` file.
