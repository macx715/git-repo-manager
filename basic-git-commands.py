import git


repo = git.Repo('<repodir>')
repo.remotes.origin.pull()



