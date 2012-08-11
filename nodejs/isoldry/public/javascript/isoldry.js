// Content 
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
  
  // hack for google map problem
  if (id == "link_contact")
    $('#map').html('<iframe width="730" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.fr/maps?f=q&amp;source=s_q&amp;hl=fr&amp;geocode=&amp;q=isoldry&amp;aq=&amp;sll=50.628597,3.030102&amp;sspn=0.038439,0.072613&amp;ie=UTF8&amp;hq=isoldry&amp;hnear=&amp;t=m&amp;ll=50.642167,3.031025&amp;spn=0.043544,0.094585&amp;z=13&amp;iwloc=A&amp;output=embed"></iframe><br /><small><a href="http://maps.google.fr/maps?f=q&amp;source=embed&amp;hl=fr&amp;geocode=&amp;q=isoldry&amp;aq=&amp;sll=50.628597,3.030102&amp;sspn=0.038439,0.072613&amp;ie=UTF8&amp;hq=isoldry&amp;hnear=&amp;t=m&amp;ll=50.642167,3.031025&amp;spn=0.043544,0.094585&amp;z=13&amp;iwloc=A" style="color:#0000FF;text-align:left">Agrandir le plan</a></small>').css('display', 'block');
	
}


// Chantiers
chantiers = [ { 
  "id" : "ilots-corot",
  "nom" : "Ilots Corot",
  "lieu" : "Calais",
  "imgs" : 4 ,
  "moeu" : "Nacarat",
  "mouv" : "I. Colasse",
  "surface" : "1200m²",
  "systemes" : "Dry Solution, Finition Sampable 1.6"
  },
  { 
  "id" : "grain-orge",
  "nom" : "Site Grain d'Orge",
  "lieu" : "Ronchin",
  "imgs" : 4,
  "moeu" : "SIA Habitat",
  "mouv" : "DFA Architectes",
  "surface" : "6000m²",
  "systemes" : "Dry Solution, Finition Sandblast 1.2, Plaquettes de briques"
  },
  { 
  "id" : "carre-modes",
  "nom" : "Carré des modes",
  "lieu" : "Roubaix",
  "imgs" : 4,
  "moeu" : "Pierres etTterritoires",
  "mouv" : "Ateliers 2F",
  "surface" : "5000m²",
  "systemes" : "Sampable 1.6, Plaquettes de briques"
  } ]

switch_chantier = function(chantier_id){
  jQuery.each(chantiers, function(index, chantier) {
    if (chantier_id == chantier.id) {
      jQuery.each(chantier, function(key, value) {
        $('#' + key).text(value)
      })
      //for (i=1, i<chantier.imgs, i++){}
    }
  })
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
  
  // References 
  $('#slides').slides({
      /*generateNextPrev: true,
      generatePagination: true
      */
      play: 7000,
      generateNextPrev: false,
      generatePagination: false,
      preload: true,
      preloadImage: 'img/loading.gif'
  });

  $('#slides_all').slides({
      generateNextPrev: false,
      generatePagination: false,
      play: 5000
  });

  $('#go-ilot').click( function() { switch_chantier('ilots-corot')} );
  $('#go-grain').click( function() { switch_chantier('grain-orge')} );
  $('#go-rbx').click( function() { switch_chantier('carre-modes')} );

});
