from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'BTSBots Exchange'
settings.subtitle = 'powered by btsbots'
settings.author = 'alt'
settings.author_email = 'alt@BTS'
settings.keywords = 'bts btsbots exchange botscny botsfund'
settings.description = 'exchange for bts'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '81c2eeed-0354-4a1d-b7a8-cfcb8fc33eb1'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
