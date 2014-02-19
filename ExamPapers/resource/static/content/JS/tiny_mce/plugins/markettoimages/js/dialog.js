tinyMCEPopup.requireLangPack();

var MarkettoImagesDialog = {
	init : function() {
		
	},
	
	inProgress : function() {
		document.getElementById("upload_form_container").style.display = 'none';
		document.getElementById("upload_in_progress").style.display = 'block';
	},
	
	uploadFinish : function(result) {
		if (result.resultCode == 'failed')
		{
			document.getElementById("upload_in_progress").style.display = 'none';
			document.getElementById("upload_infobar").style.display = 'block';
			document.getElementById("upload_infobar").innerHTML = result.result;
			document.getElementById("upload_form_container").style.display = 'block';
		}
		else
		{
			document.getElementById("upload_in_progress").style.display = 'none';
			document.getElementById("upload_infobar").style.display = 'block';
			document.getElementById("upload_infobar").innerHTML = result.result;
			tinyMCEPopup.editor.execCommand('mceInsertContent', false, '<img src="' + result.filename +'" />');
			tinyMCEPopup.close();
		}
	}

};

tinyMCEPopup.onInit.add(MarkettoImagesDialog.init, MarkettoImagesDialog);
