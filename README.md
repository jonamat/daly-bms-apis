# daly-bms-apis

Serve data from Daly BMS via REST APIs

## Installation

```bash
git clone https://github.com/jonamat/daly-bms-apis
cd daly-bms-apis
pip install -r requirements.txt
```

## Usage

Adjust the .env file to your needs and run the script:

```bash
python server.py
``` 

## API

Pretty self-explanatory

- /status
- /soc
- /balancing-status
- /cell-voltages
- /mosfet-status
- /errors
- /temperatures
- /all

## License

[MIT](https://choosealicense.com/licenses/mit/)