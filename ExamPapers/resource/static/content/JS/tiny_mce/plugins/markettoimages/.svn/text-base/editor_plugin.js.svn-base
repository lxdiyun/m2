(function() {
	tinymce.PluginManager.requireLangPack('markettoimages');
	tinymce.create('tinymce.plugins.MarkettoImagesPlugin', {
		init : function(ed, url) {
			ed.addCommand('markettoImages', function() {
				ed.windowManager.open( {
					file : url + '/dialog.htm',
					width : 882,
					height : 610,
					inline : 1
				}, {
					plugin_url : url
				})
			});
			ed.addButton('markettoimages', {
				title : 'markettoimages.desc',
				cmd : 'markettoImages',
				image : url + '/img/markettoimages.gif'
			});
			ed.onNodeChange.add(function(ed, cm, n) {
				cm.setActive('markettoimages', n.nodeName == 'IMG')
			})
		},
		createControl : function(n, cm) {
			return null
		},
		getInfo : function() {
			return {
				longname : 'Marketto.ru Images Plugin ENG',
				author : 'Viktor Kuzhelny',
				authorurl : 'http://marketto.ru',
				infourl : 'http://marketto.ru',
				version : "1.12"
			}
		}
	});
	tinymce.PluginManager.add('markettoimages',
			tinymce.plugins.MarkettoImagesPlugin)
})();