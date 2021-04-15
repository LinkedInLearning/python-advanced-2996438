# demonstrate the logging api in Python

# use the built-in logging module
import logging


def main():
    # Use basicConfig to configure logging
    # this is only executed once, subsequent calls to
    # basicConfig will have no effect
    logging.basicConfig(level=logging.DEBUG,
                        filemode="w",
                        filename="output.log")

    # Try out each of the log levels
    logging.debug("Das ist eine Debug-Nachricht")
    logging.info("Das ist eine Info-Nachricht")
    logging.warning("Das ist eine Warning-Nachricht")
    logging.error("Das ist eine Error-Nachricht")
    logging.critical("Das ist eine Critical-Nachricht")

    # Output formatted string to the log
    logging.info("Hier ist eine {} Variable und ein int: {}".format("string", 10))


if __name__ == "__main__":
    main()
