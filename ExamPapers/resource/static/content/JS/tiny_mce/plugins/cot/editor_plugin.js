(function() {
	tinymce
			.create(
					"tinymce.plugins.cot",
					{
						init : function(a, b) {
							a.addCommand("cot", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`cot(x)`&nbsp;");
							});
							a.addButton("cot", {
								title : "cot",
								cmd : "cot",
								image : b + "/img/cot.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("cot", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("cot", tinymce.plugins.cot)
})();