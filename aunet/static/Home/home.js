window.onload=function()
{
	var news = document.getElementsByClassName("news");
	for(var loop = 0 ; loop < news.length ; loop++)
		news[loop].addEventListener("click",GetImg);
	LoopNews();
	InitImgSrc();
	document.getElementsByClassName("menu")[0].addEventListener("click",_menu);
	InitHeader();



	//Old_width = GetWinWidth();
	function SetHotnewsMargin()
	{
		var winWidth;
		winWidth = GetWinWidth();
		// if(winWidth != Old_width)
		// {
		// // 	IncludeLinkStyle("../../../static/Home/index_mobile.css");
		// Old_width = winWidth;
		// InitMenuLine();
		// }
		var hot_new_left_width;
		hot_new_left_width = document.getElementById("hot_news").getElementsByClassName("left")[0].clientWidth;
		var hot_new_right_width;
		hot_new_right_width = document.getElementById("hot_news").getElementsByClassName("right")[0].clientWidth;
		if(winWidth >= 950)
		{
			document.getElementById("hot_news").getElementsByClassName("left")[0].style.marginLeft = (winWidth - (hot_new_left_width+hot_new_right_width) -30) / 2 + "px";
			document.getElementById("hot_news").getElementsByClassName("right")[0].style.marginRight = (winWidth - (hot_new_left_width+hot_new_right_width) - 30) / 2 + "px";
			document.getElementById("news_").style.width = (hot_new_left_width+hot_new_right_width) + "px";
			document.getElementById("news_").style.marginLeft = (winWidth - (hot_new_left_width+hot_new_right_width) -30) / 2 + "px";
			document.getElementById("star_").style.width = (hot_new_left_width+hot_new_right_width) + "px";
			document.getElementById("star_").style.marginLeft = (winWidth - (hot_new_left_width+hot_new_right_width) -30) / 2 + "px";
		}
		else
		{
			document.getElementById("hot_news").getElementsByClassName("left")[0].style.marginLeft = 0;
			document.getElementById("news_").style.width = (hot_new_left_width) + "px";
			document.getElementById("news_").style.marginLeft = (winWidth - (hot_new_left_width) - 30) / 2 + "px";
			document.getElementById("star_").style.width = (hot_new_left_width) + "px";
			document.getElementById("star_").style.marginLeft = (winWidth - (hot_new_left_width) - 30)/ 2 + "px";
		} 
		if(winWidth < 820)
			document.getElementsByClassName("news_3")[0].getElementsByTagName("span")[0].innerHTML = "<br>";
		else 
			document.getElementsByClassName("news_3")[0].getElementsByTagName("span")[0].innerHTML = "";

	}
	SetHotnewsMargin();
	var loop  = setInterval(SetHotnewsMargin , 2);
}