switch_content = function(link) {
	// we make the actual one disapear
	id = $('.selected_link').attr('id');
	$('.selected_link').removeClass('selected_link').addClass('link');
	
	content_id = id.substr(id.lastIndexOf('_') +1);
	$('#' + content_id).addClass('invisible_content');
	
	// then we display the right one
	link.addClass('selected_link');
	id = link.attr('id');
	content_id = id.substr(id.lastIndexOf('_')+1);
	$('#' + content_id).removeClass('invisible_content');

  if (id == "link_contact")
    $('#map').html('<iframe width="740" height="450" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.fr/maps?f=q&source=s_q&hl=fr&geocode=&q=8%C3%A8me+Rue,+Lille&aq=0&oq=8%C3%A8me&sll=50.62751,3.029931&sspn=0.008358,0.01929&vpsrc=0&ie=UTF8&hq=&hnear=8%C3%A8me+Rue,+59000+Lille,+Nord,+Nord-Pas-de-Calais&ll=50.62751,3.029931&spn=0.008358,0.01929&t=m&z=14&output=embed"></iframe><br /><small><a href="http://maps.google.fr/maps?f=q&source=embed&hl=fr&geocode=&q=8%C3%A8me+Rue,+Lille&aq=0&oq=8%C3%A8me&sll=50.62751,3.029931&sspn=0.008358,0.01929&vpsrc=0&ie=UTF8&hq=&hnear=8%C3%A8me+Rue,+59000+Lille,+Nord,+Nord-Pas-de-Calais&ll=50.62751,3.029931&spn=0.008358,0.01929&t=m&z=14" style="color:#0000FF;text-align:left" target="_blank">Agrandir le plan</a></small>').css('display', 'block');
	
}

$(document).ready(function() {
    $('#main').corner("bl br 6px");
    //$('#news').corner("tl br 20px");

	$('.selected_link').click( function() {
		switch_content($(this));		
	});
	$('.link').click( function() {
		switch_content($(this));		
	});
  
    $('#links').corner("bl  20px");
    $('.link').corner("br tl 6px");
});
