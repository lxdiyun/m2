(function() {
	tinymce
			.create(
					"tinymce.plugins.formulaeditor",
					{
						init : function(a, b) {
							a.addCommand("formulaeditor", function() {
								tinyMCE.activeEditor.windowManager.open({
								file : "../JS/tiny_mce/plugins/dragMath/dragmath.htm",
						        title : '方程编辑器',
						        width : 560,  // Your dimensions may differ - toy around with them!
						        height : 320,
						        resizable : "no",
						        inline : 1  // This parameter only has an effect if you use the inlinepopups plugin!
							    }, {
							    	plugin_url : b
							    });

							});
							a.addButton("formulaeditor", {
								title : "formulaeditor",
								cmd : "formulaeditor",
								//label : "公式编辑器"
								image : b + "/img/formulaeditor.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("formulaeditor", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("formulaeditor", tinymce.plugins.formulaeditor)
})();