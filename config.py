from configparser import ConfigParser
from pathlib import Path


def load_config() -> ConfigParser:
    # if we are here, we passed the config check
    # create instance of ConfigParser
    cfg = ConfigParser(allow_no_value=True)
    # read the ini file.
    cfg.read_file(open("config/config.ini"))
    # return instance of ConfigParser
    return cfg


def create_config() -> bool:
    conf: ConfigParser = ConfigParser()
    conf.add_section('MAIN')
    conf.set('MAIN', 'enabled', '0')
    conf.set('MAIN', 'movies_enabled', '0')
    conf.set('MAIN', 'tvshows_enabled', '0')
    conf.set('MAIN', 'debug', '0')
    conf.add_section('PLEX')
    conf.set('PLEX', 'movies_path', '')
    conf.set('PLEX', 'tvshows_path', '')
    conf.add_section('OPTIONS')
    conf.set('OPTIONS', 'add_hdr', '')
    conf.set('OPTIONS', 'add_dolby_vision', '')
    conf.set('OPTIONS', 'add_atmos', '')
    conf.set('OPTIONS', 'show_atmos_channel_count', '')
    conf.set('OPTIONS', 'add_dtsx', '')
    conf.set('OPTIONS', 'add_dts_ma', '')
    conf.set('OPTIONS', 'add_dts', '')
    conf.set('OPTIONS', 'add_dolby_digital', '')
    conf.set('OPTIONS', 'add_dolby_truehd', '')
    conf.add_section('LOGOS')
    conf.set('LOGOS', 'dolby_vision', '')
    conf.set('LOGOS', 'atmos', '')
    conf.set('LOGOS', 'dtsx', '')
    conf.set('LOGOS', 'dts_ma', '')
    conf.set('LOGOS', 'dts', '')
    conf.set('LOGOS', 'dolby_digital', '')
    conf.set('LOGOS', 'truehd', '')

    with open('config/config.ini', 'w') as f:
        conf.write(f)
    return Path("config/config.ini").exists()
