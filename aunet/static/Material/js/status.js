

function viewModal(button){

	var item = button.parents("tr.table-content")

	var htmlobj=$.ajax({
		url:"/Material/modal/",
		type:"post",
		data:{
			id:item.attr("uid"),
			type:item.attr("mtype"),
			modal_type:"preview"
		},
		async:false,
	});

	$("#modal").html(htmlobj.responseText);
	$("#modal").modal("show");
}
function modify(bt){
	var item = bt.parents("tr.table-content")
	var form = $("<form></form>");
	var action = '/Material/modify/' + item.attr("mtype") + "/";
	form.attr({
		"method":"post",
		"action":action,
		"target":"_self"
	})
	var input = $("<input name='id'/>");
	input.val(item.attr("uid"));
	form.append(input);
	form.appendTo("body");
    form.css('display','none');  
    form.submit();
}
function confirmDelete(bt){
	var item = bt.parents("tr.table-content")
	var value = 'drop("'+item.attr("mtype")+'","'+item.attr("uid")+'")';
	$("#confirm-delete").attr("onclick",value);
	$("#modal-delete").modal("show")
}
function drop(type,id){
	var form = $("<form></form>");
	var action = "{{url_for('material.delete')}}";
	form.attr({
		"method":"post",
		"action":action,
		"target":"_self"
	})
	var input1 = $("<input name='type'/>");
	var input2 = $("<input name='id'/>");
	input1.val(type);
	input2.val(id);
	form.append(input1);
	form.append(input2);
	form.appendTo("body");
    form.css('display','none');
	form.submit();
}
$("#time-filter").dateDropper({
	format:'Y-m-d',
	color:'#f87a54',
	animation:'bounce',
	init_animation:'bounce',
	maxYear:'2025',
	minYear:'2015',
	yearsRange:'5',
});

$("#content-top a").click(function(){
	$("#content-top a").css({
		'background-color':'transparent',
		'color':'black'
	});
	$(this).css({
		'background-color':'#214f21',
		'color':'white'
	})

	$("table").attr("status",$(this).attr("status"));
	var status=$(this).attr("status")
	$(".table-content").hide();
	$(".table-content").each(function(){
		if(status.indexOf($(this).attr('result'))>=0){
			$(this).show();
		}
	})
	$("#type-filter").val("all");
	$("#time-filter").val("");
	$("#time-clear").css("display","none");
})
$("#content-top a[status=012]").trigger("click");
function filter(){
	var materialType = $("#type-filter option:selected").val();
	var date = $("#time-filter").val();
	var status = $("table").attr("status");
	$(".table-content").hide()

	$(".table-content").each(function(){
	
		if((date == "" || $(this).find(".apply-time").text().indexOf(date)>=0)&&(materialType=="all" || $(this).attr("mtype") == materialType) && (status.indexOf($(this).attr('result'))>=0)
		){
			$(this).show();
		}

	})
}
function timeClear(){
	$("#time-filter").val("");
	filter();
	$("#time-clear").css("display","none")
}
