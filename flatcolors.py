import sublime, sublime_plugin

flatuicolors = {
    "turquoise":     "#1DD2AF",
    "green-sea":     "#19B698",
    "emerland":      "#40D47E",
    "nephritis":     "#2CC36B",
    "peter-river":   "#4AA3DF",
    "belize-hole":   "#2E8ECE",
    "amethyst":      "#A66BBE",
    "wisteria":      "#9B50BA",
    "wet-asphalt":   "#3D566E",
    "midnight-blue": "#354B60",
    "sun-flower":    "#F2CA27",
    "orange":        "#F4A62A",
    "carrot":        "#E98B39",
    "pumpkin":       "#EC5E00",
    "alizarin":      "#EA6153",
    "pomegranate":   "#D14233",
    "clouds":        "#FBFCFC",
    "silver":        "#CBD0D3",
    "concrete":      "#A3B1B2",
    "asbestos":      "#8C9899"
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
            self.colorList.append([name.title(), color.upper()])


class InsertFlatColorsCommand(sublime_plugin.TextCommand):
    def run(self, edit, value):
        for region in self.view.sel():
            self.view.replace(edit, region, value)


class FlatColorsCompleteCommand(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], 'source.css, source.stylus, source.sass, source.scss, source.postcss'):
            return []

        return[(name + '\t' + hex, hex) for name, hex in flatuicolors.items()]