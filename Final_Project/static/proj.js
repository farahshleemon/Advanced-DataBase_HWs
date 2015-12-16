function SendPost()
{					          		 
    var obj = {};
    obj["Id"]=document.getElementById("ID1").value;
    obj["In"]=document.getElementById("CNumber1").value;
	obj["date"]=document.getElementById("Date1").value;
    obj["Bo"]=document.getElementById("Block1").value;
    obj["Iu"]=document.getElementById("iucr1").value;
    obj["Pt"]=document.getElementById("PT1").value;
    obj["De"]=document.getElementById("DEC1").value;
    obj["Ld"]=document.getElementById("LDEC1").value;  
    obj["Ar"]=document.getElementById("Arr1").value;
    obj["Do"]=document.getElementById("DOM1").value;
    obj["Be"]=document.getElementById("Beat1").value;
    obj["Di"]=document.getElementById("Dis1").value;
    obj["Wa"]=document.getElementById("Ward1").value;
    obj["Dis"]=document.getElementById("Distr1").value;
    obj["Co"]=document.getElementById("Com1").value;
    obj["Fb"]=document.getElementById("FB1").value;
    obj["X"]=document.getElementById("X1").value;
    obj["Y"]=document.getElementById("Y1").value;
    obj["Ye"]=document.getElementById("Ye1").value;
    obj["Up"]=document.getElementById("UP1").value;
    obj["Lat"]=document.getElementById("Lat1").value;
    obj["Lon"]=document.getElementById("Lon1").value;
    obj["Loc"]=document.getElementById("Loc1").value ;
	//console.log(JSON.stringify(obj))
    $.ajax({
            type: 'POST',
            // Provide correct Content-Type, so that Flask will know how to process it.
            contentType: 'application/json',
            // Encode data as JSON.
            data: JSON.stringify(obj),
            // This is the type of data expected back from the server.
            dataType: 'json',
            url: '/post',
            success: function (ret) {
              alert("The Document have been successfully inserted into the collection");
			  
            }
          });		  		  		   
}
function SendPostDelete()
{
	var obj = {};
    obj["CN"]=document.getElementById("CNumber2").value;
	console.log(obj)
	$.ajax({
            type: 'POST',
            // Provide correct Content-Type, so that Flask will know how to process it.
            contentType: 'application/json',
            // Encode data as JSON.
            data: JSON.stringify(obj),
            // This is the type of data expected back from the server.
            dataType: 'json',
            url: '/Deletepost',
            success: function (ret) {
              alert("The Document have been successfully deleted from the collection");
			  
            }
          });		  	
} 
function update1(obj)
{
console.log( obj["Updated On"])
	document.getElementById("ID2").value=obj["ID"];
    document.getElementById("CNumber2").value=obj["Case Number"];
	document.getElementById("Date2").value=obj["Date"];
    document.getElementById("Block2").value=obj["Block"];
    document.getElementById("iucr2").value=obj["IUCR"];
    document.getElementById("PT2").value=obj["Primary Type"];
    document.getElementById("DEC2").value=obj["Description"];
    document.getElementById("LDEC2").value=obj["Location Description"];  
    document.getElementById("Arr2").value=obj["Arrest"];
    document.getElementById("DOM2").value=obj["Domestic"];
    document.getElementById("Beat2").value=obj["Beat"];
    document.getElementById("Dis2").value=obj["District"];
    document.getElementById("Ward2").value=obj["Ward"];
    document.getElementById("Distr2").value=obj["District"];
    document.getElementById("Com2").value=obj["Community Area"];
    document.getElementById("FB2").value=obj["FBI Code"];
    document.getElementById("X2").value=obj["X Coordinate"];
    document.getElementById("Y2").value=obj["Y Coordinate"];
    document.getElementById("Ye2").value=obj["Year"];
    document.getElementById("UP2").value=obj["Updated On"];
    document.getElementById("Lat2").value=obj["Latitude"];
    document.getElementById("Lon2").value=obj["Longitude"];
    document.getElementById("Loc2").value=obj["Location"];
}
function SendPostEdit()
{
	var obj = {};
    obj["CN"]=document.getElementById("CNumberED").value;
	
	$.ajax({
            type: 'POST',
            // Provide correct Content-Type, so that Flask will know how to process it.
            contentType: 'application/json',
            // Encode data as JSON.
            data: JSON.stringify(obj),
            // This is the type of data expected back from the server.
            dataType: 'json',
            url: '/Editpost',
            success: function (ret) {
              update1(ret);
			  
            }
          });		

}

function SendPostUpdate()
{
	var obj = {};
    obj["Id"]=document.getElementById("ID2").value;
    obj["In"]=document.getElementById("CNumber2").value;
	obj["date"]=document.getElementById("Date2").value;
    obj["Bo"]=document.getElementById("Block2").value;
    obj["Iu"]=document.getElementById("iucr2").value;
    obj["Pt"]=document.getElementById("PT2").value;
    obj["De"]=document.getElementById("DEC2").value;
    obj["Ld"]=document.getElementById("LDEC2").value;  
    obj["Ar"]=document.getElementById("Arr2").value;
    obj["Do"]=document.getElementById("DOM2").value;
    obj["Be"]=document.getElementById("Beat2").value;
    obj["Di"]=document.getElementById("Dis2").value;
    obj["Wa"]=document.getElementById("Ward2").value;
    obj["Dis"]=document.getElementById("Distr2").value;
    obj["Co"]=document.getElementById("Com2").value;
    obj["Fb"]=document.getElementById("FB2").value;
    obj["X"]=document.getElementById("X2").value;
    obj["Y"]=document.getElementById("Y2").value;
    obj["Ye"]=document.getElementById("Ye2").value;
    obj["Up"]=document.getElementById("UP2").value;
    obj["Lat"]=document.getElementById("Lat2").value;
    obj["Lon"]=document.getElementById("Lon2").value;
    obj["Loc"]=document.getElementById("Loc2").value ;
	//console.log(JSON.stringify(obj))
    $.ajax({
            type: 'POST',
            // Provide correct Content-Type, so that Flask will know how to process it.
            contentType: 'application/json',
            // Encode data as JSON.
            data: JSON.stringify(obj),
            // This is the type of data expected back from the server.
            dataType: 'json',
            url: '/postUpdate',
            success: function (ret) {
              alert("The Document have been successfully updated");
			  
            }
          });		  		  		   
	
}
function go1(){
$.getJSON("/peryear", function(dat){
console.dir(dat);
DrawBarChartData(dat)});}

function DrawBarChartData(dat)
{   console.log("hi")
console.log(dat)
	var Time=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
    var Ddata = [];
    for (var i = 0; i < Time.length; i++) 
            Ddata.push({"label": Time[i].toString(), "value": parseInt(dat[Time[i]])});
      FData = [
    {
      
      key: "Cumulative Return",
	  values:Ddata
	  //area: true 
      
    }]
	draw(FData);
}
function draw(FData){
	nv.addGraph(function() {
  var chartye = nv.models.discreteBarChart()
      .x(function(da) { return da.label })    
      .y(function(da) { return da.value })
	  .showValues(true)
      .tooltips(true); 
  chartye.xAxis
	  .axisLabel('Year')
      .tickFormat(d3.format(',f'));

chartye.yAxis
     .axisLabel('Number of Crime')
     .tickFormat(d3.format(',.1f'));	  
  d3.select('#chart1 svg')
      .datum(FData)
      .call(chartye);

  nv.utils.windowResize(chartye.update);

  return chartye;
});
}
function drawTable(Result)
{
	document.getElementById("tab1").style.display = 'block';
	//console.log(typeof Result)
	
    Data=eval(Result);
	console.log(Data)
	var arr1=new Array();
    for(var c=0;c<Data.length;c++)
    {var arr = $.map(Data[c], function(el) { return el; })
     arr1.push(arr)}


	//console.log(data)
// This part of code has been modified from http://jsfiddle.net/4pEJB/
	var TDiv = document.getElementById("tab1")
    var Result_table = document.createElement('TABLE')
    var table_Body = document.createElement('TBODY')

    Result_table.border = '1'
    Result_table.appendChild(table_Body);
	 //var h = ['ID','Case Number','Date','Block','IUCR','Primary Type','Description','Location Description','Arrest','Domestic','Beat','District','Ward','Community Area','FBI Code','X Coordinate','Y Coordinate','Year','Updated On','Latitude','Longitude','Location']   
	//Header
	var h= Object.keys(Data[0])
    var TableR = document.createElement('TR');
    table_Body.appendChild(TableR);
    for (var i = 0; i < h.length; i++) {
        var th = document.createElement('TH')
        th.width = '75';
        th.appendChild(document.createTextNode(h[i]));
        TableR.appendChild(th);
    }

    //Results
    for (i = 0; i < arr1.length; i++) {
        var tr = document.createElement('TR');
		table_Body.appendChild(tr);
        for (j = 0; j < arr1[i].length; j++) {
			//console.log(arr1[i][j])
            var td = document.createElement('TD')
            td.width = '75';
			td.appendChild(document.createTextNode(arr1[i][j]));
			tr.appendChild(td);}
    TDiv.appendChild(Result_table)
}
}
function SendYear()
{
	var obj = {};
    obj["Year"]=document.getElementById("Year").value;
	
	$.ajax({
            type: 'POST',
            // Provide correct Content-Type, so that Flask will know how to process it.
            contentType: 'application/json',
            // Encode data as JSON.
            data: JSON.stringify(obj),
            // This is the type of data expected back from the server.
            dataType: 'json',
            url: '/Yearpost',
            success: function (ret) {
              drawTable(ret["r"]);
			  //console.log(ret["r"])
			  
            }
          });		

}
function go2(){
$.getJSON("/peryear2", function(dat){
console.dir(dat);
DrawGroupedBarChart(dat)
});} 

//Grouped And Stacked Bar Chart===============================================================================================================================
function DrawGroupedBarChart(data){
	var Time=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]
    ChartData=[];
	for (var key in data){
	var Ddata = [];
	
    for (var i = 0; i < Time.length; i++) 
            
		Ddata.push({x: Time[i].toString(), y: parseInt(data[key][Time[i]])});
      FData = 
    {
      
      key: key,
	  values:Ddata
	  //area: true 
      
    }
	ChartData.push(FData)
	}
nv.addGraph(function() {
   var chart = nv.models.multiBarChart()
						.margin({left: 100})  //Adjust chart margins to give the x-axis some breathing room.
                        .rotateLabels(0)      //Angle to rotate x-axis labels.
                        .showControls(true)   //Allow user to switch between 'Grouped' and 'Stacked' mode.
                        .groupSpacing(0.3)    //Distance between each group of bars.
						;

 chart.xAxis
	  .axisLabel('Year')
      .tickFormat(d3.format(',f'));

chart.yAxis
     .axisLabel('Count')
     .tickFormat(d3.format(',.1f'));

d3.select('#chart2 svg')
  .datum(ChartData)
  .call(chart);

nv.utils.windowResize(chart.update);
return chart;
});
}