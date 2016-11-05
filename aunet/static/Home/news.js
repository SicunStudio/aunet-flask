window.onload=function()
{
	var lis = document.getElementsByClassName("search_option")[0].getElementsByTagName("li");
	for(var loop = 0 ; loop < 12 ; loop++)
		lis[loop].addEventListener("click",GetSearchPart);
	document.getElementsByTagName("body")[0].addEventListener("onload",GetAllOn);
	document.getElementsByClassName("goto")[0].getElementsByTagName("a")[0].addEventListener("click",PageUp);
	document.getElementsByClassName("goto")[0].getElementsByTagName("a")[2].addEventListener("click",PageDown);
	document.getElementsByClassName("goto")[0].getElementsByTagName("a")[1].addEventListener("click",GetAllOn);
}