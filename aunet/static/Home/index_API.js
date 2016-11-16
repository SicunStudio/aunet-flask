/******获取本地时间对象******/
var myDate = new Date();					
document.getElementsByTagName("year")[0].innerHTML = myDate.getFullYear();


/*********
获取头部循环图片的地址
及其是否被选中flag
替换大图标题
*********/
function GetImg()
{
	var news = document.getElementsByClassName("news");
	if(!news)
		return;
	else
	{
		for(var loop = 0;loop < news.length;loop++)
			news[loop].id = "";
		this.id = "on";//被选中
		for(var loop = 0;loop < news.length;loop++)
			if(news[loop].id == "on")
				break;
		var order = loop;
		var wid;
		if(parseInt(document.body.clientWidth) > 1199)
			wid = 404;
		else if(parseInt(document.body.clientWidth) > 950)
			wid = 334;
		else if(parseInt(document.body.clientWidth) >= 720)
			wid = 410;
		else if(parseInt(document.body.clientWidth) >= 415)
			wid = 235;
		else 
			wid = 174;
		
		document.getElementById("hot_news").getElementsByClassName("left")[0].getElementsByClassName("picture")[0].getElementsByClassName("img")[0].style.bottom=order*wid+"px";
		document.getElementById("picture_title").innerHTML = this.alt;//替换标题
	}
}

function InitImgSrc()
{
	var img_1 = document.getElementById("hot_news").getElementsByClassName("left")[0].getElementsByClassName("picture")[0].getElementsByTagName("img");
	var img_2 = document.getElementById("hot_news").getElementsByClassName("left")[0].getElementsByClassName("preview")[0].getElementsByTagName("img");
	for(var loop = 0 ; loop < img_2.length ; loop ++)
		img_1[loop].src = img_2[loop].src;
}
/*******
循环预览图片
*********/
function _GetImg(m , order)
{
	var news = document.getElementsByClassName("news");
	if(!news)
		return;
	else
	{
		for(var loop = 0;loop < news.length;loop++)
			news[loop].id = "";
		if(m)
			m.id = "on";//被选中
		var wid;
		if(parseInt(document.body.clientWidth) > 1199)
			wid = 404;
		else if(parseInt(document.body.clientWidth) >= 950)
			wid = 334;
		else if(parseInt(document.body.clientWidth) >= 720)
			wid = 410;
		else if(parseInt(document.body.clientWidth) >= 415)
			wid = 235;
		else 
			wid = 174;		
		document.getElementById("hot_news").getElementsByClassName("left")[0].getElementsByClassName("picture")[0].getElementsByClassName("img")[0].style.bottom=order*wid+"px";
		if(m)
			document.getElementById("picture_title").innerHTML = m.alt;//替换标题
	}
}
function LoopNews()
{
	var news = document.getElementsByClassName("news");
	if(!news)
		return;
	else
	{
		var loop = 0;
		_GetImg(news[loop] , loop);
		loop++;
		var s = setInterval(function(){
			_GetImg(news[loop] , loop);
			loop++;
			if(loop >= news.length) loop = 0;	
		},5000);
	}
}


/*****兼容性菜单的解决办法*****/
flag_funcMenu = 0;
function _menu(){
	if(!flag_funcMenu)
	{
		document.getElementById("top_menu_menu").style.display = "block";
		flag_funcMenu = 1;
	}
	else
	{	
		document.getElementById("top_menu_menu").style.display = "none";
		flag_funcMenu = 0;
	}
}

function DisplayNews(news)
{
	var page = news;
	//alert(JSON.stringify(news))
	var news = document.getElementsByClassName("news_2_x");
	for(var loop = 0;loop < news.length;loop++)
		news[loop].setAttribute("style","display:none");
	document.getElementsByClassName("goto")[0].getElementsByTagName("input")[1].setAttribute("value",page["news_number"] + "");
	document.getElementsByClassName("goto")[0].getElementsByTagName("input")[0].setAttribute("value",page["current_page"] + "");
	for(loop = 0;loop < parseInt(page["length"]);loop++)
	{
		news[loop].setAttribute("style","display:block");
		/******一下的json访问可能存在问题******/
		news[loop].getElementsByClassName("news_title")[0].innerHTML = page["title"][loop][loop+""];
		news[loop].getElementsByClassName("article")[0].innerHTML = page["outline"][loop][loop+""];
		news[loop].getElementsByTagName("img")[0].setAttribute("src",page["img_url"][loop][loop+""]);
		news[loop].getElementsByClassName("time")[0].innerHTML = page["post_time"][loop][loop+""];
	}
}

/*******
获取不同浏览器内核的ajax请求对象
*******/
function GetHttpObject() 	//解决兼容性
{
	return new XMLHttpRequest();
}

/*****
ajax提交请求并获取数据
******/
function GetNews(posts)
{
	// var request = GetHttpObject();
	// // /alert(post['Sort'])
	// if(request)
	// {
		
	// 	request.open("POST","news/news2Json",true);
	// 	request.setRequestHeader("Content-Type","application/x-javascript;charset=UTF-8");//
	// 	var info = JSON.stringify(posts);
		
	// 	alert(info);

	// 	request.onreadystatechange = function(){
	// 		if(request.readyState == 4)
	// 				{
	// 					var page=request.responseText;//返回一个json对象
	// 					DisplayNews(page);
	// 				}
	// 		}
	// 	request.send(info);//提交一个json对象

	// }
	// else
	// {
	// 	alert("error");
	// }
	
	$.ajax({
        type: "POST",
        url: "news/news2Json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(posts),
        dataType: "json",
        success: function(data) {
            if (data > 0) 
                alert("请求已提交！");
            DisplayNews(data);
        },
        error: function() {
            alert("提交数据失败！");

         //       DisplayNews(message);

        }
    });
    //alert(JSON.stringify(posts));
}

// function FillPage()
// {
// 	var news = document.getElementById("news_").getElementsByClassName("news_2_x");
// 	for(var loop = 0 ;loop < news.length ; loop++)
// 	{

// 	}
	
// }

/*****
新闻部分的条件搜索栏
更改其class值
******/
function GetSearchPart()
{
	var parent = this.parentNode;
	// alert("yep");
	for(var loop = 0 ; loop < 4;loop++)
	{
		//alert(parent.getElementsByTagName("li")[loop].getAttribute("name"));
		parent.getElementsByTagName("li")[loop].setAttribute("class","");
	}
	this.setAttribute("class","on");
	GetAllOn();
}

/******获取所有需要传递的值********/
function GetAllOn()
{
	var on = document.getElementsByClassName("search_option")[0].getElementsByTagName("li");
	var loop = 0;
	var jsonData = {};
	for(loop;loop < on.length;loop++)
	{
		if(on[loop].getAttribute("class") == "on")
		{
			var object = on[loop].parentNode.getAttribute("name");
			var value = on[loop].getAttribute("name");
			jsonData[object] = value;
		}	
	}
	//alert(jsonData['Time']);
	//alert(jsonData.object);
	var gotoPage = document.getElementsByClassName("goto")[0];
	if(parseInt(gotoPage.getElementsByTagName("input")[1].value) < parseInt(gotoPage.getElementsByTagName("input")[0].value))
		alert("跳转的页数不能大于总页数哦！");			//待后期再来修改本提示信息及其提示方式
	else
		jsonData["gotoPage"]= gotoPage.getElementsByTagName("input")[0].value;
		// jsonData.goto_Page = gotoPage.getElementsByTagName("input")[0].value;
	//alert(jsonData["gotoPage"]);
	//alert(JSON.stringify(jsonData));
	GetNews(jsonData);
}

/*****前后页跳转及错误处理：开始*****/
function PageUp()
{
	var pageUp = document.getElementsByClassName("goto")[0].getElementsByTagName("input")[0];
	if(parseInt(pageUp.getAttribute("value")) <= 1)
	{

	}
	else 
	{
		pageUp.setAttribute("value",(parseInt(pageUp.getAttribute("value"))-1)+"");
		//alert(pageUp.getAttribute("value"));
		GetAllOn();
	}
}
function PageDown()
{
	var pageUp = document.getElementsByClassName("goto")[0].getElementsByTagName("input")[0];
	if(parseInt(pageUp.getAttribute("value")) >= parseInt(document.getElementsByClassName("goto")[0].getElementsByTagName("input")[1].getAttribute("value")))
	{

	}
	else 
	{
		pageUp.setAttribute("value",(parseInt(pageUp.getAttribute("value"))+1)+"");
		//alert(pageUp.getAttribute("value"));
		GetAllOn();
	}
}
/****结束***/




function IncludeLinkStyle(url) 
{
	document.getElementsByTagName("link")[0].setAttribute("href" , url);
}
function GetWinWidth()
{
	if (window.innerWidth)
		return window.innerWidth;
	else if ((document.body) && (document.body.clientWidth))
		return document.body.clientWidth;
	
}



function getTop(e)
{ 
	var offset=e.offsetTop; 
	if(e.offsetParent!=null) offset+=getTop(e.offsetParent); 
	return offset; 
} 
function getLeft(e)
{ 
	var offset=e.offsetLeft; 
	if(e.offsetParent!=null) offset+=getLeft(e.offsetParent); 
	return offset; 
} 
function getHeight(e)
{ 
	var offset=e.clientHeight;  
	return offset; 
}





function InitPutMenuLine()
{
	var lis = document.getElementById("top_menu_menu").getElementsByTagName("li");
	for(var loop = 0 ; loop < lis.length; loop++)
		if(lis[loop].id == "on")
		{
			e = lis[loop];
			break;
		}	
	var left = getLeft(e);
	var top = getTop(e);
	var line = document.getElementById("menu_bottom_line");
	line.style.left = left + "px";
	line.style.top = top + getHeight(e) - getHeight(line) + "px";
	line.style.transition = "all 0.3s";
}
function PutMenuLine()
{
	var left = getLeft(this);
	var top = getTop(this);
	var line = document.getElementById("menu_bottom_line");
	line.style.left = left + "px";
	line.style.top = top + getHeight(this) - getHeight(line) + "px";
}
function HideMenuLine()
{
	var winWidth;
		winWidth = GetWinWidth();
	if(winWidth < 960)
	{
		document.getElementById("menu_bottom_line").style.display = "none";
	}
	else
		document.getElementById("menu_bottom_line").style.display = "block";
}

Old_width = GetWinWidth(); 
function ResetMenuLine()
{
	var winWidth;
	winWidth = GetWinWidth();
	if(winWidth != Old_width)
	{
	Old_width = winWidth;
	InitPutMenuLine();
	}
}
function InitMenuLine()
{
	InitPutMenuLine();
	lis = document.getElementById("top_menu_menu").getElementsByTagName("li");
	for(var loop = 0 ; loop < lis.length; loop++)
		{
			lis[loop].addEventListener("mouseover",PutMenuLine);
			lis[loop].addEventListener("mouseleave",InitPutMenuLine);
		}
}

function InitHeader()
{
	InitMenuLine();
	var loop_1  = setInterval(HideMenuLine , 100);
	var loop_2	= setInterval(ResetMenuLine , 10)
}

