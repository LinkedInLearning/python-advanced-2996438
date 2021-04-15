# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from

def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG)

    logging.info("Das ist eine info-Level-Nachricht")
    logging.warning("Das ist eine Warning-Level-Nachricht")


if __name__ == "__main__":
    main()
