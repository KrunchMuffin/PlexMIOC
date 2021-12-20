from pathlib import Path

import config
import scan
from config import load_config
from log_handler import logger


def check_config() -> bool:
    logger.info("Starting check config")
    ok = Path("config/config.ini").exists()
    if ok:
        logger.debug("Config file exists.")
        cfg = load_config()
        has_main = cfg.has_section('MAIN')
        has_plex = cfg.has_section('PLEX')
        has_audio_options = cfg.has_section('AUDIO_OPTIONS')
        has_video_options = cfg.has_section('VIDEO_OPTIONS')
        has_logos = cfg.has_section('LOGOS')
        if not has_main or not has_plex or not has_audio_options or not has_video_options or not has_logos:
            logger.debug(
                f"MAIN ${has_main} | PLEX ${has_plex} | AUDIO_OPTIONS ${has_audio_options} | LOGOS ${has_logos} | "
                f"VIDEO_OPTIONS ${has_video_options}")
            logger.info(
                "There is config file issue. One or more of the following sections are missing: MAIN, PLEX, "
                "AUDIO_OPTIONS, VIDEO_OPTIONS, LOGOS")
            ok = False
    else:
        logger.info(
            "Config file does not exist. Creating config. Please open config/config.ini and adjust accordingly.")
        ok = config.create_config()
    return ok


if __name__ == '__main__':
    logger.debug(
        "##################### STARTING NEW SESSION ##############################")
    logger.info("Starting up...")
    if check_config():
        cfg = load_config()
        if cfg.getboolean('MAIN', 'enabled'):
            logger.debug("Script enabled")
            has_movies = cfg.getboolean('MAIN', 'enable_movies')
            if has_movies:
                logger.info("Movies enabled")
            has_tv = cfg.getboolean('MAIN', 'enable_tvshows')
            if has_tv:
                logger.info("TV Shows enabled")
            scan.start_scan(has_movies, has_tv)
        else:
            logger.info("Script is not enabled. Exiting...")
    else:
        logger.info(
            "There is no config file located at config/config.ini and I was not able to create one. Exiting...")
