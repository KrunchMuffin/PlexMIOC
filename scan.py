import os
from glob import iglob
from pathlib import Path
from pprint import pprint

from pymediainfo import MediaInfo

from config import load_config
from log_handler import logger
import constants as c


def check_audio(com_name, other_format, title) -> str:
    if com_name in c.ATMOS_SET:
        return 'atmos'
    elif other_format in c.TRUEHD_SET:
        return 'truehd'
    elif c.DTSX_DICT["title"] == title or c.DTSX_DICT["other_format"] in other_format:
        return 'dtsx'
    elif c.DTS_MA_DICT["commercial_name"] == com_name or c.DTS_MA_DICT["other_format"] in other_format:
        return 'dtsma'
    elif c.DTS_HD_DICT["commercial_name"] == com_name or c.DTS_HD_DICT["other_format"] in other_format:
        return 'dtshd'
    else:
        return ''


def start_scan(has_movies, has_tv):
    cfg = load_config()
    movies_path = cfg.get("PLEX", "movies_path")
    tv_path = cfg.get("PLEX", "tvshows_path")

    if has_movies:
        if not Path(movies_path).exists():
            logger.info(f"The Movies path does not exist: ${movies_path}. Please check your config.")
            return
        else:
            logger.debug(f"Movies path exists: ${movies_path}")
            logger.info("Starting Movies scan")
            movies_path_glob = movies_path + "/**/*"
            # grab all the files into an iterable
            file_list = [f for f in iglob(movies_path_glob, recursive=True) if os.path.isfile(f)]
            # loop over the file_list iterable
            for f in file_list:
                # TODO: we should probably keep track of files scanned for later runs.
                logger.info(f"Scanning... ${f}")
                info = MediaInfo.parse(f)

                # get what we need from the first audio track
                if info.audio_tracks and info.audio_tracks[0].channel_s >= 6:
                    # print(f)
                    com_name = info.audio_tracks[0].commercial_name
                    other_format = info.audio_tracks[0].other_format
                    title = info.audio_tracks[0].title
                    print(check_audio(com_name, other_format, title))

                    # print(com_name, ' | ', title)

                # for track in info.tracks:
                #     if track.track_type == "Audio" and info.audio_tracks[0].channel_s >= 6:
                #         print("Audio Track data:")
                #         pprint(track.to_data())
                #     elif track.track_type == "Video":
                #         print("Video Track data:")
                #         pprint(track.to_data())

    if not Path(tv_path).exists():
        logger.info(f"The TV Shows path does not exist: ${tv_path}. Please check your config.")
        return False
    else:
        logger.debug(f"TV Shows path exists: ${tv_path}")
