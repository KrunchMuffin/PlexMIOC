from configparser import ConfigParser


def load_config():
    # if we are here, we passed the config check
    # create instance of ConfigParser
    cfg = ConfigParser(allow_no_value=True)
    # read the ini file.
    cfg.read_file(open("config/config.ini"))

    return cfg
