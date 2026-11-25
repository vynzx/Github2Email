import requests, click, re
from colorama import Fore as f 

@click.command()
@click.argument("username")
def findemail(username):
    click.echo(f.GREEN + 
    r"""
  ______ _      _           _    ______  _______             _ _ 
 / _____|_)_   | |         | |  (_____ \(_______)           (_) |
| /  ___ _| |_ | | _  _   _| | _  ____) )_____   ____   ____ _| |
| | (___) |  _)| || \| | | | || \/_____/|  ___) |    \ / _  | | |
| \____/| | |__| | | | |_| | |_) )______| |_____| | | ( ( | | | |
 \_____/|_|\___)_| |_|\____|____(_______)_______)_|_|_|\_||_|_|_|
                                                                 
Find the email address of a github user.
    """)
    try:
     # Fetch repos
     repos = requests.get(f"https://api.github.com/users/{username}/repos").json()
     for repo in repos:
        # Fetch Commits
        commits = requests.get(
            f"https://api.github.com/repos/{username}/{repo['name']}/commits"
        ).json()
        for commit in commits:
            # Fetch the author of the commit
            author = commit.get("author")
            # If the author is the target
            if author["login"].lower() == username.lower():
                # Fetch email
                email = commit["commit"]["author"].get("email")

                if email:
                    print(f.GREEN + "[+] Public email:", email)

    except Exception as e:
        print(f.RED + "[!] ERROR", e)

if __name__ == "__main__":
    findemail()
