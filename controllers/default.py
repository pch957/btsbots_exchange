# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    form = FORM(
      DIV(
      DIV(
          DIV(T('Deposit currency')+':',_class='float_l fw div-lable'),
          DIV(
          SELECT('BOTSCNY','BDR.AAPL','BTS','CNY','USD','EUR','GOLD','SILVER','BTC', _name="deposit_currency",_id="deposit_currency",_onchange="javascript:calc_order()"),
          _class='div-select',
          _id='sendasset'
          ),
          _class='con'
      ),
      DIV(
         DIV(T('Deposit amount')+':',_class='float_l fw div-lable'),
         INPUT(_id="deposit_amount",_name="deposit_amount",_onchange="javascript:calc_order();",_onkeyup="javascript:calc_order();",value=1,_class='input-xlarge'),
         T('Max')+':',SPAN(_id="deposit_limit"),
         _class='con fw'
      ),
      DIV(
        DIV(T('Withdraw currency')+':',_class='float_l fw div-lable'),
        DIV(
            SELECT('BDR.AAPL','BOTSCNY','BTS','CNY','USD','EUR','GOLD','SILVER','BTC', _name="withdraw_currency",_id="withdraw_currency",_onchange="javascript:calc_order()"),
            _id='getasset',
            _class='div-select'
        ),
        _class='con'
      ),
      DIV(T('Withdraw amount')+':',SPAN(_id="withdraw_amount"), T('Price')+':', SPAN(_id="exchange_price"),_class='con'),
      INPUT(_class='btn btn-success',_type='button',  _value=T("Place Order"),  _onclick="javascript:generate_link()"),
      DIV(T('Comment')+':', TT(_id="comment")), _class="left"),
      DIV(DIV(_id="qrcode"), _class="right"),
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
      account = "bts.auction.btsbots"
      chanel_prefix = "auction"
    form = FORM(
        DIV(DIV(
        DIV(T('Deposit'), _class='float_l fw',_style='margin:0 5px 0 0'),
        DIV(INPUT(_id="deposit_amount",_name="deposit_amount",_onkeyup="javascript:refresh_comment();",_onchange="javascript:refresh_comment();",value=1), _class='float_l fw'),
        DIV(SELECT(asset,'BOTSCNY','CNY','USD','EUR','GOLD','SILVER', _name="deposit_currency",_id="deposit_currency",_onchange="javascript:refresh_comment();"),
        _id='sendasset',_class='div-select',_style='width:120px'
        ),
        DIV(T('with price limit'),_class='float_l fw',_style='margin:0 5px;'),
        DIV(INPUT(_id="price_limit",_name="price_limit",_onkeyup="javascript:refresh_comment();",_onchange="javascript:refresh_comment();"), _class='float_l fw'),
        DIV('CNY/'+market,_class='float_l fw',_style='margin:0 5px;'),
        DIV(INPUT(_type='button',_class='btn-success', _value=T("Place Order"),  _onclick="javascript:generate_link()",_style='margin-bottom: 8px;'),_class='float_l fw'),
        DIV(_id="link_div",_style="display:none"),
        _class='con'
        ),
        DIV(
          P(),
          SPAN(T('Comment')+':',_class='label label-info', _style='margin-right:5px;'), TT(_id="comment"),
          P(),
          T('transfer ASSET if you want to sell MARKET, others for buy MARKET.').replace("ASSET",asset).replace("MARKET",market)
        ), _class="left"),
      DIV(DIV(_id="qrcode"), _class="right"),
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
    form = FORM(
      DIV(
        DIV(T('operation:'),_class='float_l fw', _style='width:40px;'),
          DIV(SELECT(T('deposit'),T('withdraw'), _name="operation",_id="operation",_onchange="javascript:refresh_comment();"),
          _id='operation_div',
          _class='div-select'),
        _class='con'
      ),
      DIV(
        DIV(T('amount:'),_class='float_l fw', _style='width:40px;'),
        INPUT(_id="amount",_name="amount",_class='input-xlarge',_onkeyup="javascript:refresh_comment();",_onchange="javascript:refresh_comment();",value=1),
        TT(T('Max')+':', _id="asset"),B(_id="limit"),
        _class='con'
        ),

      DIV(
         DIV(T('account:'),_class='float_l fw', _style='width:40px;'),
        INPUT(_id="account",_name="account",_class='input-xlarge',_onkeyup="javascript:refresh_comment();",_onchange="javascript:refresh_comment();"),
        _class='con fw'),
      DIV(INPUT(_type='button',_class='btn-success', _value=T("confirm"),  _onclick="javascript:generate_link()"),_class='con'),
      DIV(_id="link_div",_style="display:none"),
      DIV(T('Comment')+':', TT(_id="comment"),_class='con'),
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
