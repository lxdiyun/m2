(function() {
	tinymce
			.create(
					"tinymce.plugins.xpower2",
					{
						init : function(a, b) {
							a.addCommand("xpower2", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`x^2`&nbsp;");
							});
							a.addButton("xpower2", {
								title : "",
								cmd : "xpower2",
								image : b + "/img/xpower2.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("xpower2", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null
						}
					});
	tinymce.PluginManager.add("xpower2", tinymce.plugins.xpower2)
})();