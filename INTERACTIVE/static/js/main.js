$(document).ready(function() {
    console.log("Works! Updated");
   
    $("#knnTest").click(function() {
        console.log("ANDA???");
        var numberK = $('#knnValue').val();
        if (numberK){
            console.log("K is a number "+numberK);
            calllService("GET","http://localhost:5000/classify/knn?k="+numberK,knnSuccess,knnFailed);
        } else {
            console.log("K is not a number error");
            knnFailed("Please try again...")
        }
    });

    $("#clusSubmit").click(function() {
        console.log("ANDA???");
        var numberK = $('#clusK').val();
        if (numberK){
            console.log("K is a number "+numberK);
            calllService("GET","http://localhost:5000/cluster/knnMeans?k="+numberK,clusSuccess,clusFailed);
        } else {
            console.log("K is not a number error");
            clusFailed("Please try again...")
        }
    });

    $("#treeSubmit").click(function() {
        console.log("ANDA???");
        calllService("GET","http://localhost:5000/classify/tree",treeSuccess,treeFailed);
    });

    $( "#songName" ).keypress(function( event ) {
        console.log("On key press???");
        songQuery = $('#songName').val();
        $('#songSuggestions').empty();
        if (songQuery.length > 3) {
            calllService("GET", "http://localhost:5000/search/track?q="+songQuery,searchSuccess,searchFailed);
        }
    });

    $("#classifySong").click(function() {
        console.log(" va ANDA???");
        var songId = $('option[value="'+$("#songName").val()+'"]').attr("data_value");
        console.log("Es song Id "+songId);
        if (songId){
            console.log("K is a number "+songId);
            calllService("GET","http://localhost:5000/classify/song?songId="+songId,songCatSuccess,songCatFailed);
        } else {
            console.log("K is not a number error");
            songCatFailed("Please try again...")
        }
    });

    console.log("IS GOING TO CALL A SERVICE!!!!");
    calllService("GET","http://localhost:5000/data/describe",dataDescribeSuccess,dataDescribeFailure);

});
function songCatSuccess(value) {
    $('#songClassResult').text("According to the Tree Classifier the song is: "+ value);
}

function songCatFailed(value) {
    $('#songClassResult').text(value);   
}

function searchSuccess(value) {
    console.log(value);
    if (value) {
        for (var i = 0; i < value.length; i++) { 
            console.log("Adding option?? "+value[i].name);
            if (i < 10) {
                $('#songSuggestions').append("<option data_value = '"+value[i].id+"'' value='" + value[i].name + "'>");    
            }
            
        }   
    }
}
function searchFailed(value) {

}
function knnSuccess(value){	
    $('#knnResult').text("Accuracy: "+ value);
}
function knnFailed(value){
    $('#knnResult').text(value);
}

function clusSuccess(value){ 
    console.log(value);
    $('#clusHom').text("Homogenity: "+ value.homgenity);
    $('#clusCom').text("Completeness: "+ value.completeness);
    var jsonList = value.listOfClusters;
    var tableHTML = "<table class='table-bordered'>";

    for (var i = 0; i < jsonList.length; i++) { 
        clusterJson = jsonList[i];
        tableHTML += "<tr><th>Cluster "+clusterJson.clusterId+" has "+clusterJson.numberOfTracks+" tracks</th></tr>";
        tableHTML += "<tr><th>Track Name</th><th>Listen</th></tr>";
        for (var m = 0; m < clusterJson.top5.length; m++) {     
            trackJson = clusterJson.top5[m];
            audioPlugin = "<audio src='"+trackJson.url+"' controls> Your browser does not support the audio element</audio>";
            tableHTML += "<tr><td>"+trackJson.name+"</td><td>"+audioPlugin+"</td></tr>";
        }
    }
    tableHTML += "</table>";
    $("#clusteringResults").html(tableHTML);

}
function clusFailed(value){
    $('#clusHom').text(value);
    $('#clusCom').text("");
}

function treeSuccess(value){ 
    $('#treeResult').text("Accuracy: "+ value);
}
function treeFailed(value){
    $('#treeResult').text(value);    
}

function dataDescribeSuccess(value) {
    var columnsNames = value.columnTitles;
    var rowNames = value.rowTitles;
    var data = value.data;

    var tableHTML = "<table class='table-bordered'><thead>";
    tableHTML += "<th>#</th>";
    for (var h = 0 ; h < columnsNames.length; h++){
        console.log("H "+h);
        hed = columnsNames[h];
        tableHTML += "<th>"+hed+"</th>"
    }
    tableHTML += "</thead><tbody>";
    // var rowIndex = 0;
    for (var r = 0; r < rowNames.length; r++) { 
        console.log("R "+r);
        tableHTML += "<tr><td>"+rowNames[r]+"</td>";
        for (var c = 0; c < columnsNames.length; c++) { 
            console.log("C "+c);
            console.log("Va -->"+data[r][c]+"<---");
            tableHTML += "<td>"+data[r][c]+"</td>";
        }
        tableHTML += "</tr>";
        console.log(tableHTML)
        // rowIndex +=1;
    }
    tableHTML += "</tbody></table>";
    $("#table-describe").html(tableHTML);

}
function dataDescribeFailure(value) {
    console.log(value);
}

function calllService(method, url, success, failure){
	console.log("va a llamar a un servicio "+url);
	$.ajax({
        type: "GET",
        url: url,
        success: function(msg) {
        	console.log("Servicio success "+msg);
            success(msg);
        },
        error: function(e){
            console.log("error");
        }
    });
}