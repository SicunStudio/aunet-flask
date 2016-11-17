window.onload=function()
{
	for(var loop=0 ; loop < 10 ; loop++)
		document.getElementById("news_").getElementsByClassName("news_2")[0].innerHTML = '<div class="news_2_x"><img src="" alt=""><div><div class="news_title"></div><div class="article"></div></div><div><span class="time"></span><span class="detail"><a href="">&nbsp;&nbsp;<img src="../../../	static/Home/xq.png" alt="">详情</a></span></div><br><br><br><br><hr><br></div>' + document.getElementById("news_").getElementsByClassName("news_2")[0].innerHTML;
	InitHeader();
	var lis = document.getElementsByClassName("search_option")[0].getElementsByTagName("li");
	for(var loop = 0 ; loop < lis.length ; loop++)
		lis[loop].addEventListener("click",GetSearchPart);
		GetAllOn();
	document.getElementsByClassName("goto")[0].getElementsByTagName("a")[0].addEventListener("click",PageUp);
	document.getElementsByClassName("goto")[0].getElementsByTagName("a")[2].addEventListener("click",PageDown);
	document.getElementsByClassName("goto")[0].getElementsByTagName("a")[1].addEventListener("click",GetAllOn);
}