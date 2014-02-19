(function() {
	tinymce
			.create(
					"tinymce.plugins.omega",
					{
						init : function(a, b) {
							a.addCommand("omega", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`omega`&nbsp;");
							});
							a.addButton("omega", {
								title : "omega",
								cmd : "omega",
								image : b + "/img/omega.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("omega", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("omega", tinymce.plugins.omega)
})();