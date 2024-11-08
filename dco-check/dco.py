import os
import subprocess
import re
import tempfile
import shutil
import json
import urllib.request
import urllib.error
from typing import Dict
import pandas as pd
from dotenv import load_dotenv


def append_if_absent(user_map: Dict[str, list[object]], key: str, value: object):
    if key not in user_map:
        user_map[key] = []
    user_map[key].append(value)

def check_list_element_in_string(string: str, string_list: list) -> bool:
    return any(element.lower() in string.lower() for element in string_list)

def main():
    repos = []
    with open('repos.csv', 'r', encoding='utf-8') as f:
        text = f.read()
        lines = text.split('\n')
        for line in lines:
            spits = line.split(',')
            repos.append({
                'org': spits[0].strip(),
                'name': spits[1].strip(),
            })

    mail_ignored = []
    with open('mail-ignored.csv', 'r', encoding='utf-8') as f:
        text = f.read()
        lines = text.split('\n')
        for line in lines:
            mail_ignored.append(line.strip())


    user_map: Dict[str, list[object]] = {}

    for repo in repos:
        repo_input = f'https://github.com/{repo["org"]}/{repo["name"]}.git'

        # Store the original working directory
        original_cwd = os.getcwd()

        temp_dir = tempfile.mkdtemp()
        try:
            print(f"Cloning repository {repo['org']}/{repo['name']}...")
            subprocess.check_call(['git', 'clone', repo_input, temp_dir])
            repo_path = temp_dir
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
            shutil.rmtree(temp_dir)
            return

        try:
            # Change the current working directory to the repository path
            os.chdir(repo_path)
            # Git log command to retrieve commit information
            git_log_cmd = [
                'git',
                'log',
                '--pretty=format:%H%x1f%an%x1f%ad%x1f%ae%x1f%B%x1e',
                '--date=iso'
            ]
            # Execute the git log command
            output = subprocess.check_output(git_log_cmd)
            # Decode the output to a string
            output = output.decode('utf-8', errors='replace')
            # Split the output into individual commits
            commits = output.strip().split('\x1e')


            for commit in commits:
                commit = commit.strip()
                if not commit:
                    continue
                # Split the commit into fields
                fields = commit.strip().split('\x1f')
                if len(fields) < 5:
                    print("Malformed commit data, skipping.")
                    continue
                commit_hash, author_name, commit_date, author_email, commit_message = fields
                # Check if the commit message contains a "Signed-off-by" line

                if check_list_element_in_string(author_email.strip(), mail_ignored):
                    continue

                if not re.search(r'^Signed-off-by: .+', commit_message, re.MULTILINE):
                    # Add the commit to the list of non-DCO commits
                    commit_obj = {
                        'email': author_email,
                        'author': author_name,
                        'date': commit_date,
                        'repo': f'{repo["org"]}/{repo["name"]}',
                        'github_username': None,
                        'link': f'https://github.com/{repo["org"]}/{repo["name"]}/commit/{commit_hash}',
                        'hash': commit_hash
                    }
                    append_if_absent(user_map, author_email, commit_obj)
            # Change back to the original directory before writing the output file
            os.chdir(original_cwd)
        finally:
            shutil.rmtree(temp_dir)

    if len(user_map.values()) > 0:
        for email in user_map.keys():
            print(f'No sign-off found for author: {email}')
            github_user = get_github_username(user_map[email][0]['repo'], user_map[email][0]['hash'], os.getenv('GITHUB_TOKEN'))
            if github_user:
                other_email = None
                if "github" in email:
                    other_email = get_github_username(email, os.getenv('GITHUB_TOKEN'))

                for commit in user_map[email]:
                    commit["github_username"] = github_user
                    if other_email:
                        commit["email"] = other_email


        # Write Excel-File
        with pd.ExcelWriter("output.xlsx") as writer:
            summary_data = [{"email": email, "link": record["link"]} for email, records in user_map.items() for record in
                             records]
            overview_df = pd.DataFrame(summary_data)
            # Übersichtstabelle in ein separates Arbeitsblatt schreiben
            overview_df.to_excel(writer, sheet_name="Summary", index=False)

            for i, records in enumerate(user_map.values(), start=1):
                df = pd.DataFrame(records)
                sheet_name = f"E-Mail {i}"
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        print("Success: results in output.xlsx")


def get_github_username(repo, commit_hash, github_token=None):
    # Use the GitHub API to get the commit information
    api_url = f'https://api.github.com/repos/{repo}/commits/{commit_hash}'
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'non-dco-script'
    }
    if github_token:
        headers['Authorization'] = f'token {github_token}'
    try:
        request = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(request) as response:
            if response.status == 200:
                commit_data = json.loads(response.read().decode())
                if 'author' in commit_data and commit_data['author'] is not None:
                    return commit_data['author']['login']
                else:
                    return None
            else:
                print(f"GitHub API error: {response.status} {response.reason}")
                return None
    except urllib.error.HTTPError as e:
        print(f"GitHub API error: {e.code} {e.reason}")
        return None
    except Exception as e:
        print(f"Error fetching GitHub username: {e}")
        return None

def get_github_user_email(username, github_token):
    # Use the GitHub API to get the commit information
    api_url = f'https://api.github.com/users/{username}'
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'non-dco-script',
        'Authorization': f'token {github_token}'
    }

    try:
        request = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(request) as response:
            if response.status == 200:
                user_data = json.loads(response.read().decode())
                if 'email' in user_data and user_data['email'] is not None:
                    return user_data['email']
                else:
                    return None
            else:
                print(f"GitHub API error: {response.status} {response.reason}")
                return None
    except urllib.error.HTTPError as e:
        print(f"GitHub API error: {e.code} {e.reason}")
        return None
    except Exception as e:
        print(f"Error fetching GitHub user mail: {e}")
        return None


if __name__ == '__main__':
    load_dotenv()
    main()
