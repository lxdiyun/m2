(function() {
	tinymce
			.create(
					"tinymce.plugins.varphi",
					{
						init : function(a, b) {
							a.addCommand("varphi", function() {
								tinyMCE.activeEditor.execCommand('mceInsertContent', false, "&nbsp;`varphi`&nbsp;");
							});
							a.addButton("varphi", {
								title : "varphi",
								cmd : "varphi",
								image : b + "/img/varphi.gif"
							});
							a.onNodeChange.add(function(d, c, e) {
								c.setActive("varphi", e.nodeName == "IMG")
							})
						},
						createControl : function(b, a) {
							return null;
						}
					});
	tinymce.PluginManager.add("varphi", tinymce.plugins.varphi)
})();