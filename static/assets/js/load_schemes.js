$(document).ready(function(){
    $.ajax({
        url: '/api/schemes/all',
        success: function(data){
          if(data.success == true){
            var html = "";
            for(x in data.schemes){
                html += "<li>";
                html += "<div class=\"collapsible-header\">"+data.schemes[x].name+"</div>";
                html += "<div class=\"collapsible-body\"><span>"+data.schemes[x].description + "</span>";
                html += "<br> Department: "+ data.schemes[x].department_name +"</div>";
                html += "</li>";
            }
            document.getElementById("schemes_tab").innerHTML = html;
          }else{
            document.getElementById("schemes_tab").innerHTML += '<div class=row><div class="col-sm-12" >No Updates</div></div></br>';
          }
        },
        error: function(){
          alert('Sorry an error occured while loading schemes');
          console.log('AJAX call not successfull');
        }
    });
    $("#progress_bar").hide();
    $('.collapsible').collapsible();
});