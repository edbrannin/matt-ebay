Usage:

## First-time setup

    virtualenv env
    . env/bin/activate
    pip install -r requirements.txt

## Afterwards, once per shell session:

    . env/bin/activate

## Doing it

* `python matt_ebay.py csvfile templatefile`
* `python matt_ebay.py csvfile templatefile | tee result.csv`
* `python matt_ebay.py csvfile templatefile > result.csv`
