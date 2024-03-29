# -*- coding: utf-8 -*-
DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.7'

BLOG_PLATFORM = 'tumblr'  # Wordpress or tumblr

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'musinglyinclined.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'oMLZBQ5YjKCKqC9gYGpcVWdbBk7FOOTHqJYorCd9IGfPTxBlfI'

#Blog Integration: Wordpress
WORDPRESS_BLOG_URL = 'musinglyinclined.wordpress.com'
WORDPRESS_API_URL = 'https://public-api.wordpress.com/rest/v1/sites/{0}'.format(WORDPRESS_BLOG_URL)

#RSS Feed Integration: (by default use Tumblr rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'https://api.twitter.com/'
TWITTER_CONSUMER_KEY = 'lICsTbcETiZc23iYTQwww'
TWITTER_CONSUMER_SECRET = 'kRUih2UvaTY1PE799CoaNMnQIRtCHpG10ABzmQCqfE'
TWITTER_USER_KEY = '159258400-1wrFbywQ0J8szCcjCW31xc5b18ouJfaPAiyHrU9B'
TWITTER_USER_SECRET = '0PgmpLRTmdceiEHLWjqqFKnChsxGzOGWUh44a3vkggk'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '834ddd752ff1447b6b5d645230c47bfcdd8d6b26'

GITHUB_OAUTH_ENABLED = False
GITHUB_CLIENT_ID = '1abcfba37836048f5231'
GITHUB_CLIENT_SECRET = '32c91e18fd65a17c28141f7df13435fa7312527a'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Stack Overflow Integration
STACKOVERFLOW_INTEGRATION_ENABLED = True
STACKOVERFLOW_API_URL = 'http://api.stackoverflow.com/1.1/'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '15952251.ac0178d.c7f85bb7dcdb485e8d16a28024515763'
INSTAGRAM_USER_ID = '15952251'

INSTAGRAM_OAUTH_ENABLED = False
INSTAGRAM_CLIENT_ID = 'ac0178dc17a44430bac2bbd5eaf7a2b9'
INSTAGRAM_CLIENT_SECRET = 'b4a36821456b487aa3870427d078e534'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Foursquare Integration
FOURSQUARE_INTEGRATION_ENABLED = True
FOURSQUARE_API_URL = 'https://api.foursquare.com/v2/'
FOURSQUARE_ACCESS_TOKEN = 'XBCVF4FZAJTQ4YFTTSSAFSQJF0LKGD0NEYA2T4RJG51TNU2K'
FOURSQUARE_SHOW_CURRENT_DAY = True

FOURSQUARE_OAUTH_ENABLED = False
FOURSQUARE_CLIENT_ID = '3QYFS0X1JEBXNBYIQZRP1UWJREX1EDMSLN23RBBSSDH5LDK5'
FOURSQUARE_CLIENT_SECRET = 'WS3AE3D1SFXZ2RYF0LDWJ0SL4XQBQZEEWUTAOYNVEX1IBAMY'
FOURSQUARE_OAUTH_AUTHORIZE_URL = 'https://foursquare.com/oauth2/authenticate'
FOURSQUARE_OAUTH_ACCESS_TOKEN_URL = 'https://foursquare.com/oauth2/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = ''


#ShareThis
SHARETHIS_PUBLISHER_KEY = ''


#Woopra
WOOPRA_TRACKING_DOMAIN = ''
WOOPRA_TRACKING_IDLE_TIMEOUT = 300000  # 5 minutes
WOOPRA_TRACKING_INCLUDE_QUERY = False


#Disqus Integration
DISQUS_INTEGRATION_ENABLED = True
DISQUS_SHORTNAME = 'bsiddiqui'


#Lastfm Integration
LASTFM_INTEGRATION_ENABLED = True
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
LASTFM_API_KEY = '[ENTER LASTFM API_KEY HERE, SEE LASTFM SETUP INSTRUCTIONS]'

#SoundCloud Integration
SOUNDCLOUD_INTEGRATION_ENABLED = True
SOUNDCLOUD_API_URL = 'https://api.soundcloud.com/'
SOUNDCLOUD_CLIENT_ID = 'e4735d4c6856da33ad4b43be1529390f'
SOUNDCLOUD_SHOW_ARTWORK = True
SOUNDCLOUD_PLAYER_COLOR = 'ff912b'


#Bitbucket Integration
BITBUCKET_INTEGRATION_ENABLED = False
BITBUCKET_API_URL = 'https://api.bitbucket.org/1.0/'
# Forks count require one connection for each repository,
# set BITBUCKET_SHOW_FORKS to false to disable
BITBUCKET_SHOW_FORKS = False


#Tent.io Integration
TENT_INTEGRATION_ENABLED = False
TENT_ENTITY_URI = '[ENTER YOUR ENTITY URI HERE] ex. https://yourname.tent.is'
TENT_FEED_URL = '[ENTER A URL TO YOUR FEED] ex. https://yourname.tent.is'


#Steam Integration
STEAM_INTEGRATION_ENABLED = False
STEAM_API_URL = 'http://api.steampowered.com/ISteamUser'
STEAM_API_KEY = '[ENTER YOUR STEAM API KEY HERE, SEE STEAM SETUP INSTRUCTIONS]'


SITEMAP_ENABLED = False

if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://bsiddiqui.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
