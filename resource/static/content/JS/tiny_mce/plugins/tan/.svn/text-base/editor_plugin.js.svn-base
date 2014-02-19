(function() {
	tinymce
			.create(
					"tinymce.plugins.tan",
					{
						init : function(a, b) {
							a.addCommand("tan", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`tan(x)`&nbsp;");
							});
							a.addButton("tan", {
								title : "tan",
								cmd : "tan",
								image : b + "/img/tan.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("tan", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("tan", tinymce.plugins.tan)
})();