(function() {
	tinymce
			.create(
					"tinymce.plugins.frac",
					{
						init : function(a, b) {
							a.addCommand("frac", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`x/y`&nbsp;");
							});
							a.addButton("frac", {
								title : "frac",
								cmd : "frac",
								image : b + "/img/frac.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("frac", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("frac", tinymce.plugins.frac)
})();