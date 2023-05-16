(function($){$('.navbar-nav > li.menu-item > a').click(function(){if($(this).attr('target')!='_blank'&&$(this).attr('class')!='dropdown-toggle')
window.location=$(this).attr('href');});$('.navbar-nav > li.menu-item > .dropdown-toggle').click(function(){if($(this).attr('target')=='_blank')
window.open(this.href);else
window.location=$(this).attr('href');});$('.dropdown').hover(function(){$(this).addClass('open');},function(){$(this).removeClass('open');});var setHeight=function(h){height=h;$("#cc_spacer").css("height",height+"px");}
$(window).resize(function(){setHeight($("#navigation_menu").height());})
$(window).ready(function(){setHeight($("#navigation_menu").height());})})(jQuery);