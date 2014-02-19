(function() {
	tinymce
			.create(
					"tinymce.plugins.gamma",
					{
						init : function(a, b) {
							a.addCommand("gamma", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`gamma`&nbsp;");
							});
							a.addButton("gamma", {
								title : "gamma",
								cmd : "gamma",
								image : b + "/img/gamma.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("gamma", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("gamma", tinymce.plugins.gamma)
})();