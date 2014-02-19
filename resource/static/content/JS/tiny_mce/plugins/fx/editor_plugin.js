(function() {
	tinymce
			.create(
					"tinymce.plugins.fx",
					{
						init : function(a, b) {
							a.addCommand("fx", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`f(x)`&nbsp;");
							});
							a.addButton("fx", {
								title : "fx",
								cmd : "fx",
								image : b + "/img/fx.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("fx", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("fx", tinymce.plugins.fx)
})();