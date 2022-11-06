# Boilerplate for Python Programs

This is the boilerplate to create Python standalone programs, like CLI utilities.


# VSCode Dev Containers

**VSCode Dev Containers** are very handy to debug. Run inside **Dev Containers** to run a recurrent Docker container that persist installed packages and other stuff. Use the **exec** script to attach to the Dev Container to use external terminals. Use the integrated environment in VSCode to debug. Use the **python_run** script to run an independent, volatile container. External infrastructure like databases and the like are to be defined in independent Docker Composes whose network the Dev Container attach to. Check the **graph/Toolsresearch/Dev Containers** for more details.

**Virtualenv** queda obsoleto.


# Publishing Workflow

Steps:

- [] check for **print("D:** left behind;

- [] review changes with Git to get a clear idea of changes in the current version, but don't commit yet;

- [] close the **Git Flow Feature** and go back to **develop**, if any. Get a clear idea of changes in the current version;

- [] if applicable, create a new **Git Flow Release**;

- [] push all branches and tags to **GitHub**:

```Shell
# This will push ALL branches to origin, even the non-existant ones. Remove sporious branches with git push origin :branch_name
git push --all origin
git push --tags
git fetch -av --prune
git branch -av
```


# DVC Operations

Most used DVC operations:

```shell
dvc status
dvc add data
dvc move old_file_name new_file_name
dvc commit
dvc push
dvc pull
```
