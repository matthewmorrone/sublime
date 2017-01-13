import sublime, sublime_plugin

def ReplaceAll(edit, view, exp, tar):
	regions = view.find_all(exp)
	regions.reverse()
	for region in regions:
		view.replace(edit, region, tar)

class StripTagsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()
		ReplaceAll(edit, view, "<\/?.+?>", "")


