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

$("button#sub").click(function () {

	$.ajax({
		type: 'post',
		contentType: "application/json; charset=UTF-8",
		url: "/Command/",
		dataType: 'json',
		data:JSON.stringify({
				'host': 	    $("input#host").val(),
				'module_name':  $("input#module_name").val(),
				'module_args':	$("input#module_args").val(),
			}),
		success:function (data) {
			if(data.status == "success"){
				// alert(data.success);
				$("#p2").append("<p><h5>SuccessHosts：</h5>");
                for(var i = 0; i < data.successHosts.length; i++){
                    $("#p2").append("<li>"+data.successHosts[i]+"</li>");

                }
                $("#p2").append("</p><br/>");
                $("#p2").append("<p><h5>FailedsHosts：</h5>");
                for(var i = 0; i < data.failedHosts.length; i++){
                    $("#p2").append("<li>"+data.failedHosts[i]+"</li>");

                }
                $("#p2").append("</p><br/>");
                $("#p2").append("<p><h5>UnreachableHosts：</h5>");
                for(var i = 0; i < data.unreachableHosts.length; i++){
                    $("#p2").append("<li>"+data.unreachableHosts[i]+"</li>");

                }
                $("#p2").append("</p><br/>");
				$("#p2").append("<h5>HostDetails:</h5><br/>");
                    // $("#p2").append(data.hosts+"<br/>");
                    // $("#p2").append(data.hosts[0]['stdout']+"<br/>");
                for(let jsondata in data.hosts){
                    $("#p2").append("<p>"+jsondata+"===>>"+JSON.stringify(data.hosts[jsondata])+"</p><br/>");
                }

                $("#p2").append('================分割===================');

			}else if(data.status == "fail"){
				$("#p2").append('程序就没执行吧？老铁！');
			}
        }
	});
});
/**
 * Created by qius on 2018/7/19.
 */

$("button#fileDo").click(function () {

	$.ajax({
		type: 'post',
		contentType: "application/json; charset=UTF-8",
		url: "/FileDo/",
		dataType: 'json',
		data:JSON.stringify({
				'host': $(".host").val(),
				'src':  $("input#src").val(),
				'dest':	$("input#dest").val(),
			}),

		success:function (data) {
			if(data.status == "success"){
				// alert(data.success);
				$("#p2").append("<p><h5>SuccessHosts：</h5>");
                for(var i = 0; i < data.successHosts.length; i++){
                    $("#p2").append("<li>"+data.successHosts[i]+"</li>");

                }
                $("#p2").append("</p><br/>");
                $("#p2").append("<p><h5>FailedsHosts：</h5>");
                for(var i = 0; i < data.failedHosts.length; i++){
                    $("#p2").append("<li>"+data.failedHosts[i]+"</li>");

                }
                $("#p2").append("</p><br/>");
                $("#p2").append("<p><h5>UnreachableHosts：</h5>");
                for(var i = 0; i < data.unreachableHosts.length; i++){
                    $("#p2").append("<li>"+data.unreachableHosts[i]+"</li>");

                }
                $("#p2").append("</p><br/>");
				$("#p2").append("<h5>HostDetails:</h5><br/>");
                    // $("#p2").append(data.hosts+"<br/>");
                    // $("#p2").append(data.hosts[0]['stdout']+"<br/>");
                for(let jsondata in data.hosts){
                    $("#p2").append("<p>"+jsondata+"===>>"+JSON.stringify(data.hosts[jsondata])+"</p><br/>");
                }

                $("#p2").append('================分割===================');

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



