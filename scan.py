from config import load_config


def start_scan():
    cfg = load_config()
    has_movies = cfg.getboolean('DEFAULT', 'enable_movies')
    has_tv = cfg.getboolean('DEFAULT', 'enable_tvshows')
