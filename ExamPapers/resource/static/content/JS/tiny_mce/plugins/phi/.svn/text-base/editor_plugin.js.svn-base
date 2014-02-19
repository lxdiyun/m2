(function() {
	tinymce
			.create(
					"tinymce.plugins.phi",
					{
						init : function(a, b) {
							a.addCommand("phi", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`phi`&nbsp;");
							});
							a.addButton("phi", {
								title : "phi",
								cmd : "phi",
								image : b + "/img/phi.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("phi", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("phi", tinymce.plugins.phi)
})();