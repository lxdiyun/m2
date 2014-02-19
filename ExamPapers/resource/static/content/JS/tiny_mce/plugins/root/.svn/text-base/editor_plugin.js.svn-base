(function() {
	tinymce
			.create(
					"tinymce.plugins.root",
					{
						init : function(a, b) {
							a.addCommand("root", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`rootn(x)`&nbsp;");
							});
							a.addButton("root", {
								title : "root",
								cmd : "root",
								image : b + "/img/rootn.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("root", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("root", tinymce.plugins.root)
})();