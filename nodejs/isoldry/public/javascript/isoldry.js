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
  
  if (id == "link_references") {
    $('#description').hide();
    hide_sliders();
    $('#references-wrapper').show();
    $('#notice').show();
  }


  // hack for google map problem
  if (id == "link_contact")
    $('#map').html('<iframe width="730" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.fr/maps?f=q&amp;source=s_q&amp;hl=fr&amp;geocode=&amp;q=isoldry&amp;aq=&amp;sll=50.628597,3.030102&amp;sspn=0.038439,0.072613&amp;ie=UTF8&amp;hq=isoldry&amp;hnear=&amp;t=m&amp;ll=50.642167,3.031025&amp;spn=0.043544,0.094585&amp;z=13&amp;iwloc=A&amp;output=embed"></iframe><br /><small><a href="http://maps.google.fr/maps?f=q&amp;source=embed&amp;hl=fr&amp;geocode=&amp;q=isoldry&amp;aq=&amp;sll=50.628597,3.030102&amp;sspn=0.038439,0.072613&amp;ie=UTF8&amp;hq=isoldry&amp;hnear=&amp;t=m&amp;ll=50.642167,3.031025&amp;spn=0.043544,0.094585&amp;z=13&amp;iwloc=A" style="color:#0000FF;text-align:left">Agrandir le plan</a></small>').css('display', 'block');
	
}


// Chantiers
chantiers = [ { 
  "id" : "ilots-corot",
  "nom" : "Ilots Corot",
  "lieu" : "Calais",
  "imgs" : 5 ,
  "moeu" : "Nacarat",
  "mouv" : "I. Colas",
  "surface" : "1200m²",
  "systemes" : "Drysulation, Finition Sandpebble 1.6"
  },
  { 
  "id" : "grain-orge",
  "nom" : "Site Grain d'Orge",
  "lieu" : "Ronchin",
  "imgs" : 7,
  "moeu" : "SIA Habitat",
  "mouv" : "DFA Architectes",
  "surface" : "6000m²",
  "systemes" : "Drysulation, Finition Sandblast 1.2, Plaquettes de briques"
  },
  { 
  "id" : "carre-modes",
  "nom" : "Carré des modes",
  "lieu" : "Roubaix",
  "imgs" : 6,
  "moeu" : "Pierres et Territoires",
  "mouv" : "Ateliers 2F",
  "surface" : "5000m²",
  "systemes" : "Sandpebble 1.6, Plaquettes de briques"
  },
  {
  "id" : "marine-harvest",
  "imgs" : 6,
  "nom" : "Marine Harvest",
  "lieu" : "Boulogne-sur-Mer",
  "moeu" : "Marine Harvest",
  "mouv" : "Archifix",
  "surface" : "1500m²",
  "systemes": "Traitement K3 par projection du système Stonemist"
  }]

hide_sliders = function(){
  $('.slider-wrapper').hide()
}

init_sliders = function(){
  jQuery.each(chantiers, function(index, chantier) {
    for (i=1; i<=chantier.imgs; i++) {
      id = chantier.id
      $('#' + id + '-slider').append("<img src='img/refs/" + 
        id + 
        "/" + i + ".jpg' />");
    }
    $('#' + id + '-slider').nivoSlider();
  });
}

switch_chantier = function(chantier_id){
  jQuery.each(chantiers, function(index, chantier) {
    if (chantier_id == chantier.id) {
      // we set the right description
      jQuery.each(chantier, function(key, value) {
        $('#' + key).text(value)
      });
      $('#description').show();
      // and we display the right slider
      hide_sliders()
      $('#notice').hide();
      $('#' + chantier.id + "-wrapper").show();
    }
  })
}


// References
init_references = function() {

  jQuery.each(chantiers, function(index, chantier){
    $('#references-slider').append("<img src='img/refs/" + 
      chantier.id + 
      "/main.jpg' title='#" +
      chantier.id +
      "-caption' />");

    $('#content').append("<div class='nivo-html-caption' id='" +
      chantier.id +
      "-caption'> " + 
      "<a href=# onClick=\"switch_chantier('" + chantier.id + "');\" class='chantier-caption' >" +
      chantier.nom + " - " + chantier.systemes +
      "</a>" +
      "</div>");
  });

  $('#references-slider').nivoSlider();
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
  $('#chantier_title').corner("bl br tl tr 3px");
  
  init_sliders();
  init_references();

  $('#produits_accordion').accordion( { autoHeight: false } );

  // References 
  /*
  $('#slides').slides({
      /*generateNextPrev: true,
      generatePagination: true
      
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
  });*/
/*
  $('#go-ilot').click( function() { switch_chantier('ilots-corot')} );
  $('#go-grain').click( function() { switch_chantier('grain-orge')} );
  $('#go-rbx').click( function() { switch_chantier('carre-modes')} );

  /*
  jQuery.each(chantiers, function(index, chantier) {
    $('.ad-thumbs-list').append("<li> <a href='img/refs/" + 
      chantier.id +
      "/main.jpg'> <img src='img/refs/" +
      chantier.id + 
      "/main.jpg' /> </a> </li>")
  })

  $('.ad-gallery').adGallery();
  */
  
  //$('#ilots-corot-link').click( function() {alert('yo');});
/*
  jQuery.each(chantiers, function(index, chantier){
    $('#' + chantier.id + '-link').click( function() {alert(chantier.id);});
  });*/
});
