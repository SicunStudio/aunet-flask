var myDate = new Date();
document.getElementsByTagName("year")[0].innerHTML=myDate.getFullYear();

function _getimg(m)
{
	document.getElementById("show_").src=m.src;
	news=document.getElementsByClassName("news");
	for(var loop=0;loop<5;loop++)
		news[loop].id="";
	m.id="on";
	document.getElementById("picture_title").innerHTML=m.alt;
}

flag_funcMenu=0;
function _menu(){
	if(!flag_funcMenu)
		{
			document.getElementById("top_menu_menu").style.display="block";
			flag_funcMenu=1;
		}
	else
		{	
			document.getElementById("top_menu_menu").style.display="none";
			flag_funcMenu=0;
		}
}

function GetHttpObject() 	//解决兼容性
{
		return new XMLHttpRequest();
}


// function NewsPro(text,x)//ajax 获取的字符串处理
// {
// 	switch(x)
// 		{
// 		case 1:	return text.split("<title>")[1].split("</title>")[0];break;     //1
// 		case 2: return text.split("<time>")[1].split("</time>")[0];break;        //2
// 		case 3: return text.split("<img src=\"")[1].split("\" alt=\"\">")[0];break;		//3
// 		case 4: return article=text.split("<article>")[1].split("</article>")[0];break;		//4
// 		default : alert("Error");break;
// 		}
// }

function LoopNews()
{
	// var news=document.getElementsByClassName("news");
	// var img=document.getElementById("show_").src;
	// var title=document.getElementById("picture_title").innerHTML;
	// var loop=0;
	// var s=setInterval(function(){
	// 	img=news[loop].src;
	// 	title=news[loop].alt;
	// 	loop++;
	// 	if(loop>=5) loop=0;
	// 	},500);
	var news=document.getElementsByClassName("news");
	var loop=0;
	var s=setInterval(function(){
		_getimg(news[loop]);
		loop++;
		if(loop>=5) loop=0;	
	},5000	)
}



//主页新闻获取方式，ajax或者后台直接组装？先看后台如何
//其他页面资源的预加载，保证用户可以快速访问除主页外的其他页面，添
//加文件时请确保文件不会过大，以免影响浏览器性能
// function GetNews(src)	
// {
//  var request=GetHttpObject();
// 	if(request)
// 	{
// 		request.open("GET",src,true);
// 		request.onreadystatechange=function(){
// 			if(request.readyState==4)
// 					{
//					var text=request.responseText;
// 					}

// 		};
// 		request.send(null);
// 	}
// 	else
// 	{
// 		alert("error");		//错误处理
// 	}
// }


window.onload=function()
{
	LoopNews();
}