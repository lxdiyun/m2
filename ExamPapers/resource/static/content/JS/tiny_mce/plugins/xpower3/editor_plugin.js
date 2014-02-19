(function() {
	tinymce
			.create(
					"tinymce.plugins.xpower3",
					{
						init : function(a, b) {
							a.addCommand("xpower3", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`x^3`&nbsp;");
							});
							a.addButton("xpower3", {
								title : "",
								cmd : "xpower3",
								image : b + "/img/xpower3.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("xpower3", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null
						}
					});
	tinymce.PluginManager.add("xpower3", tinymce.plugins.xpower3)
})();