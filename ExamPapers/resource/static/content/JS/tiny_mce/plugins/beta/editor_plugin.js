(function() {
	tinymce
			.create(
					"tinymce.plugins.beta",
					{
						init : function(a, b) {
							a.addCommand("beta", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`beta`&nbsp;");
							});
							a.addButton("beta", {
								title : "beta",
								cmd : "beta",
								image : b + "/img/beta.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("beta", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("beta", tinymce.plugins.beta)
})();