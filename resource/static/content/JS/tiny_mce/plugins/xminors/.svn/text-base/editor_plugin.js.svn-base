(function() {
	tinymce
			.create(
					"tinymce.plugins.xminors",
					{
						init : function(a, b) {
							a.addCommand("xminors", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`x^(-1)`&nbsp;");
							});
							a.addButton("xminors", {
								title : "",
								cmd : "xminors",
								image : b + "/img/xminors.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("xminors", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null
						}
					});
	tinymce.PluginManager.add("xminors", tinymce.plugins.xminors)
})();