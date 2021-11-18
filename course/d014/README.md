# 21/10/25 html, CSS lesson

## What I learned(Important)

### how to use git ([more information](https://sabarada.tistory.com/75))

1. initial setting
    * `git config --global user.name "$user-name$"` (to unset : `git config --global --unset $user.name`)
    * `git config --global user.email "$user-email$"`
    * `git config --list` (or `git config -l`)
    * `cd $repo-path$` (to move other drive : `cd :$drive name$`)
    * `git init`
    * `git checkout -b $branch-name$` (for us, branch name is "main")
    * `git remote add $repo-url-nickname$ $repo-url$` (to remove: `git remote remove $repo-url-nickname$`)
    * `git remote -v`
    * `git log --oneline`
2. main use
    * `git status`
    * `git add $file-name$` (or `git add .` for all)
    * `git status`
    * `git commit -m "$commit-contents$"`
    * (`git commit -am "$commit-contents$"` = `git add .` + `git commit -m "$commit-contents$"`, -am does add and commit at once)
    * `git log --oneline`(press `q` to quit log)
      * we could see `HEAD -> $branch-name$` and `$repo-url-nickname$/$branch-name$`
      * `$repo-rul-nickname$/$branch-name$` is last log that you pushed to github  
      * `HEAD -> $branch-name$` is last log that you committed on your local system
      * between them is logs that you committed and not pushed to github  
    * `git push $repo-url-nickname$ $branch-name$`
    * login to your github account to push
      * when you once login github, git automatically save the data with credential
      * you could see saved data with command `git credential fill` and `url=https://github.com`  
      * If you want to remove this saved data, go to windows credential

### how to make responsive web and navigation bar

* practice file: [index.html](index.html) and [style.css](style.css)

## What I studied myself

## What I didn't understand

## What I want to know more

## etc(Additional)

## Practice problems
