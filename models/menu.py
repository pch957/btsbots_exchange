response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [(T('Exchange'),URL('default','index')==URL(),URL('default','index'),[]),]
submenu = [ (T('CNY/BTS'),False,URL('default','auction',vars=dict(market='BTS')),[]), ]
submenu += [ (T('CNY/PLS'),False,URL('default','auction',vars=dict(market='PLS')),[]), ]
submenu += [ (T('CNY/BTC'),False,URL('default','auction',vars=dict(market='BTC')),[]), ]
response.menu += [ (T('Auction'),URL('default','auction')==URL(),URL('default','auction',vars=dict(market='BTS')),submenu)]
submenu = [ (T('PLS<->BTSBOTS.PLS'),False,URL('default','gateway',vars=dict(asset='PLS')),[]), ]
response.menu += [ (T('Gateway'),URL('default','gateway')==URL(),URL('default','gateway',vars=dict(asset='PLS')),submenu)]
response.menu += [ (T('MMBots'),URL('default','mmaker')==URL(),URL('default','mmaker'),[]), ]
response.menu += [ (T('Join Us'),URL('default','join')==URL(),URL('default','join'),[]), ]
response.menu += [ (T('FAQ'),URL('default','faq')==URL(),URL('default','faq'),[]), ]
