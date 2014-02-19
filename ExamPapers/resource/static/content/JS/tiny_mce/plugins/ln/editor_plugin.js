(function() {
	tinymce
			.create(
					"tinymce.plugins.ln",
					{
						init : function(a, b) {
							a.addCommand("ln", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`ln(x)`&nbsp;");
							});
							a.addButton("ln", {
								title : "ln",
								cmd : "ln",
								image : b + "/img/ln.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("ln", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("ln", tinymce.plugins.ln)
})();