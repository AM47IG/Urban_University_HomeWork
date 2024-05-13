# -*- coding: utf-8 -*-

log_config = {
    "version": 1,
    "formatters": {
        "_formatter": {
            "format": "%(levelname)s: %(message)s"
        },
    },
    "handlers": {
        "success_handler": {
            "class": "logging.FileHandler",
            "formatter": "_formatter",
            "filename": "success_responses.log",
            "mode": "w",
            "encoding": "UTF-8",

        },
        "bad_handler": {
            "class": "logging.FileHandler",
            "formatter": "_formatter",
            "filename": "bad_responses.log",
            "mode": "w",
            "encoding": "UTF-8",
        },
        "blocked_handler": {
            "class": "logging.FileHandler",
            "formatter": "_formatter",
            "filename": "blocked_responses.log",
            "mode": "w",
            "encoding": "UTF-8",
        },
    },
    "loggers": {
        "success": {
            "handlers": ["success_handler"],
            "level": "INFO",
        },
        "bad": {
            "handlers": ["bad_handler"],
            "level": "WARNING",
        },
        "blocked": {
            "handlers": ["blocked_handler"],
            "level": "ERROR",
        },
    },
}
