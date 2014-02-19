(function() {
	tinymce
			.create(
					"tinymce.plugins.rho",
					{
						init : function(a, b) {
							a.addCommand("rho", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`rho`&nbsp;");
							});
							a.addButton("rho", {
								title : "rho",
								cmd : "rho",
								image : b + "/img/rho.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("rho", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("rho", tinymce.plugins.rho)
})();