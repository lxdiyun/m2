(function() {
	tinymce
			.create(
					"tinymce.plugins.mu",
					{
						init : function(a, b) {
							a.addCommand("mu", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`mu `&nbsp;");
							});
							a.addButton("mu", {
								title : "mu",
								cmd : "mu",
								image : b + "/img/mu.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("mu", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("mu", tinymce.plugins.mu)
})();