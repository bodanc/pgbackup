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
    parser.add_argument("--driver", "-d",
            help="which driver to use and where to store the backup",
            nargs=2,
            metavar=("DRIVER", "DESTINATION"),
            action=DriverAction,
            required=True)
    return parser


def main():
    # import the boto3 dependeency only after the main function is called;
    import boto3
    import time
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)

    if args.driver == "s3":
        client = boto3.client("s3")
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        print("backing up the database to s3 bucket %s as %s" % (args.destination, file_name))
        storage.s3(client, dump.stdout, args.destination, "example.sql")
    else:
        outfile = open(args.destination, "w")
        print("backing up the database locally to %s" % outfile.name)
        storage.local(dump.stdout, outfile)

