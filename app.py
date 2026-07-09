from git import Repo
import os
from config import REPO_URL
import traceback

repo_url = REPO_URL
repo_name = repo_url.split("/")[-1].replace(".git", "")
print(f"repo url ===> {repo_url}")
local_repo = os.path.join("repository", repo_name)

try: 
    repo = Repo.clone_from(repo_url, local_repo, branch = "master", single_branch = True)
    print(f"Repo cloned successfully! ===> {repo}")
    print(f"GIT STATUS ===> {repo.git.status()}")
    print(os.listdir(local_repo))

except Exception as e:
    print(e)
    traceback.print_exc() 
