import requests as rq
import logging.config
from log_settings import log_config

logging.config.dictConfig(log_config)
log_success = logging.getLogger('success')
log_bad = logging.getLogger('bad')
log_blocked = logging.getLogger('blocked')

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            log_success.info(f'\'{site}\', response - 200')
        else:
            log_bad.warning(f'\'{site}\', response - {response.status_code}')
    except rq.exceptions.ConnectionError:
        log_blocked.error(f'\'{site}\', NO CONNECTION')
    except rq.exceptions.ReadTimeout:
        log_blocked.error(f'\'{site}\', READ TIMEOUT')
