(function() {
	tinymce
			.create(
					"tinymce.plugins.log",
					{
						init : function(a, b) {
							a.addCommand("log", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`log(x)`&nbsp;");
							});
							a.addButton("log", {
								title : "log",
								cmd : "log",
								image : b + "/img/log.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("log", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("log", tinymce.plugins.log)
})();