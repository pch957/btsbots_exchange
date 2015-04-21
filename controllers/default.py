# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    form = FORM(TABLE(
      TR(T('Deposit currency')+':', SELECT('BOTSCNY','BDR.AAPL','BTS','CNY','USD','EUR','GOLD','SILVER','BTC', _name="deposit_currency",_id="deposit_currency",_onchange="javascript:calc_order()")),
      TR(T('Deposit amount')+':', INPUT(_id="deposit_amount",_name="deposit_amount",_onchange="javascript:calc_order();",_onkeyup="javascript:calc_order();",value=1),T('Max')+':',B(_id="deposit_limit")),
      TR(T('Withdraw currency')+':', SELECT('BDR.AAPL','BOTSCNY','BTS','CNY','USD','EUR','GOLD','SILVER','BTC', _name="withdraw_currency",_id="withdraw_currency",_onchange="javascript:calc_order()")),
      TR(T('Withdraw amount')+':', B(_id="withdraw_amount")),
      TR(T('Price')+':', B(_id="exchange_price"))),
      INPUT(_type='button', _value=T("Place Order"),  _onclick="javascript:generate_link()"),
      T('Comment')+':', TT(_id="comment"),
      DIV(_id="link_div",_style="display:none"),
      _id="fm", _name="fm")

    return dict(form=form)

def auction():
    if "market" in request.vars:
      market = request.vars['market'].upper()
    else:
      market = "BTS"
    if market == "BTC":
      asset = "TRADE.BTC"
      account = "btc.auction.btsbots"
      chanel_prefix = "auction_btc"
    elif market == "PLS":
      asset = "BTSBOTS.PLS"
      account = "pls.auction.btsbots"
      chanel_prefix = "auction_pls"
    else:
      asset = "BTS"
      account = "auction.btsbots"
      chanel_prefix = "auction"
    form = FORM(
      (T('Deposit')),
      (INPUT(_id="deposit_amount",_name="deposit_amount",_onkeyup="javascript:refresh_comment();",_onchange="javascript:refresh_comment();",value=1)),
      (SELECT(asset,'BOTSCNY','CNY','USD','EUR','GOLD','SILVER', _name="deposit_currency",_id="deposit_currency",_onchange="javascript:refresh_comment();")),
      (T('with price limit')),
      (INPUT(_id="price_limit",_name="price_limit",_onkeyup="javascript:refresh_comment();",_onchange="javascript:refresh_comment();")),
      ('CNY/'+market),
      (INPUT(_type='button', _value=T("Place Order"),  _onclick="javascript:generate_link()")),
      DIV(_id="link_div",_style="display:none"),
      P(),
      T('Comment')+':', TT(_id="comment"),
      P(),
      T('transfer ASSET if you want to sell MARKET, others for buy MARKET.').replace("ASSET",asset).replace("MARKET",market),
      _id="fm", _name="fm")
    #response.flash = T('transfer BTS if you want to sell, others for buy.')
    return dict(form=form, market=market, account=account, chanel_prefix=chanel_prefix)

def gateway():
    if "asset" in request.vars:
      asset= request.vars['asset'].upper()
    else:
      asset = "PLS"
    if asset == "PLS":
      network_a = "bts"
      network_b = "pls"
      asset_a = "BTSBOTS.PLS"
      asset_b = "PLS"
      my_account = "pls.btsbots"
    else:
      network_tom = "bts"
      network_jerry = "pls"
    form = FORM(TABLE(
      TR(T('operation:'),SELECT(T('deposit'),T('withdraw'), _name="operation",_id="operation",_onchange="javascript:refresh_comment();")),
      TR(T('amount:'),INPUT(_id="amount",_name="amount",_onkeyup="javascript:refresh_comment();",_onchange="javascript:refresh_comment();",value=1),
      TT(_id="asset"),T('Max')+':',B(_id="limit")),

      TR(T('account:'),
      INPUT(_id="account",_name="account",_onkeyup="javascript:refresh_comment();",_onchange="javascript:refresh_comment();"))),
      (INPUT(_type='button', _value=T("confirm"),  _onclick="javascript:generate_link()")),
      DIV(_id="link_div",_style="display:none"),
      T('Comment')+':', TT(_id="comment"),
      _id="fm", _name="fm")
    return dict(form=form, asset=asset, withdraw=T('withdraw'),deposit=T('deposit'),network_a=network_a,
        network_b=network_b,asset_a=asset_a,asset_b=asset_b, my_account=my_account)

def wmarket():
    return dict()

def mmaker():
    return dict()

def faq():
    return dict()

def join():
    return dict()

def error():
    return dict()

def botscny():
    return dict()
