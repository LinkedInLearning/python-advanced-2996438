# Demonstrate how to customize logging output

import logging

extData = {'user':'Ralph'}
# TODO: add another function to log from
def meineProtokollFunktion():
    logging.debug("Das ist eine Debug-Level-Nachricht",extra=extData)

def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Zeile:%(lineno)d User:%(user)s %(message)s"
    dateStr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG, format=fmtStr, datefmt=dateStr)

    logging.info("Das ist eine Info-Level-Nachricht", extra=extData)
    logging.warning("Das ist eine Warning-Level-Nachricht",extra=extData)
    meineProtokollFunktion()


if __name__ == "__main__":
    main()
