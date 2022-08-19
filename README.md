# Beryl
named after the rare gemstone: https://en.wikipedia.org/wiki/Beryl


## Local Setup

### Install Miniconda

For installers for operating systems other than linux see https://docs.conda.io/en/latest/miniconda.html

    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -s --output miniconda.sh
    chmod +x miniconda_installer.sh
    ./miniconda.sh -u
    rm miniconda.sh

### Create conda enviroment

You may need to reopen your shell after installing miniconda

    conda create -n beryl python=3.10
    conda activate beryl
    conda install --file requirements.txt

### Run the project

The default port is 5000

    python ./app/main.py

## Docker

### Building the Docker container

With your working directory in the root of the repository

    docker build --tag beryl .

### Running the Docker container

    docker run -p 5000:5000 beryl

or for detached mode

    docker run -d -p 5000:5000 beryl    



