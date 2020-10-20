import datetime
import hashlib
import logging
import os
from logging.handlers import SysLogHandler

from utils.settings_handler import settings

LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"


class ColoredFormatter(logging.Formatter):
    """
    Apply only to the console handler.
    """

    green = "\u001b[32m"
    cyan = "\u001b[36m"
    reset = "\u001b[0m"

    def format(self, record):
        frmt = LOG_FORMAT
        if record.getMessage().startswith("id="):
            frmt = f"{ColoredFormatter.green}{frmt}{ColoredFormatter.reset}"
        if record.getMessage().startswith("msg="):
            frmt = f"{ColoredFormatter.cyan}{frmt}{ColoredFormatter.reset}"
        formatter = logging.Formatter(frmt)
        return formatter.format(record)


def set_up_logging(save_to_file=True):
    """
    Logger for tenhou communication and AI output
    """
    logs_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "logs")
    if not os.path.exists(logs_directory):
        os.mkdir(logs_directory)

    logger = logging.getLogger("tenhou")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = ColoredFormatter(LOG_FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    ai_logger = logging.getLogger("ai")
    ai_logger.setLevel(logging.DEBUG)
    ai_logger.addHandler(ch)

    log_prefix = settings.LOG_PREFIX
    if not log_prefix:
        log_prefix = hashlib.sha1(settings.USER_ID.encode("utf-8")).hexdigest()[:5]

    if save_to_file:
        formatter = logging.Formatter(LOG_FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
        ch.setFormatter(formatter)

        # we need it to distinguish different bots logs (if they were run in the same time)
        file_name = "{}_{}.log".format(log_prefix, datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S"))

        fh = logging.FileHandler(os.path.join(logs_directory, file_name), encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        ai_logger.addHandler(fh)

    if settings.PAPERTRAIL_HOST_AND_PORT:
        syslog = SysLogHandler(address=settings.PAPERTRAIL_HOST_AND_PORT)
        game_id = hashlib.sha1(datetime.datetime.now().strftime("%Y-%m-%d_%H_%M").encode("utf-8")).hexdigest()[:5]
        game_id = f"BOT_{log_prefix}_{game_id}"
        formatter = logging.Formatter(f"%(asctime)s {game_id}: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        syslog.setFormatter(formatter)
        logger.addHandler(syslog)
        ai_logger.addHandler(syslog)
