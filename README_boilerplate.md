# Boilerplate for Python Programs

This is the boilerplate to create Python standalone programs, like CLI utilities.


# VSCode Dev Containers

**VSCode Dev Containers** are very handy to debug. Run inside **Dev Containers** to run a recurrent Docker container that persist installed packages and other stuff. Use the **exec** script to attach to the Dev Container to use external terminals. Use the integrated environment in VSCode to debug. Use the **python_run** script to run an independent, volatile container. External infrastructure like databases and the like are to be defined in independent Docker Composes whose network the Dev Container attach to. Check the **graph/Toolsresearch/Dev Containers** for more details.

**Virtualenv** queda obsoleto.


# Setup (DELETE AFTER CONFIGURING)

Follow:

- [x] configure the **tmuxinator profile** and install it;

- [x] configure scripts at **docker**;

- [x] configure the **VSCode Dev Container** as explained in **KB/Dev Containers** at the **dot.devcontainer** folder;

- [x] configure the script **src/010-pip_install.sh** to install packages;

- [x] write something in the main **Git README.md**;

- [x] initialise **Git**, **DVC** (if applicable), and **Git Flow**:

```shell
# Init GIT
git init

# Check for big files
mlkgitlfssearch

# For DVC, create a folder to store large files in the file system
# Initialize DVC if applicable
dvc init
dvc remote add -d storage /mnt/samsung_hdd_1_5tb/dvc_storage/project_name_if_applicable
dvc config cache.local storage

# Add DVC files if applicable
dvc add
dvc commit
dvc push

# Create and set up GIT first commit
git commit -m "First commit"
```

- [] set up the repo at **GitHub** and upload the first commits in **main** branch:

```shell
# This is what GitHub output for the "…or push an existing repository from the command line"
# post-repo creation option
git remote add origin git@github.com:whatever.git
git branch -M main
git push -u origin main
```

- [] initialize **Git Flow** and push **develop branch**:

```shell
git flow init
git checkout develop
git push -u origin develop
```

- [] configure **GitHub Pages** pointing the the **main branch docs folder**.


# Management of Virtualenv

Just:

```shell
# Activate
. virtualenv/bin/activate

# List packages
pip list

# Deactivate
deactivate
```


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
