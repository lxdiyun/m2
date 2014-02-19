(function() {
	tinymce
			.create(
					"tinymce.plugins.bec",
					{
						init : function(a, b) {
							a.addCommand("bec", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;∵&nbsp;");
							});
							a.addButton("bec", {
								title : "bec",
								cmd : "bec",
								image : b + "/img/bec.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("bec", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("bec", tinymce.plugins.bec)
})();