$(document).ready(function(){
	$("body").css({
		"min-width":window.screen.width,
	});
	$(".item").each(
		function(){
			var result = {
				"1":"pass",
				"2":"fail",
				"0":"ongoing",
				"3":"modified"
			}
			var index = $(this).attr("result");
			$(this).find(".seal").css("background-image","url('/static/Material/icon-"+result[index]+".jpg");

			$(this).find(".seal").css(
				"background-repeat","no-repeat"
		)

})
	$("#datePicker").dateDropper({
		format:'Y-m-d',
		color:'#f87a54',
		animation:'bounce',
		init_animation:'bounce',
		maxYear:'2025',
		minYear:'2015',
		yearsRange:'5',
	});

	$("div.header_filt p").click(function(){
		$(".items").attr("status",$(this).attr("status"));
		$("div.header_filt p").css({
			"color":"black",
			"bottom":"0"
		})
		$(this).css({
			"color":"#0bc7b4",
			"bottom":"23%"
		})
		$(".choosed_filter").remove();
		$(".number").remove();
		var div1 = $("<div class='choosed_filter'></div>")
		div1.css({
			"width":"7.5%",
			"height":"4px",
			"background-color":"#0bc7b4",
			"position":"absolute",
			"top":"0"
		})
		$(this).before(div1);
		
		
		var status=$(this).attr("status")
		var number=0;
		$(".item").hide()
		$(".item").each(function(){
			if(status.indexOf($(this).attr('result'))>=0){
				$(this).show();
				number++;
			}
		})
		var str = "<div class='number'>" + number + "</div>";
		var div2 = $(str);	
		div2.css({
			"width":"20px",
			"height":"20px",
			"font-size":"14px",
			"background-color":"#0bc7b4",
			"border-radius":"100px",
			"color":"#ffffff",
			"position":"relative",
			"left":"70%",
			"top":"20%",
			"text-align":"center"
		})
		$(this).before(div2);
		$("#type-filter").val("all");
		$("#datePicker").val("");
		$("#time-clear").css("display","none");
		$("#print-filter").val("all");
	})
})






	function eachformDownload(buttons,option){
		var i=buttons.length;
		var interval=setInterval(function(){
			//alert("i="+i);
			if (i==0) {
				clearInterval(interval);
			}else{
			formDownload($(buttons[i-1]),option);
			}
			i--;
		},1000);	
	}

	function formDownload(button,option){
		var item;
		if(option==1){
			item = button.parents("#approve");
		}
		else{
			item = button.parents("div.item");
		}
		var form = document.getElementById("form");
		$(form).attr("action","/Material/download/form");
		$("#type").val(item.attr("mtype"));
		$("#id").val(item.attr("uid"));
		form.submit();
	

		$(form).attr("action",null);
		$("#type").val(null);
		$("#id").val(null);
		//alert("开始下载"+item);
		
	}


/*
		function formDownloadTest(buttons,option){
			buttons.each(function(){
				var item=$(this);
				item.text('helloworld');
			})
		}

*/		


	function schemeDownload(button,option){
		var item;
		if(option==1){
			item = button.parents("#approve")
		}
		else{
			item = button.parents("div.item")
		}
		var form = document.getElementById("form");
		$(form).attr("action","/Material/download/scheme");
		$("#type").val(item.attr("mtype"));
		$("#id").val(item.attr("uid"));
		form.submit();

		$(form).attr("action",null);
		$("#type").val(null);
		$("#id").val(null);
		//alert("开始下载"+item);

	}

	function eachSchemeDownload(buttons,option){
		var i=buttons.length;
		var interval=setInterval(function(){
		//	alert("i="+i);
			if (i==0) {
				clearInterval(interval);
			}else{
			schemeDownload($(buttons[i-1]),option);
			}
			i--;
		},1000);	
	}





	function getModal(button){

		var item = button.parents("div.item");

		var htmlobj=$.ajax({
			url:"/Material/modal/",
			type:"post",
			data:{
				id:item.attr("uid"),
				type:item.attr("mtype"),
				modal_type:"approve"
			},
			async:false,
		});

		$("#modal-approve").html(htmlobj.responseText);
		$("#approve").attr({
			"uid":item.attr("uid"),
			"mtype":item.attr("mtype")
		});
		$("#approve-id").val(item.attr("uid"));
		$("#approve-type").val(item.attr("mtype"));
		$("#modal-approve").modal("show");
    }	

	function filter(){
		var materialType = $("#type-filter option:selected").val();
		var printType = $("#print-filter option:selected").val();
		var date = $("#datePicker").val();
		var status = $(".items").attr("status");
		$(".item").hide()

		$(".item").each(function(){
		
			if(
				(printType=="all" || $(this).find("span.is_print").text() == printType)&&(date == "" || $(this).find("span[name='applytime']").text().indexOf(date)>=0)&&(materialType=="all" || $(this).attr("mtype") == materialType) && (status.indexOf($(this).attr('result'))>=0)
			){
				$(this).show();
			}

		})
	}

	function timeClear(){
		$("#datePicker").val("");
		filter();
		$("#time-clear").css("display","none")
	}

	//全选
	function allChoose(){
		$(".checkbox>input").prop("checked",true);
	}
	//全不选

	function allCancel(){
		$(".checkbox>input").prop("checked",false);
	}
	//全选和全不选不能用attr。jquery版本问题



	function eachSave(){
		//获取目标items集合
		var items=$('.checkbox>input:checked').parent().parent().find('ul').find('button:odd').parents("div.item");
		//alert(items.length);
		var dataArray=new Array(items.length);
	//	for (var i = items.length - 1; i >= 0; i--) {
	//		alert(items[i]);
	//	}

		//初始化一个储存数据的json数组
		for (var i = items.length - 1; i >= 0; i--) {
		//var mtype=item.attr("mtype");
			var item=$(items[i]);
			dataArray[i]={
				"type":item.attr("mtype"),
				"id":item.attr("uid")

			};
			//alert(dataArray[i].type);
		};
	//获取panel面板上用户填写的值
		var result=$("#panel").find('select').val();

		var is_print;
	//$("#panel").find('input:checkbox')[0].checked;获取checkbox的check值	
		if ($("#panel").find('input:checkbox')[0].checked) {
			is_print="是";
		}else{
			is_print="否";
		}





	/*
	以上获取到了所需各项内容值
	下面准备发送data
	*/
			


		var data={
			"is_print":is_print,//获取到panel上选择的值
			"result":result,//获取到panel上选择的值
		
			"items":dataArray
		}

		//转字符串
		var dataString=JSON.stringify(data);
		//结果测试
		//alert("data="+data);
		//alert("dataString="+dataString);


	//发送
	args = "mark="+result
	//	$.post("{{url_for('material.mult_approve')}}",dataString,location.reload());
	//直接刷新没毛病
	postResult = $.post("/Material/multiApprove/",dataString,function(result){
		//alert(result)
		location.href="/Material/admin/?"+args;
	});

	

	//刷新
	
}

	//跳转对应页面
	/*	switch(result){//以下4个case编号待定
			case "0" :$("div.header_filt p[status=0]").trigger("click");break;

			case "1" :$("div.header_filt p[status=1]").trigger("click");break;

			case "2" :$("div.header_filt p[status=12]").trigger("click");break;
		
			case "3" :$("div.header_filt p[status=03]").trigger("click");break;
		}
	}
*/




