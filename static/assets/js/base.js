$(document).ready(function(){
    $.ajax({
        url: '/api/schemes/all',
        success: function(data){
          if(data.success == true){
            var html = "";
            for(x in data.schemes){
                 html += "<li class=\"collection-item\">"+data.schemes[x].name+"</li>";
            }
            document.getElementById("plans_display").innerHTML = html
          }else{
            document.getElementById("plans_display").innerHTML += '<div class=row><div class="col-sm-12" >No Updates</div></div></br>';
          }
        },
        error: function(){
          alert('Sorry an error occured while loading schemes');
          console.log('AJAX call not successfull');
        }
    });
    $.ajax({
        url: '/api/schemes/all',
        success: function(data){
          if(data.success == true){
            var html = "";
            for(x in data.schemes){
                html += "<li class=\"collection-item\">"+data.schemes[x].name+"</li>";
            }
            document.getElementById("budget_display").innerHTML = html;
          }else{
            document.getElementById("budget_display").innerHTML += '<div class=row><div class="col-sm-12" >No Updates</div></div></br>';
          }
        },
        error: function(){
          alert('Sorry an error occured while loading schemes');
          console.log('AJAX call not successfull');
        }
    });
    $.ajax({
        url: '/api/announcements/all',
        success: function(data){
          if(data.success == true){
            var html = "";  
            for(x in data.announcements){
                html += "<li class=\"collection-item\">"+data.announcements[x].name+"</li>";
            }
            document.getElementById("circulars_display").innerHTML = html
          }else{
            document.getElementById("circulars_display").innerHTML += '<div class=row><div class="col-sm-12" >No Updates</div></div></br>';
          }
        },
        error: function(){
          alert('Sorry an error occured while loading schemes');
          console.log('AJAX call not successfull');
        }
    });
    $("#progress_bar").hide();
});