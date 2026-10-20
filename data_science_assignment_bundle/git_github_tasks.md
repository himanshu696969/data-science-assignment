# Git and GitHub Tasks — Commands and Evidence

Replace `YOUR-USERNAME` and example email/name with your actual GitHub details. Commands that push require a GitHub repository and authentication.

## Install and configure Git

```powershell
git --version
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
git config --global --list
```

## music-recommendation local folder → foodie-favorites remote

Create an empty GitHub repository named `foodie-favorites`, then run:

```powershell
mkdir "$HOME\Desktop\music-recommendation"
cd "$HOME\Desktop\music-recommendation"
git init
git branch -M main
"# Music Recommendation" | Set-Content README.md
git add README.md
git commit -m "Initial commit for music-recommendation project"
git remote add origin https://github.com/YOUR-USERNAME/foodie-favorites.git
git push -u origin main
```

Append a `Top 3 Music Apps` section to README, commit, and push. Then create a GitHub Issue titled `Add playlist sharing`. Suggested issue: “Allow users to share playlists with friends using a shareable link.”

## InstaCloneRepo and clone check

```powershell
mkdir "$HOME\Desktop\InstaCloneRepo"
cd "$HOME\Desktop\InstaCloneRepo"
git init
Get-ChildItem -Force
cd "$HOME\Desktop"
git clone https://github.com/public-apis/public-apis.git
cd public-apis
git status
```

Expected observation immediately after clone: normally the working tree is clean. Record the branch and exact status displayed on your system.

Create a playlist file inside `InstaCloneRepo` and commit it:

```powershell
cd "$HOME\Desktop\InstaCloneRepo"
@"
Blinding Lights - The Weeknd
Shape of You - Ed Sheeran
Believer - Imagine Dragons
"@ | Set-Content playlist.txt
git add playlist.txt
git commit -m "Add initial playlist with 3 songs"
```

## Branch and merge conflict practice

Use a test repository with a `main` branch. Create `feature-playlist`, add `playlist.md`, and commit it. Add a separate commit on `main`, then run:

```powershell
git switch main
git merge --no-ff feature-playlist -m "Merge feature-playlist into main"
```

To practice a conflict, change the same line of `playlist.md` differently on `main` and `feature-playlist`, committing each change. Then merge the feature branch into `main`. Open the file in VS Code, resolve conflict markers, save, and run:

```powershell
git add playlist.md
git commit -m "Resolve playlist title merge conflict"
git status
```

## Fork and Pull Request

1. Visit https://github.com/public-apis/public-apis and click Fork.
2. Clone your fork and create the requested branch:

```powershell
git clone https://github.com/YOUR-USERNAME/public-apis.git
cd public-apis
git switch -c feature-zomato-analysis
"Analyze Zomato orders for popular cuisines, peak order times, delivery delays, and ratings." | Set-Content zomato_analysis.txt
git add zomato_analysis.txt
git commit -m "Add Zomato order analysis proposal"
git push -u origin feature-zomato-analysis
```

3. On GitHub, open a Pull Request with the original repository as the base repository, if contributions are accepted. Request a classmate review where available. Do not claim a PR was opened until you have done so.

Sample constructive review comment:
> Nice work adding the data visualization feature. The chart makes the results easier to understand. Could you add axis labels and a descriptive title, handle missing values before plotting, and include a small test with sample data?

## Git LFS exercise

Install Git LFS and initialize it:

```powershell
git lfs install
git lfs track "*.csv"
```

Create a synthetic CSV larger than 100 MB only if the assignment requires it. Track it before the first commit:

```powershell
git add .gitattributes large_sample.csv
git commit -m "Track large sample dataset with Git LFS"
git push
```

Check GitHub LFS storage/bandwidth limits first. Do not upload personal, confidential, licensed, or sensitive raw data.

## nbdime notebook comparison

```powershell
python -m pip install nbdime
nbdiff movie_ratings_v1.ipynb movie_ratings_v2.ipynb
```

Make a change in the second notebook before comparing. Paste actual output or a screenshot into your README.

## GitHub Pages

1. Add `index.html` and your own `resume.pdf` to the repository root.
2. Commit and push the files.
3. Open repository Settings → Pages.
4. Select “Deploy from a branch”, choose `main` and `/ (root)`, and save.
5. Wait for deployment and test the published URL.

GitHub operations (Issue, fork, Pull Request, actual conflict resolution, and Pages publishing) must be completed on GitHub/your computer; files in this bundle cannot perform those actions automatically.
