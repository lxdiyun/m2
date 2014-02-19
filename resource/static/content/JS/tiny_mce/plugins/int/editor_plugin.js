(function() {
	tinymce
			.create(
					"tinymce.plugins.int",
					{
						init : function(a, b) {
							a.addCommand("int", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`int_(-x)^(x)`&nbsp;");
							});
							a.addButton("int", {
								title : "int",
								cmd : "int",
								image : b + "/img/int.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("int", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("int", tinymce.plugins.int)
})();