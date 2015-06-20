;(function(){
  var brigadeData = [];

  (function getBrigadeData(){
    var cfa = "http://codeforamerica.org/api/organizations?per_page=1000"

    $.ajax({
      url: cfa,
      success: function(data){
        data.objects.forEach(function(brigade){
          brigadeData.push({'name': brigade.name, 'projects_url': brigade.all_projects})
        })
      _getBrigadeProjects(brigadeData);
      }
    })
  }())

  function _getBrigadeProjects(brigades){
    brigades.forEach(function(brigade){
      //console.log(brigade)
      $.get(brigade.projects_url, function(projects){
        brigade["total_projects"] = projects.total.toString();
      })
    })

    setTimeout(function(){
      _cacheBrigadesToFirebase(brigadeData);
    }, 500)
  }

  function _cacheBrigadesToFirebase(){
    console.log(brigadeData)
    console.log(JSON.stringify(brigadeData));
    // $.post("https://cfn-brigadepulse.firebaseio.com/brigadeInfo.json", brigadeData ,function(data){
    //    console.log(brigadeData);
    // })
  }
})();
