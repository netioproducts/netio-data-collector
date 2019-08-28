
# netio-data-collector
Simple HTTP server listening TCP on specific port for incoming data. Data is continuously saved into CSV file.

## Table of Contents
- [Installation and usage](#Installation-and-usage)
    - [Linux dependencies](#Linux-dependencies)
    - [Windows dependencies](#Windows-dependencies)
    - [Installation](#Installation)
    - [Usage](#Usage)

## Installation and usage

#### Requirements:
- Python 3.6 or newer
### Linux dependencies
##### Ubuntu/Debian
```
sudo apt-get install python3
```

##### Fedora/RHEL 8+/CentOS 8+
```
sudo dnf install python3
```

##### OpenSUSE
```
sudo zypper install python3
```

### Windows dependencies
- Download latest python 3 package from [the official site](https://www.python.org/downloads/)
- Install the package and check "Add Python 3.x to PATH"

##### Installation
- clone the repository `git clone https://github.com/netioproducts/netio-data-collector.git` (requires git)
- change into the cloned directory `cd netio-data-collector`
**OR**
- download the repository from [GitHub](https://github.com/netioproducts/netio-data-collector.git)
- unzip the downloaded folder
- open the unzipped folder in file explorer
- open terminal in the current location (hold SHIFT and right click inside the folder, click on `Open PowerShell window here` or `Open Command Prompt window here`)

### Usage

##### Linux usage
run `python3 main.py`

##### Windows usage
run `python main.py`

The output will be saved to a directory specified in `config.py`  the default is `$(git-root)/log/log_$(device-mac).csv`  
Each device will have separate `.csv` file.


### Parameters
| short |  long  | default | description |
|-------|--------|---------|-------------|
|  -n   | --host | 0.0.0.0 | ip address to listen on. |
|  -p   | --port | 9000    | port to listen on. Warning: ports  below 1024 require root permission. |
