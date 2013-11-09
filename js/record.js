$(function datePicker() {
    $.datepicker.setDefaults(
      $.extend($.datepicker.regional[""])
      );
    $("#datepicker").datepicker();
});

var loadFactions = function() {
  $('#userFaction').empty();
  $('#opponentFaction').empty();
  $.ajax({
   type: 'GET',
   url: '/data/casters.json',
   dataType : 'json',
   success : function(resp) {
             window.factionData = resp;
             for(faction in resp) {
                $('#userFaction').append('<option value="'+faction+'">'+faction+'</option>');
                $('#opponentFaction').append('<option value="'+faction+'">'+faction+'</option>');
             }
             updateUserCaster();
             updateOpponentCaster();
        }
   });
};

var loadResults = function() {
  $('#result').empty();
  $.ajax({
   type: 'GET',
   url: '/data/results.json',
   dataType : 'json',
   success : function(resp) {
             for(result in resp) {
              result = resp[result];
                $('#result').append('<option value="'+result['name']+'">'+result['name']+'</option>');
            }
        }
   });
};

var loadData = function() {
  loadResults();
  loadFactions();
  setupDropDowns();
};

var updateUserCaster = function () {
  $('#userCaster').empty();
    var faction = $('#userFaction').val();
    var casters = window.factionData[faction];
    for (caster in casters) {
      caster  = casters[caster];
      $('#userCaster').append('<option value="'+caster+'">'+caster+'</option>');
    }
};

var updateOpponentCaster = function() {
  $('#opponentCaster').empty();
    var faction = $('#opponentFaction').val();
    var casters = window.factionData[faction];
    for (caster in casters) {
      caster  = casters[caster];
      $('#opponentCaster').append('<option value="'+caster+'">'+caster+'</option>');
    }
};

var setupDropDowns = function() {
  $("#userFaction").change(function(e) {
    updateUserCaster();
  });

  $("#opponentFaction").change(function(e) {
    updateOpponentCaster();
  });
};

$( document ).ready(function() {
  loadData();
});