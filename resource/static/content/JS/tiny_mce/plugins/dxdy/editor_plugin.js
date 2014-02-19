(function() {
	tinymce
			.create(
					"tinymce.plugins.dxdy",
					{
						init : function(a, b) {
							a.addCommand("dxdy", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`dx/dy`&nbsp;");
							});
							a.addButton("dxdy", {
								title : "dxdy",
								cmd : "dxdy",
								image : b + "/img/dxdy.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("dxdy", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("dxdy", tinymce.plugins.dxdy)
})();