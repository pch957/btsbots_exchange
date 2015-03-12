response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [(T('Exchange'),URL('default','index')==URL(),URL('default','index'),[]),]
submenu = [ (T('CNY/BTS'),False,URL('default','auction',vars=dict(market='BTS')),[]), ]
submenu += [ (T('CNY/BTC'),False,URL('default','auction',vars=dict(market='BTC')),[]), ]
response.menu += [ (T('Auction'),URL('default','auction')==URL(),URL('default','auction',vars=dict(market='BTS')),submenu)]
response.menu += [ (T('MMBots'),URL('default','mmaker')==URL(),URL('default','mmaker'),[]), ]
response.menu += [ (T('Join Us'),URL('default','join')==URL(),URL('default','join'),[]), ]
response.menu += [ (T('FAQ'),URL('default','faq')==URL(),URL('default','faq'),[]), ]
