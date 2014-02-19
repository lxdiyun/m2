(function() {
	tinymce
			.create(
					"tinymce.plugins.lim",
					{
						init : function(a, b) {
							a.addCommand("lim", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`lim_(n->oo)`&nbsp;");
							});
							a.addButton("lim", {
								title : "lim",
								cmd : "lim",
								image : b + "/img/lim.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("lim", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("lim", tinymce.plugins.lim)
})();