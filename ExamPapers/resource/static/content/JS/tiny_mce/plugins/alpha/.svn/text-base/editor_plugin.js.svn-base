(function() {
	tinymce
			.create(
					"tinymce.plugins.alpha",
					{
						init : function(a, b) {
							a.addCommand("alpha", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`alpha`&nbsp;");
							});
							a.addButton("alpha", {
								title : "alpha",
								cmd : "alpha",
								image : b + "/img/alpha.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("alpha", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("alpha", tinymce.plugins.alpha)
})();