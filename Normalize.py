import sublime, sublime_plugin

def ReplaceAll(edit, view, exp, tar):
	regions = view.find_all(exp)
	regions.reverse()
	for region in regions:
		view.replace(edit, region, tar)

def Reindent(window):
	window.run_command("select_all")
	window.run_command("reindent")
	window.run_command("save")

class NormalizeParensCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()

		ReplaceAll(edit, view, "\([ \t]+", "(")
		ReplaceAll(edit, view, "[ \t]+\)", ")")

class NormalizeBracketsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()

		ReplaceAll(edit, view, "\[[ \t]+", "[")
		ReplaceAll(edit, view, "[ \t]+]",  "]")

class NormalizeCurliesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()

		ReplaceAll(edit, view, "\{[ \t]+", "{")
		ReplaceAll(edit, view, "[ \t]+\}", "}")

class NormalizeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()

		window.run_command("normalize_parens")
		window.run_command("normalize_brackets")
		window.run_command("normalize_curlies")
		Reindent(window)

