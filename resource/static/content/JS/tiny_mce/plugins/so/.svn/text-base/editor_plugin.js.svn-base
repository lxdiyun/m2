(function() {
	tinymce
			.create(
					"tinymce.plugins.so",
					{
						init : function(a, b) {
							a.addCommand("so", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;∴&nbsp;");
							});
							a.addButton("so", {
								title : "so",
								cmd : "so",
								image : b + "/img/so.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("so", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("so", tinymce.plugins.so)
})();