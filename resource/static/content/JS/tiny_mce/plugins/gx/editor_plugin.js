(function() {
	tinymce
			.create(
					"tinymce.plugins.gx",
					{
						init : function(a, b) {
							a.addCommand("gx", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`g(x)`&nbsp;");
							});
							a.addButton("gx", {
								title : "gx",
								cmd : "gx",
								image : b + "/img/gx.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("gx", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("gx", tinymce.plugins.gx)
})();