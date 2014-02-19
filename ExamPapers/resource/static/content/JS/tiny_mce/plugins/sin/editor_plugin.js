(function() {
	tinymce
			.create(
					"tinymce.plugins.sin",
					{
						init : function(a, b) {
							a.addCommand("sin", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`sin(x)`&nbsp;");
							});
							a.addButton("sin", {
								title : "sin",
								cmd : "sin",
								image : b + "/img/sin.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("sin", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("sin", tinymce.plugins.sin)
})();