response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Exchange'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Auction'),URL('default','auction')==URL(),URL('default','auction'),[]),
(T('MMBots'),URL('default','mmaker')==URL(),URL('default','mmaker'),[]),
(T('Join Us'),URL('default','join')==URL(),URL('default','join'),[]),
(T('FAQ'),URL('default','faq')==URL(),URL('default','faq'),[]),
]
