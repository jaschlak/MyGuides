
# Git Guide


## Setup

    git config --global user.name "\<insert username\>"    # set username
    git config --global user.email "\<insert e-mail\>"     # set e-mail
    git config --global --unset user.password              # delete user password
    git remote add origin "\<repo url\>"                   # Sets origin url
    git init                                               # set git workspace here
    git clone "\<insert url\>"                             # clone a repository 

## Normal Workflow

    git init                                               # initiate workspace
    git add .                                              # add current workspace to repository
    git status                                             # doublecheck this is what you expected
    git commit -m "\<insert message about what you added\>"# commits changes, preparing to add to repo
    git push origin master                                 # pushes changes to repo


## Troubleshooting

    git push origin master --force                         # sometimes you need to force 
                                                             the push (I.E. changed local repo location)
    git remote -v                                          # see where the remote origin is pointing
    git -rf .git                                           # uninitiate local .git file

## Branching

    git clone -b <branch name> --single-branch <repo url>  # Clones branch of repo to this path