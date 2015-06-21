;(function(){
  var brigadeData = [];

  (function getBrigadeData(){
    var cfa = "http://codeforamerica.org/api/organizations?per_page=1000"

    $.ajax({
      url: cfa,
      success: function(data){
        data.objects.forEach(function(brigade){
          brigadeData.push({'name': brigade.name, 'city': brigade.city, 'projects_url': brigade.all_projects, 'total_projects': 'n/a'})
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
    }, 10000)
  }

  function _cacheBrigadesToFirebase(){
    JSONBrigadeData = JSON.stringify(brigadeData);
    $.ajax({
      type: 'POST', // Use POST with X-HTTP-Method-Override or a straight PUT if appropriate.
      dataType: 'json', // Set datatype - affects Accept header
      url: "https://cfn-brigadepulse.firebaseio.com/brigadeInfo.json", // A valid URL
      headers: {"X-HTTP-Method-Override": "PUT"}, // X-HTTP-Method-Override set to PUT.
      data: JSONBrigadeData // Some data e.g. Valid JSON as a string
    });
  }
})();
