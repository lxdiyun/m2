
   function changefuncs(link){	
	   document.getElementById('text').className = "gb2";
	   document.getElementById('formula').className = "gb2";
	   document.getElementById('txtformula').className = "gb2";
	   document.getElementById('graph').className = "gb2";
	   document.getElementById('diagram').className = "gb2";
   	      
	   link.className = "gb2chosen";
	
	
	   document.getElementById('formuladialog').style.display = "none";
	   document.getElementById('graphdialog').style.display = "none";
	   document.getElementById('diagramdialog').style.display = "none";
	   document.getElementById('editor').style.display = "none";
	   document.getElementById('editor').style.width = "540px";
   
   
   if (link.id == "txtformula" || link.id == "formula"){
	   document.getElementById('editor').style.display = "block";
	   document.getElementById('formuladialog').style.display = "block";
	   
   }
   else if (link.id == "graph"){
	   document.getElementById('editor').style.display = "block";
	   document.getElementById('editor').style.width = "420px";
	   document.getElementById('graphdialog').style.display = "block";
   }

   else if (link.id == "diagram"){
	   document.getElementById('editor').style.display = "block";
	   document.getElementById('editor').style.width = "400px";
	   document.getElementById('diagramdialog').style.display = "block";
       }
      
       
   }

	function changeSubject(subject, userid){
		
		// alert(subject + userid);
		var ajax = createRequest();
		// alert(query);
		var Strurl = "ajax.php?subject=" + encodeURIComponent(subject) + "&userid=" + userid;
		// alert("ddddddddddd");
		// alert(Strurl);
		ajax.open("GET", Strurl, true);
		ajax.onreadystatechange = function() {
			if (ajax.readyState == 4 && ajax.status == 200) {
				location.reload();
				//alert(ajax.responseText);
			}
		};
		ajax.send(null);
	}
			
function panelchooser(radio) {
	var value = radio.value;
	switch (value) {
	case "mcq": {
		var panel = document.getElementById('mcqpanel');
		panel.style.display = "block";
		document.getElementById('longqpanel').style.display = "none";
		break;
	}
	case "fbq": {
		var panel = document.getElementById('mcqpanel');
		panel.style.display = "none";
		document.getElementById('longqpanel').style.display = "none";
		break;
	}
	case "lq": {
		var panel = document.getElementById('mcqpanel');
		panel.style.display = "none";
		document.getElementById('longqpanel').style.display = "block";
		break;
	}
	}
}

var displayed = 1;
var chooseArray = new Array("divsub1", "divsub2", "divsub3", "divsub4");


function classification() {
	document.getElementById('classifications').style.display = "none";
	document.getElementById('classificationschooser').style.display = "block";	
}


function addsubqs() {
	//alert("ddddddddd");
	for ( var i = 0; i < displayed; i++) {
		document.getElementById(chooseArray[i]).style.display = "block";
	}
	displayed++;
	// max
	if (displayed == 5)
		document.getElementById("addsubqs").style.display = "none";
}


var choices = 1;
var chooseItemsArray = new Array("divA", "divB", "divC", "divD");

function addchoiceqs() {
	//alert("ddddddddd");
	for ( var i = 0; i < choices; i++) {
		document.getElementById(chooseItemsArray[i]).style.display = "block";
	}
	choices++;
	// max
	if (choices == 5)
		document.getElementById("addchoicesqs").style.display = "none";
}


function delsubqs(div) {
	// alert(div);
	document.getElementById(div).style.display = "none";
	displayed--;
	document.getElementById("addsubqs").style.display = "block";
}

// Ajax supporting
function createRequest() {
	var request;
	if (window.XMLHttpRequest) { // For Mozilla, Safari, ...
		request = new XMLHttpRequest();
	}
	return request;
}


function showSearchResults(divID, value) {
	alert(divID);
	var ajax = createRequest();
	var query = value;
	// alert(query);
	var Strurl = "ajax.php?q=" + encodeURIComponent(query);
	// alert("ddddddddddd");
	 alert(Strurl);
	ajax.open("GET", Strurl, true);
	ajax.onreadystatechange = function() {
		if (ajax.readyState == 4 && ajax.status == 200) {
			document.getElementById(divID).innerHTML = ajax.responseText;
			AMtranslated = false;
			translate();
			// alert(ajax.responseText);
		}
	};
	ajax.send(null);
	// call existing onload function
}

var inputComp = "";

function compfocus(comp){
	   inputComp = comp;
	   if (comp == "questionContent"){
		   document.getElementById('edt_formula').className = "gb2chosen";
		   document.getElementById('editor').style.display = "block";
	   	   document.getElementById('formuladialog').style.display = "block";
	   }
}

function changefuncs(link){	
   

	   document.getElementById('edt_formula').className = "gb2ask";
	   document.getElementById('edt_graph').className = "gb2ask";
	   document.getElementById('edt_diagram').className = "gb2ask";		    			    	   	      
    link.className = "gb2chosen";




    document.getElementById('formuladialog').style.display = "none";
    document.getElementById('graphdialog').style.display = "none";
    document.getElementById('diagramdialog').style.display = "none";
    

    if (link.id == "edt_formula"){
 	   document.getElementById('editor').style.display = "block";
 	   document.getElementById('editor').style.width = "450px";
 	   document.getElementById('formuladialog').style.display = "block";
 	   
    }
    else if (link.id == "edt_graph"){
 	   document.getElementById('editor').style.display = "block";
 	   document.getElementById('editor').style.width = "420px";
 	   document.getElementById('graphdialog').style.display = "block";
    }

    else if (link.id == "edt_diagram"){
 	   document.getElementById('editor').style.display = "block";
 	   document.getElementById('editor').style.width = "400px";
 	   document.getElementById('diagramdialog').style.display = "block";
    }
    
}

function insertFormula(){
      var mathExpression = document.dragmath.getMathExpression();
      document.getElementById(inputComp).value += mathExpression;
      document.dragmath.setMathExpression("");
 } 




var base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
var base64DecodeChars = new Array(
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63,
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1,
    -1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1,
    -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1);
function base64encode(str) {
    var out, i, len;
    var c1, c2, c3;
    len = str.length;
    i = 0;
    out = "";
    while(i < len) {
        c1 = str.charCodeAt(i++) & 0xff;
        if(i == len){
            out += base64EncodeChars.charAt(c1 >> 2);
            out += base64EncodeChars.charAt((c1 & 0x3) << 4);
            out += "==";
            break;
        }
        c2 = str.charCodeAt(i++);
        if(i == len){
            out += base64EncodeChars.charAt(c1 >> 2);
            out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
            out += base64EncodeChars.charAt((c2 & 0xF) << 2);
            out += "=";
            break;
        }
        c3 = str.charCodeAt(i++);
        out += base64EncodeChars.charAt(c1 >> 2);
        out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
        out += base64EncodeChars.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >>6));
        out += base64EncodeChars.charAt(c3 & 0x3F);
    }
    return out;
}
