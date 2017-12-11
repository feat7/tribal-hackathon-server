$(document).ready(function(){
    $.ajax({
        url: '/api/schemes/all',
        success: function(data){
          if(data.success == true){
            var chart_id = "";
            var html = "";
            var style = "";
            for(x in data.schemes){
                chart_id = "chart_"+data.schemes[x].id;
                style = "<style>@include donut-chart('"+ chart_id +"', 94, 250px, 40px, .5s, #e1e1e1, #fff, #50C690);</style>";
                document.getElementById("styles").innerHTML += style;
                style = "";
                html += "<li>";
                html += "<div class=\"collapsible-header\">"+data.schemes[x].name+"</div>";
                html += "<div class=\"collapsible-body\"><span>"+data.schemes[x].description + "</span>";
                html += "<div class=\"donut-chart "+ chart_id +"\">";
                html += "<div class=\"quad one\"></div>";
                html += "<div class=\"quad two\"></div>";
                html += "<div class=\"quad three\"></div>";
                html += "<div class=\"quad four\"></div>";
                html += "<div class=\"quad top\"></div>";
                html += "<div class=\"chart-center\"></div>";
                html += "</div>";
                html += "<br> Department: "+ data.schemes[x].department_name +"</div>";
                html += "</li>";
                document.getElementById("schemes_tab").innerHTML += html;
            }
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