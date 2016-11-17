jQuery.validator.addMethod("validFileType", function(value, element) {   
    var ldot = value.lastIndexOf(".");
    var type = value.substring(ldot + 1);
    var result = ["doc","docx","ppt","pptx","xls","xlsx","pdf","zip","rar","7z","txt"].indexOf(type);
    return this.optional(element) || (result>=0);
}, "请上传指定的文件类型！(doc,docx,ppt,pptx,xls,xlsx,pdf,zip,rar,7z,txt)")

	$.validator.setDefaults({
		submitHandler: function() {				//可成功提交，隐藏alert
		  form.submit(); 
		},
		debug:false,
		onfocusout: function(element) { $(element).valid(); },
	});

	$().ready(function() {
		$("#form1").validate({
			rules:{	
				week:"required",
				capacity:"required",
				host:"required",
				unit:"required",
				title:"required",
				association:"required",
				activity:"required",
				site:"required",
				resp_person:"required",
				school_id:"required",
				phone:"number",
				department:"required",
				content:"required",
				time:"required",
				number:{
					required:true,
					number:true
				},				
				tel:{
					required:true,
					number:true,
				},
				trans_desk_num:{
					required:true,
					number:true
				},					//二选一？
				trans_chair_num:{
					required:true,
					number:true
				},
				desk_num:{
					required:true,
					number:true
				},
				chair_num:{
					required:true,
					number:true
				},
				electricity_num:{
					required:true,
					number:true
				},
				projector_num:{
					required:true,
					number:true
				},
				year1:{
					required:true,
					number:true
				},
				month1:{
					required:true,
					number:true
				},
				year2:{
					required:true,
					number:true
				},
				month2:{
					required:true,
					number:true
				},
				year3:{
					required:true,
					number:true
				},
				month3:{
					required:true,
					number:true
				}
			},
			messages: {										// 提示信息
				association:"协会名称：不能为空！ ",
				activity:"活动名称：不能为空！ ",
				site:"活动地点：不能为空！ ",
				resp_person:"负责人：不能为空！ ",
				tel:{
					required:"联系电话：不能为空！ ",
					number:"联系电话：请规范填写！ "
				},
				trans_desk_num:{
					required:"运送桌子数量：不能为空！ ",
					number:"运送桌子数量：请规范填写！ "
				},
				trans_chair_num:{
					required:"运送椅子数量：不能为空！ ",
					number:"运送椅子数量：请规范填写！ "
				},
				desk_num:{
					required:"桌子数量：不能为空！ ",
					number:"桌子数量：请规范填写！ "
				},
				chair_num:{
					required:"椅子数量：不能为空！ ",
					number:"椅子数量：请规范填写！ "
				},
				electricity_num:{
					required:"瓦数：不能为空！ ",
					number:"瓦数：请规范填写！ "
				},
				projector_num:{
					required:"台数：不能为空！ ",
					number:"台数：请规范填写！ "
				},
				year1:{
					required:"请选择借用年份！ ",
					number:"请选择借用年份！ "
				},
				month1:{
					required:"请选择借用月份！ ",
					number:"请选择借用月份！ "
				},
				date1:{
					required:"请选择借用日期！ ",
					number:"请选择借用日期！ "
				},
				year2:{
					required:"请选择归还年份！ ",
					number:"请选择归还年份！ "
				},
				month2:{
					required:"请选择归还月份！ ",
					number:"请选择归还月份！ "
				},
				date2:{
					required:"请选择归还日期！ ",
					number:"请选择归还日期！ "
				},
				year3:{
					required:"请选择归还年份！ ",
					number:"请选择归还年份！ "
				},
				month3:{
					required:"请选择归还月份！ ",
					number:"请选择归还月份！ "
				},
				date3:{
					required:"请选择归还日期！ ",
					number:"请选择归还日期！ "
				},
			}
		});
	});
