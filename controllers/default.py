# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    form = FORM(TABLE(
      TR(T('Deposit currency')+':', SELECT('BTS','BOTSCNY','CNY','USD','EUR','GOLD','SILVER','BTC', _name="deposit_currency",_id="deposit_currency",_onchange="javascript:calc_order()")),
      TR(T('Deposit amount')+':', INPUT(_id="deposit_amount",_name="deposit_amount",_onchange="javascript:calc_order();",_onkeyup="javascript:calc_order();",value=1),T('Max')+':',B(_id="deposit_limit")),
      TR(T('Withdraw currency')+':', SELECT('BOTSCNY','BTS','CNY','USD','EUR','GOLD','SILVER','BTC', _name="withdraw_currency",_id="withdraw_currency",_onchange="javascript:calc_order()")),
      TR(T('Withdraw amount')+':', B(_id="withdraw_amount")),
      TR(T('Price')+':', B(_id="exchange_price"))),
      INPUT(_type='button', _value=T("Place Order"),  _onclick="javascript:generate_link()"),
      T('Comment')+':', TT(_id="comment"),
      DIV(_id="link_div",_style="display:none"),
      _id="fm", _name="fm")

    return dict(form=form)

def auction():
    form = FORM(
      (T('Deposit')),
      (INPUT(_id="deposit_amount",_name="deposit_amount",_onkeyup="javascript:refresh_comment();",_onchange="javascript:refresh_comment();",value=1)),
      (SELECT('BTS','BOTSCNY','CNY','USD','EUR','GOLD','SILVER', _name="deposit_currency",_id="deposit_currency",_onchange="javascript:refresh_comment();")),
      (T('with price limit')),
      (INPUT(_id="price_limit",_name="price_limit",_onkeyup="javascript:refresh_comment();",_onchange="javascript:refresh_comment();")),
      ('CNY/BTS'),
      (INPUT(_type='button', _value=T("Place Order"),  _onclick="javascript:generate_link()")),
      DIV(_id="link_div",_style="display:none"),
      P(),
      T('Comment')+':', TT(_id="comment"),
      P(),
      T('transfer BTS if you want to sell, others for buy.'),
      _id="fm", _name="fm")
    #response.flash = T('transfer BTS if you want to sell, others for buy.')
    return dict(form=form)

def mmaker():
    return dict()

def faq():
    return dict()

def join():
    return dict()

def error():
    return dict()

