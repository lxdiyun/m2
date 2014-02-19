(function() {
	tinymce
			.create(
					"tinymce.plugins.exp",
					{
						init : function(a, b) {
							a.addCommand("exp", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`e^x`&nbsp;");
							});
							a.addButton("exp", {
								title : "exp",
								cmd : "exp",
								image : b + "/img/exp.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("exp", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("exp", tinymce.plugins.exp)
})();