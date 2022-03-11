# `datacol` #

> Collect data for VCA QoE using active measurement.

Requires [Google Chrome](https://www.google.com/chrome/) and the accompanying [ChromeDriver](https://chromedriver.chromium.org/).

## Setup ##

Note: On Windows, run `py -3` instead of `python3`.

### With `poetry` ###
```sh
$ mv .../chromedriver drivers/
$ poetry install
```

### Without `poetry`
```sh
$ mv .../chromedriver drivers/
$ python3 -m venv .venv
$ . .venv/bin/activate
$ python3 -m pip install -r requirements.txt
```

## Run ##
```sh
$ python3 -m datacol
```
