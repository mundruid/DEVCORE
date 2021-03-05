# Git CLI demo commands

## Cloning a repo

```bash
git clone git@github.com:networktocode/pyntc.git
cd pyntc
git status
```

## Starting from develop from a repo that I cloned a while ago

```bash
git status
git pull origin develop
git checkout -b demo-git-cli
```

## A day in a developers life

```bash
git status
git add .
git commit -m "add docstring ios"
git push origin demo-git-cli
```

## A bad day(s) in a developers life

### Dangit, I accidentally committed to the wrong branch!

The problem:

```bash
git checkout develop
# make some changes
git add pyntc/devices/ios_device.py
git commit -m "add docstring"
```

How to fix the problem:

```bash
git reset HEAD~ --soft
git stash
git checkout correct-branch
git stash pop
git add .
git commit -m "add docstring"
```

### Dangit, I accidentally committed something to main that should have been on a brand new branch!

The problem:

```bash
git checkout main
git add .
git commit -m "I should not be doing this"
```

How to fix it:

```bash
git branch proper-branch
git reset HEAD~ --hard
git checkout proper-branch
```

Note: this doesn't work if you've already pushed the commit to a public/shared branch, and if you tried other things first, you might need to `git reset HEAD@{number-of-commits-back}` (painful but it works)

### Dangit, I committed and immediately realized I need to make one small change!

```bash
git add .
git commit --amend --no-edit
```

### Dangit, I need to undo a commit from like 5 commits ago!

```bash
git log
git revert [saved hash]
```

### Dangit, I need to undo my changes to a file!

```bash
git log
git checkout [saved hash] -- path/to/file
git commit -m "Wow you don't have copy paste to undo"
```

### Dangit, someone's MR was merged to develop before mine!

```bash
git pull origin develop
```

OR

```bash
git merge origin develop
```

OR

```bash
git rebase origin develop
```

### Forget all this noise, I give up

```bash
rm -r pyntc
git clone
cd pyntc
```

OR

```bash
git fetch origin
git checkout develop
git reset --hard origin/develop
git clean -d --force
```
