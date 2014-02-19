(function() {
	tinymce
			.create(
					"tinymce.plugins.cos",
					{
						init : function(a, b) {
							a.addCommand("cos", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`cos(x)`&nbsp;");
							});
							a.addButton("cos", {
								title : "cos",
								cmd : "cos",
								image : b + "/img/cos.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("cos", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("cos", tinymce.plugins.cos)
})();