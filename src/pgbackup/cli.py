import argparse

known_drivers = ["local", "s3"]

class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values

        if driver.lower() not in known_drivers:
            parser.error("unknown driver; available drivers are 'local' or 's3'")

        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = argparse.ArgumentParser(description="backup a postgresql database locally or to aws s3")
    parser.add_argument("url", help="url of the database to backup")
    parser.add_argument("--driver",
            help="which driver to use and where to store the backup",
            nargs=2,
            metavar=("DRIVER", "DESTINATION"),
            action=DriverAction,
            required=True)
    return parser

