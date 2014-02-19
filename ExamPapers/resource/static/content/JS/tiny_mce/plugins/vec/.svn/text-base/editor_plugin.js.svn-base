(function() {
	tinymce
			.create(
					"tinymce.plugins.vec",
					{
						init : function(a, b) {
							a.addCommand("vec", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`vec(x)`&nbsp;");
							});
							a.addButton("vec", {
								title : "vec",
								cmd : "vec",
								image : b + "/img/vec.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("vec", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("vec", tinymce.plugins.vec)
})();