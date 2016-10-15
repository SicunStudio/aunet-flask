window.onload=function()
{
	var news = document.getElementsByClassName("news");
	for(var loop = 0 ; loop < 5 ; loop++)
		news[loop].addEventListener("click",GetImg);
	document.getElementsByTagName("body")[0].addEventListener("onload",LoopNews);
}