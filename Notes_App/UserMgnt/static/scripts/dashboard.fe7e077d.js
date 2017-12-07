(function($)
		{
			'use strict';
			var n = document.getElementById("new").value;
			var ip = document.getElementById("ip").value;
			var c = document.getElementById("comp").value;
			var browserData=[{label:'New',data:n,color:$.urbanApp.danger},
			                 {label:'In Progress',data:ip,color:$.urbanApp.warning},
			                 {label:'Completed',data:c,color:$.urbanApp.success}];
			$.plot($('.flot-pie'),browserData,{series:{pie:{show:true,innerRadius:0.5,stroke:{width:2},label:{show:true,}}},legend:{show:true},});
			
			var tot_new = document.getElementById("tot_new").value;
			var tot_ip = document.getElementById("tot_ip").value;
			var tot_comp = document.getElementById("tot_comp").value;
			var barData=[{data:[['New',tot_new],['In Progress',tot_ip],['Completed',tot_comp]],bars:{show:true,barWidth:0.6,align:'center',fill:true,lineWidth:0,fillColor:$.urbanApp.default}}];
			$.plot($('.flot-bars'),barData,{grid:{hoverable:false,clickable:false,color:'white',borderWidth:0,},yaxis:{show:false},xaxis:{mode:'categories',tickLength:0,axisLabelUseCanvas:true,axisLabelFontSizePixels:12,axisLabelFontFamily:'Roboto',axisLabelPadding:5}});
		})
		(jQuery);
