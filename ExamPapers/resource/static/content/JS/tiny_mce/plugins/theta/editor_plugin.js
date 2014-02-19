(function() {
	tinymce
			.create(
					"tinymce.plugins.theta",
					{
						init : function(a, b) {
							a.addCommand("theta", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`theta`&nbsp;");
							});
							a.addButton("theta", {
								title : "theta",
								cmd : "theta",
								image : b + "/img/theta.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("theta", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("theta", tinymce.plugins.theta)
})();