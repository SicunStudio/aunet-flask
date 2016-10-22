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
	for(var loop = 0;loop < 5;loop++)
		news[loop].id = "";
	this.id = "on";//被选中
	for(var loop = 0;loop < 5;loop++)
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

function InitImgSrc()
{
	var img_1 = document.getElementById("hot_news").getElementsByClassName("left")[0].getElementsByClassName("picture")[0].getElementsByTagName("img");
	var img_2 = document.getElementById("hot_news").getElementsByClassName("left")[0].getElementsByClassName("preview")[0].getElementsByTagName("img");
	for(var loop = 0 ; loop < 5 ; loop ++)
		img_1[loop].src = img_2[loop].src;
}
/*******
循环预览图片
*********/
function _GetImg(m , order)
{
	var news = document.getElementsByClassName("news");
	for(var loop = 0;loop < 5;loop++)
		news[loop].id = "";
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
	document.getElementById("picture_title").innerHTML = m.alt;//替换标题
}
function LoopNews()
{
	var news = document.getElementsByClassName("news");
	var loop = 0;
	_GetImg(news[loop] , loop);
	loop++;
	var s = setInterval(function(){
		_GetImg(news[loop] , loop);
		loop++;
		if(loop >= 5) loop = 0;	
	},5000);
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
	var news = document.getElementsByClassName("news_2_x");
	for(var loop = 0;loop < 10;loop++)
		news[loop].setAttribute("style","display:none");
	var page = JSON.parse(news);
	document.getElementsByClassName("goto")[0].getElementsByTagName("input")[1].setAttribute("value",page["news_Length"] + "");
	document.getElementsByClassName("goto")[0].getElementsByTagName("input")[0].setAttribute("value",page["news_Current_Page"] + "");
	for(loop = 0;loop < page.news_Length;loop++)
	{
		news[loop].setAttribute("style","display:block");
		/******一下的json访问可能存在问题******/
		news[loop].getElementsByClassName("news_title")[0].innerHTML = page.["news_Title"][loop][loop+""];
		news[loop].getElementsByClassName("article")[0].innerHTML = page["news_Outline"][loop][loop+""];
		news[loop].getElementsByTagName("img")[0].setAttribute("src",page["news_Img_Url"][loop][loop+""]);
		news[loop].getElementsByClassName("time")[0].innerHTML = page["news_Post_Time"][loop][loop+""];
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
        success: function (message) {
            if (message > 0) {
                alert("请求已提交！");
                alert(JSON.parse(message));
                DisplayNews(message);
            }
        },
        error: function (message) {
            alert("提交数据失败！");

                DisplayNews(message);
        }
    });
    alert(JSON.stringify(posts));

// $.ajax{
// 	type:'POST',
// 	dataType:'json',
// 	url:'news/news2Json',
// 	data:post,
// }
// 
// 
// $().ajax({
//     type: 'POST',
//     url: 'news/news2Json',
//     data: JSON.stringify(posts),
//     contentType: 'application/json; charset=UTF-8',
//     dataType: 'json',
//     success: function(data) { 
//     },
//     error: function(xhr, type) {
//     }
// });
// 
}
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
	for(loop;loop < 12;loop++)
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


/****文档加载完成后的执行代码*****/
window.onload=function()
{
}