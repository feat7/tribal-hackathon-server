$(document).ready(function(){
    $.ajax({
        url: '/api/schemes/all',
        success: function(data){
          if(data.success == true){
            
            for(x in data.schemes){
                document.getElementById("plans_display").innerHTML += "<li class=\"collection-item\">"+data.schemes[x].name+"</li>";
            }
            
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
            
            for(x in data.schemes){
                document.getElementById("budget_display").innerHTML += "<li class=\"collection-item\">"+data.schemes[x].name+"</li>";
            }
            
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
            
            for(x in data.announcements){
                document.getElementById("circulars_display").innerHTML += "<li class=\"collection-item\">"+data.announcements[x].name+"</li>";
            }
            
          }else{
            document.getElementById("circulars_display").innerHTML += '<div class=row><div class="col-sm-12" >No Updates</div></div></br>';
          }
        },
        error: function(){
          alert('Sorry an error occured while loading schemes');
          console.log('AJAX call not successfull');
        }
    });
});