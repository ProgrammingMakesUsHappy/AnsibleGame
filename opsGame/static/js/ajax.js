/**
 * function 7-31 ajax refresh
 */
function refresh() {
    $.ajax({
        type: 'get',
        contentType: "application/json; charset=UTF-8",
        url: "/getargs/",
        dataType: 'json',
        success: function (data) {
            $("p#group").text(data['groupCount']);
            $("p#run").text(data['alive']);
            $("p#stop").text(data['offline']);
            $("p#cmdCount").text(data['cmdCount']);
            for (var i = 0, len = data['groupList'].length; i < len; i++) {
                // alert(data['groupList'][i]);
                var hostNum = data[data['groupList'][i] + '_on'] + data[data['groupList'][i] + '_off'];
                var onPercent = (data[data['groupList'][i] + '_on'] / hostNum) * 100;
                var offPercent = (data[data['groupList'][i] + '_off'] / hostNum) * 100;
                var onStr = onPercent.toString() + '%';
                var offStr = offPercent.toString() + '%';
                $("#" + data['groupList'][i] + '-on').css("width", onStr);
                $("#" + data['groupList'][i] + '-off').css("width", offStr);
                $("#" + data['groupList'][i] + '-content').text(data[data['groupList'][i] +'_off_host']);            }
            ;
        }
    });
};
/**
 * Created by qius on 2018/7/18.
 */

$("input#commandsub").click(function () {
    if(($("input#module_name").val() != '') || $(".module").val().toString() == 'DIY'){
        var moduleName = $("input#module_name").val();
    }else {
        moduleName = $(".module").val().toString();
    };

	$.ajax({
		type: 'post',
		contentType: "application/json; charset=UTF-8",
		url: "/Command/",
		dataType: 'json',
		data:JSON.stringify({
				'host': 	    $(".host").val().toString(),
				'module_name':  moduleName,
				'module_args':	$("input#module_args").val(),
			}),
		success:function (data) {
			if(data.status == "success"){
				$("#p2").append("<h5 style='color: #40e829'>SuccessHosts：</h5><ul>");
                for(var i = 0; i < data.successHosts.length; i++){
                    $("#p2").append("<li>"+data.successHosts[i]+"</li>");

                }
                $("#p2").append("</ul><br/>");
                $("#p2").append("<h5 style='color: #ea0e1f'>FailedsHosts：</h5><ul>");
                for(var i = 0; i < data.failedHosts.length; i++){
                    $("#p2").append("<li>"+data.failedHosts[i]+"</li>");

                }
                $("#p2").append("</ul><br/>");
                $("#p2").append("<h5 style='color: #c0b93d'> UnreachableHosts：</h5><ul>");
                for(var i = 0; i < data.unreachableHosts.length; i++){
                    $("#p2").append("<li>"+data.unreachableHosts[i]+"</li>");

                }
                $("#p2").append("</ul><br/>");
				$("#p2").append("<h5 style='color: #eea236'>HostDetails:</h5> <ul><br/>");
                    // $("#p2").append(data.hosts+"<br/>");
                    // $("#p2").append(data.hosts[0]['stdout']+"<br/>");

                for(let jsondata in data.hosts){
                    $("#p2").append("<p style='color: #46b8da'>"+jsondata+"</p>");
                    $("#p2").append("<text style='color:orangered'>"+JSON.stringify(data.hosts[jsondata])+"</text><br/>");
                }
                $("#p2").append("</ul><br/>");

                $("#p2").append('<h3 style="text-align: center">=======================分割========================</h3>');

			}else if(data.status == "fail"){
				$("#p2").append('程序就没执行吧？老铁！');
			}
        }
	});
});
/**
 * Created by qius on 2018/7/19.
 */

$("input#fileDo").click(function () {

	$.ajax({
		type: 'post',
		contentType: "application/json; charset=UTF-8",
		url: "/FileDo/",
		dataType: 'json',
		data:JSON.stringify({
				'host': $(".host").val().toString(),
				'src':  $("input#src").val(),
				'dest':	$("input#dest").val(),
			}),
		success:function (data) {
			if(data.status == "success"){
				$("#p2").append("<h5 style='color: #40e829'>SuccessHosts：</h5><ul>");
                for(var i = 0; i < data.successHosts.length; i++){
                    $("#p2").append("<li>"+data.successHosts[i]+"</li>");

                }
                $("#p2").append("</ul><br/>");
                $("#p2").append("<h5 style='color: #ea0e1f'>FailedsHosts：</h5><ul>");
                for(var i = 0; i < data.failedHosts.length; i++){
                    $("#p2").append("<li>"+data.failedHosts[i]+"</li>");

                }
                $("#p2").append("</ul><br/>");
                $("#p2").append("<h5 style='color: #c0b93d'> UnreachableHosts：</h5><ul>");
                for(var i = 0; i < data.unreachableHosts.length; i++){
                    $("#p2").append("<li>"+data.unreachableHosts[i]+"</li>");

                }
                $("#p2").append("</ul><br/>");
				$("#p2").append("<h5 style='color: #eea236'>HostDetails:</h5> <ul><br/>");
                    // $("#p2").append(data.hosts+"<br/>");
                    // $("#p2").append(data.hosts[0]['stdout']+"<br/>");

                for(let jsondata in data.hosts){
                    $("#p2").append("<p style='color: #46b8da'>"+jsondata+"</p>");
                    $("#p2").append("<text style='color:orangered'>"+JSON.stringify(data.hosts[jsondata])+"</text><br/>");
                }
                $("#p2").append("</ul><br/>");

                $("#p2").append('<h3 style="text-align: center">=======================分割========================</h3>');

			}else if(data.status == "fail"){
				$("#p2").append('程序就没执行吧？老铁！');
			}
        }
	});
});

/**
 * Created by qius on 2018/7/27.
 */
 // 更新进度条
$("button#refresh").click(function (){
    refresh();
});




/**
 * Created by qius on 2018-07-30
 */
$("div#accordion").accordion();



