
# netio-data-collector
Simple HTTP server listening TCP on specific port for incomming data. Data are continuosly saved into CSV file.


## installation and usage

### instalattion

first you need to install python3.6+ and git

on ubuntu/debian
```
sudo apt-get install python3 git
```

on Arch python3 is by default pre-installed


clone the reposiory and change directory
```
git clone git@github.com:netioproducts/netio-data-collector.git
cd netio-data-collector
```

### usage

just run the `Main.py` with python3
```
python3 Main.py
```
or 
```
./Main.py
```

the script will save everything in directory specified in `Config.py`  the default is `$(git-root)/log/log_$(device-mac).csv`

each device will have separate csv file.


### parameters
| short |  long  | default | description |
|-------|--------|---------|-------------|
|  -n   | --host | 0.0.0.0 | ip address to listen on. |
|  -p   | --port | 9000    | port to listen on. Warning: ports  below 1024 require root permission. |
