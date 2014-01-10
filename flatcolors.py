import sublime, sublime_plugin

flatuicolors = {
	"turquoise":     "#1dd2af",
	"green-sea":     "#19b698",
	"emerland":      "#40d47e",
	"nephritis":     "#2cc36b",
	"peter-river":   "#4aa3df",
	"belize-hole":   "#2e8ece",
	"amethyst":      "#a66bbe",
	"wisteria":      "#9b50ba",
	"wet-asphalt":   "#3d566e",
	"midnight-blue": "#354b60",
	"sun-flower":    "#f2ca27",
	"orange":        "#f4a62a",
	"carrot":        "#e98b39",
	"pumpkin":       "#ec5e00",
	"alizarin":      "#ea6153",
	"pomegranate":   "#d14233",
	"clouds":        "#fbfcfc",
	"silver":        "#cbd0d3",
	"concrete":      "#a3b1b2",
	"asbestos":      "#8c9899"
}

class FlatColorsCommand(sublime_plugin.WindowCommand):
	colorList = []
	def __init__(self, *args, **kwargs):
		super(FlatColorsCommand, self).__init__(*args, **kwargs)
		colorList = []
		self.generateColorDialog()

	def run(self):
		self.window.show_quick_panel(self.colorList , self.callback)

	def callback(self, index):
		if (index > -1): # No value is -1
			colorValue = self.colorList[index][1]
			self.window.active_view().run_command("insert_flat_colors", {"value": colorValue})

	def generateColorDialog(self):
		for name, color in flatuicolors.items():
			self.colorList.append([name, color.upper()])


class InsertFlatColorsCommand(sublime_plugin.TextCommand):
	def run(self, edit, value):
		for region in self.view.sel():
			self.view.replace(edit, region, value)


class FlatColorsCompleteCommand(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		if not view.match_selector(locations[0], 'source.css'):
			return []

		return[(str(x),) * 2 for x in flatuicolors]