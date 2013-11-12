# Scrapy settings for florida_jobs project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'florida_jobs'

SPIDER_MODULES = ['florida_jobs.spiders']
NEWSPIDER_MODULE = 'florida_jobs.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'florida_jobs (+http://www.yourdomain.com)'

# Crawl responsibly by adding some delay
DOWNLOAD_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = True
