BOT_NAME = 'chitai_gorod'

SPIDER_MODULES = ['chitai_gorod.spiders']
NEWSPIDER_MODULE = 'chitai_gorod.spiders'


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'


ROBOTSTXT_OBEY = False


CONCURRENT_REQUESTS = 14


DOWNLOAD_DELAY = 5

COOKIES_ENABLED = True


IMAGES_STORE = "images"


ITEM_PIPELINES = {
   'chitai_gorod.pipelines.ChitaiGorodImagesPipeline': 299,
   'chitai_gorod.pipelines.ChitaiGorodPipeline': 300,
}


MONGO_URI: str = 'mongodb://localhost:27017'
MONGO_DATABASE: str = 'mydb'

from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS = ['--headless', '--start-maximized']

DOWNLOADER_MIDDLEWARES = {
   'scrapy_selenium.SeleniumMiddleware': 800
}

LOG_ENABLED = True
LOG_FILE = 'log.txt'
lOG_LEVEL = 'DEBUG'