//据material_type显示



//日期option生成
	var o1d=0;//决定是否生成date1的option
	var o2d=0;//决定是否生成date2的option
	var o3d=0;//决定是否生成date3的option
	var o2m=0;//决定是否生成month2的option
	var o3m=0;//决定是否生成manth3的option
	

	function fo1d(n){	//执行后不再生成date1的option
		o1d=n;
	}
	function fo2d(n){	
		o2d=n;
	}
	function fo3d(n){	
		o3d=n;
	}
	function fo2m(){	
		o2m=1;
	}
	function fo3m(){	
		o3m=1;
	}


	function addmonth1(){
		for (i=1;i<13;i=i+1)
		{
			var newOption=document.createElement("option"); 
			if (i<10)
				{
					var s='0'+i.toString();
					newOption.value=s;
					newOption.text=s;
				} 
				else
				{
					var s=i.toString();
					newOption.value=s;
					newOption.text=s;
				}
			document.getElementById("month1").options.add(newOption);
		}
	}
	function addmonth2(){
		if (o2m==0)
		{
			for (i=1;i<13;i=i+1)
			{
				var newOption=document.createElement("option"); 
				if (i<10)
				{
					var s='0'+i.toString();
					newOption.value=s;
					newOption.text=s;
				} 
				else
				{
					var s=i.toString();
					newOption.value=s;
					newOption.text=s;
				}
				document.getElementById("month2").options.add(newOption);
			}
			fo2m();
		}
	}
	
	function addmonth3(){
		if (o3m==0)
		{
			for (i=1;i<13;i=i+1)
			{
				var newOption=document.createElement("option"); 
				if (i<10)
				{
					var s='0'+i.toString();
					newOption.value=s;
					newOption.text=s;
				} 
				else
				{
					var s=i.toString();
					newOption.value=s;
					newOption.text=s;
				}
				document.getElementById("month3").options.add(newOption);
			}
			fo3m();
		}
	}


	function adddate1(){
		var tf=1;
		var mm=document.getElementById("month1").value;
		if (o1d==31&&(mm=='01'||mm=='03'||mm=='05'||mm=='07'||mm=='08'||mm=='10'||mm=='12'))
		{tf=0;}
		else if (o1d==30&&(mm=='04'||mm=='06'||mm=='09'||mm=='11'))
		{tf=0;}
		else if (o1d==28&&mm=='02')
		{tf=0;}//不更换选项的条件
		if (tf==1)
		{
			document.getElementById("date1").options.length=0; 
			for (i=1;i<29;i=i+1)
			{
				var newOption=document.createElement("option"); 
				if (i<10)
				{
					var s='0'+i.toString();
					newOption.value=s;
					newOption.text=s;
				} 
				else
				{
					var s=i.toString();
					newOption.value=s;
					newOption.text=s;
				}
				document.getElementById("date1").options.add(newOption);
			}
			if (mm!='02')
			{
				if (mm=='04'||mm=='06'||mm=='09'||mm=='11')
				{
					for (i=29;i<31;i=i+1)
					{
						var newOption=document.createElement("option"); 
						if (i<10)
						{
							var s='0'+i.toString();
							newOption.value=s;
							newOption.text=s;
						} 
						else
						{
							var s=i.toString();
							newOption.value=s;
							newOption.text=s;
						}
						document.getElementById("date1").options.add(newOption);
					}
					fo1d(30);
				}
				else
				{
					for (i=29;i<32;i=i+1)
					{
						var newOption=document.createElement("option"); 
						if (i<10)
						{
							var s='0'+i.toString();
							newOption.value=s;
							newOption.text=s;
						} 
						else
						{
							var s=i.toString();
							newOption.value=s;
							newOption.text=s;
						}
						document.getElementById("date1").options.add(newOption);
					}
					fo1d(31);
				}
			}
			else{
				fo1d(28);
			}
		}
	}

	function adddate2(){
		var tf=1;
		var mm=document.getElementById("month2").value;
		if (o2d==31&&(mm=='01'||mm=='03'||mm=='05'||mm=='07'||mm=='08'||mm=='10'||mm=='12'))
		{tf=0;}
		else if (o2d==30&&(mm=='04'||mm=='06'||mm=='09'||mm=='11'))
		{tf=0;}
		else if (o2d==28&&mm=='02')
		{tf=0;}//不更换选项的条件
		if (tf==1)
		{
			document.getElementById("date2").options.length=0; 
			for (i=1;i<29;i=i+1)
			{
				var newOption=document.createElement("option"); 
				if (i<10)
				{
					var s='0'+i.toString();
					newOption.value=s;
					newOption.text=s;
				} 
				else
				{
					var s=i.toString();
					newOption.value=s;
					newOption.text=s;
				}
				document.getElementById("date2").options.add(newOption);
			}
			if (mm!='02')
			{
				if (mm=='04'||mm=='06'||mm=='09'||mm=='11')
				{
					for (i=29;i<31;i=i+1)
					{
						var newOption=document.createElement("option"); 
						if (i<10)
						{
							var s='0'+i.toString();
							newOption.value=s;
							newOption.text=s;
						} 
						else
						{
							var s=i.toString();
							newOption.value=s;
							newOption.text=s;
						}
						document.getElementById("date2").options.add(newOption);
					}
					fo2d(30);
				}
				else
				{
					for (i=29;i<32;i=i+1)
					{
						var newOption=document.createElement("option"); 
						if (i<10)
						{
							var s='0'+i.toString();
							newOption.value=s;
							newOption.text=s;
						} 
						else
						{
							var s=i.toString();
							newOption.value=s;
							newOption.text=s;
						}
						document.getElementById("date2").options.add(newOption);
					}
					fo2d(31);
				}
			}
			else{
				fo2d(28);
			}
		}
	}

	function adddate3(){
		var tf=1;
		var mm=document.getElementById("month3").value;
		if (o3d==31&&(mm=='01'||mm=='03'||mm=='05'||mm=='07'||mm=='08'||mm=='10'||mm=='12'))
		{tf=0;}
		else if (o3d==30&&(mm=='04'||mm=='06'||mm=='09'||mm=='11'))
		{tf=0;}
		else if (o3d==28&&mm=='02')
		{tf=0;}//不更换选项的条件
		if (tf==1)
		{
			document.getElementById("date3").options.length=0; 
			for (i=1;i<29;i=i+1)
			{
				var newOption=document.createElement("option"); 
				if (i<10)
				{
					var s='0'+i.toString();
					newOption.value=s;
					newOption.text=s;
				} 
				else
				{
					var s=i.toString();
					newOption.value=s;
					newOption.text=s;
				}
				document.getElementById("date3").options.add(newOption);
			}
			if (mm!='02')
			{
				if (mm=='04'||mm=='06'||mm=='09'||mm=='11')
				{
					for (i=29;i<31;i=i+1)
					{
						var newOption=document.createElement("option"); 
						if (i<10)
						{
							var s='0'+i.toString();
							newOption.value=s;
							newOption.text=s;
						} 
						else
						{
							var s=i.toString();
							newOption.value=s;
							newOption.text=s;
						}
						document.getElementById("date3").options.add(newOption);
					}
					fo3d(30);
				}
				else
				{
					for (i=29;i<32;i=i+1)
					{
						var newOption=document.createElement("option"); 
						if (i<10)
						{
							var s='0'+i.toString();
							newOption.value=s;
							newOption.text=s;
						} 
						else
						{
							var s=i.toString();
							newOption.value=s;
							newOption.text=s;
						}
						document.getElementById("date3").options.add(newOption);
					}
					fo3d(31);
				}
			}
			else{
				fo3d(28);
			}
		}
	}

	function ale(){
		$("#statement").val($("input[type='file']").val());
		$("#statement").valid();
	}