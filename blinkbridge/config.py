from pathlib import Path
import logging
import json
from datetime import datetime, timedelta
from typing import Union
import os
import json
from pathlib import Path

config_data = {
    "still_video_duration": 0.5,
    "paths": {
        "videos": "/Volumes/Space/blinkbridge-1/Blink/videos",
        "concat": "/Volumes/Space/blinkbridge-1/Blink/concat",
        "config": "/Volumes/Space/blinkbridge-1/Blink/config"
    },
    "cameras": {
        "enabled": [],
        "disabled": [],
        "max_failures": 3,
        "restart_delay_seconds": 15
    },
    "blink": {
        "login": {
            "username": "bligava@icloud.com",
            "password": "gomxi5-qArdoz-dedsip"
        },
        "history_days": 90,
        "poll_interval": 1
    },
    "rtsp_server": {
        "address": "mediamtx",
        "port": 8555
    },
    "log_level": "INFO"
}

config_path = Path("/Volumes/Space/blinkbridge-1/config/.cred.json")

with config_path.open('w') as config_file:
    json.dump(config_data, config_file, indent=4)


__all__ = ['COMMON_FFMPEG_ARGS', 'CONFIG', 'DELAY_RESTART', 'RTSP_URL', 'PATH_VIDEOS', 'PATH_CONCAT', 'PATH_CONFIG']

COMMON_FFMPEG_ARGS = [
    '-hide_banner',
    '-loglevel', 'error',
    '-y',
]

CONFIG = None
DELAY_RESTART = None
RTSP_URL = None
PATH_VIDEOS = None
PATH_CONCAT = None
PATH_CONFIG = None

def load_config_file(file_name: Union[str, Path]) -> None:
    global CONFIG, DELAY_RESTART, RTSP_URL, PATH_VIDEOS, PATH_CONCAT, PATH_CONFIG

    with open(file_name) as f:
        CONFIG = json.load(f)

    DELAY_RESTART = timedelta(seconds=CONFIG['cameras']['restart_delay_seconds'])
    RTSP_URL = f'rtsp://{CONFIG['rtsp_server']['address']}:{CONFIG['rtsp_server']['port']}'

    PATH_VIDEOS = Path(CONFIG['paths']['videos'])
    PATH_CONCAT = Path(CONFIG['paths']['concat'])
    PATH_CONFIG = Path(CONFIG['paths']['config'])

config_file = os.getenv('BLINKBRIDGE_CONFIG', 'config.json')
load_config_file(config_file)
 
