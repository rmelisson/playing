switch_content = function(link) {
	// we make the actual one disapear
	id = $('.selected_link').attr('id');
	$('.selected_link').removeClass('selected_link').addClass('link');
	
	content_id = id.substr(id.lastIndexOf('_') +1);
	$('#' + content_id).addClass('invisible_content');
	
	//addClass('invisible_content');	

	// then we display the right one
	link.addClass('selected_link');
	id = link.attr('id');
	content_id = id.substr(id.lastIndexOf('_')+1);
	$('#' + content_id).removeClass('invisible_content');
	
}

$(document).ready(function(){
	$('#header').corner("tr tl 10px");		
	$('#home').corner("bl br 10px");		
	$('#links').corner("5px");		
	$('.link').corner("tl tr 12px");
	$('.selected_link').corner("tl tr 12px");
	$('.selected_link').click( function() {
		switch_content($(this));		
	});
	$('.link').click( function() {
		switch_content($(this));		
	});
});
