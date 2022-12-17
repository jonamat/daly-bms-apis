from bottle import route, run, template
from dalybms import DalyBMS
from dotenv import load_dotenv
import os

driver = DalyBMS()
load_dotenv()


@route("/status")
def index():
    data = driver.get_status()

    if not data:
        return abort(500, "Device not responding")
    else:
        return data


@route("/soc")
def index():
    data = driver.get_soc()

    if not data:
        return abort(500, "Device not responding")
    else:
        return data


@route("/balancing-status")
def index():
    data = driver.get_balancing_status()

    if not data:
        return abort(500, "Device not responding")
    else:
        return data


@route("/cell-voltages")
def index():
    data = driver.get_cell_voltages()

    if not data:
        return abort(500, "Device not responding")
    else:
        return data


@route("/mosfet-status")
def index():
    data = driver.get_mosfet_status()

    if not data:
        return abort(500, "Device not responding")
    else:
        return data


@route("/errors")
def index():
    data = driver.get_errors()

    if not data:
        return abort(500, "Device not responding")
    else:
        return data


@route("/temperatures")
def index():
    data = driver.get_temperatures()

    if not data:
        return abort(500, "Device not responding")
    else:
        return data


@route("/all")
def index():
    data = driver.get_all()

    if not data:
        return abort(500, "Device not responding")
    else:
        return data


if __name__ == "__main__":
    print(f"Connecting to device on {os.getenv('DEVICE_ADDR')}")
    driver.connect(device=os.getenv("DEVICE_ADDR"))

    print(f"Starting server on {os.getenv('HOST')}:{os.getenv('PORT')}")
    run(host=os.getenv("HOST"), port=os.getenv("PORT"))
