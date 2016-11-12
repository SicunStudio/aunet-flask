$(document).ready(function(){

	$(".item").each(
		function(){
			var result = {
				"1":"pass",
				"2":"fail",
				"0":"ongoing"
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
	$("div.header_filt p[status=0]").trigger("click");
})
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
		
	};
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
	}
	function getModal(button){

		var item = button.parents("div.item")

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