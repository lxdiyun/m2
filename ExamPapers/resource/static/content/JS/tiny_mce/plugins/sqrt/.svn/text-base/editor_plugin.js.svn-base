(function() {
	tinymce
			.create(
					"tinymce.plugins.sqrt",
					{
						init : function(a, b) {
							a.addCommand("sqrt", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`sqrt(x)`&nbsp;");
							});
							a.addButton("sqrt", {
								title : "sqrt",
								cmd : "sqrt",
								image : b + "/img/sqrt.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("sqrt", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("sqrt", tinymce.plugins.sqrt)
})();