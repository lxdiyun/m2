(function() {
	tinymce
			.create(
					"tinymce.plugins.sum",
					{
						init : function(a, b) {
							a.addCommand("sum", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`sum_(i->0)^(n)`&nbsp;");
							});
							a.addButton("sum", {
								title : "sum",
								cmd : "sum",
								image : b + "/img/sum.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("sum", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("sum", tinymce.plugins.sum)
})();