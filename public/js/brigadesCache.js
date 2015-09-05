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
    brigadeDetailsPromises = []
    brigades.forEach(function(brigade){
      //console.log(brigade)
      var promise = $.get(brigade.projects_url, function(projects){
        brigade["total_projects"] = projects.total.toString();
      })
      brigadeDetailsPromises.push(promise);
    })

    // Wait until all the $.get requests have resolved before
    // saving the data back to firebase.
    $.when.apply(this, brigadeDetailsPromises).done(function(){
      console.log("Caching Brigade API data to https://cfn-brigadepulse.firebaseio.com/brigadeInfo.json");
      _cacheBrigadesToFirebase(brigadeData);
    });
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
