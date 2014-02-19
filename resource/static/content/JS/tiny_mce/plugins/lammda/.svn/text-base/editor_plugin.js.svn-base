(function() {
	tinymce
			.create(
					"tinymce.plugins.lammda",
					{
						init : function(a, b) {
							a.addCommand("lammda", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`lambda `&nbsp;");
							});
							a.addButton("lammda", {
								title : "lammda",
								cmd : "lammda",
								image : b + "/img/lammda.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("lammda", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("lammda", tinymce.plugins.lammda)
})();