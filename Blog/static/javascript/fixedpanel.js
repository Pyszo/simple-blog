window.onscroll=function(){
	if(document.body.scrollTop > 200){
		document.getElementById('fp').style.position = 'fixed';
		document.getElementById('fp').style.top = '20px';
	} else {
		document.getElementById('fp').style.position = 'absolute';
		document.getElementById('fp').style.top = '220px';
	}
}
