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
				'host': 	    $("input#host").val(),
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