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
  jQuery('.lavalamp').css('left',jQuery('ul.nav li.web2py-menu-active').offset().left);
  
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
        var mi = jQuery(this).addClass('open');
        mi.children('.dropdown-menu').stop(true, true).delay(100).fadeIn(400);
    }, function(){
        var mi = jQuery(this);
        mi.children('.dropdown-menu').stop(true, true).delay(100).fadeOut(function(){mi.removeClass('open')});
    });
    jQuery('ul.nav li').hover(function(){
        var div = jQuery('.lavalamp');
        var thisli = jQuery(this);
        div.css('left',thisli.offset().left);
    }, function(){
        var div = jQuery('.lavalamp');
        var activeli = jQuery('ul.nav li.web2py-menu-active');
        div.css('left',activeli.offset().left);
    });
  }
  hoverMenu(); // first page load
  jQuery(window).resize(hoverMenu); // on resize event
  jQuery('ul.nav li.dropdown a').click(function(){window.location=jQuery(this).attr('href');});
});
