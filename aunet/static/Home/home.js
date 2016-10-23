window.onload=function()
{
	var news = document.getElementsByClassName("news");
	for(var loop = 0 ; loop < 5 ; loop++)
		news[loop].addEventListener("click",GetImg);
	LoopNews();
	InitImgSrc();
	document.getElementsByClassName("menu")[0].addEventListener("click",_menu);
}