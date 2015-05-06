// this code improves bootstrap menus and adds dropdown support
jQuery(function(){
  jQuery('.nav>li>a').each(function(){
    if(jQuery(this).parent().find('ul').length)
      jQuery(this).attr({'class':'dropdown-toggle','data-toggle':'dropdown'}).append('<b class="caret"></b>');
  });
  jQuery('.nav li li').each(function(){
    if(jQuery(this).find('ul').length)
      jQuery(this).addClass('dropdown-submenu');
  });
  
  //lavalamp
  var lavalamp = jQuery('.navbar .lavalamp');
  if(location.href.indexOf('gateway')>0) {
    jQuery('li.dropdown ul.dropdown-menu a[href="/btsbots_exchange/default/gateway?asset=PLS"]')
    .parents('li.dropdown').addClass('web2py-menu-active');
  }
  lavalamp.css('left',jQuery('ul.nav li.web2py-menu-active').offset().left);
  lavalamp.fadeIn();
  
  function adjust_height_of_collapsed_nav() {
        var cn = jQuery('div.collapse');
        if (cn.get(0)) {
            var cnh = cn.get(0).style.height;
            if (cnh>'0px'){
                cn.css('height','auto');
            }
        }
  }
  function hoverMenu(){
    jQuery('ul.nav a.dropdown-toggle').parent().hover(function(){
        adjust_height_of_collapsed_nav();
        var mi = jQuery(this).addClass('open open-back');
        //mi.children('.dropdown-toggle').css('background-color','#aaa');
        mi.children('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
    }, function(){
        var mi = jQuery(this);
        //mi.children('.dropdown-toggle').css('background-color','transparent');
        mi.removeClass('open-back');
        mi.children('.dropdown-menu').stop(true, true).delay(200).fadeOut(0,function(){mi.removeClass('open')});
    });
    //lavalamp
    jQuery('ul.nav li').hover(function(){
        var div = jQuery('.navbar .lavalamp');
        var thisli = jQuery(this);
        div.css('left',thisli.offset().left);
    }, function(){
        var div = jQuery('.navbar .lavalamp');
        var activeli = jQuery('ul.nav li.web2py-menu-active');
        div.css('left',activeli.offset().left);
    });
  }
  hoverMenu(); // first page load
  jQuery(window).resize(hoverMenu); // on resize event
  jQuery('ul.nav li.dropdown a').click(function(){
    jQuery('.web2py-menu-active').removeClass('web2py-menu-active');
    jQuery(this).parents('li.dropdown').addClass('web2py-menu-active');
    window.location=jQuery(this).attr('href');    
  });
});
