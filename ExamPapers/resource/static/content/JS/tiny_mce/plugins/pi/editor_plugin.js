(function() {
	tinymce
			.create(
					"tinymce.plugins.pi",
					{
						init : function(a, b) {
							a.addCommand("pi", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`pi`&nbsp;");
							});
							a.addButton("pi", {
								title : "pi",
								cmd : "pi",
								image : b + "/img/pi.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("pi", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("pi", tinymce.plugins.pi)
})();