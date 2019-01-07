import sublime, sublime_plugin

# self.window.run_command("")

# Multi line find is there, but '.' doesn't match newline characters by default.
# You can either do (.|\n) or prefix the expression with (?s)

def ReplaceAll(edit, view, exp, tar):
	# regions = reversed(view.find_all(exp))
	regions = view.find_all(exp)
	regions.reverse()

	# edit = view.begin_edit()
	for region in regions:
		view.replace(edit, region, tar)
	# view.end_edit(edit)

class RemoveLinebreaksCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()
		ReplaceAll(edit, view, "\n+", "\n")
		ReplaceAll(edit, view, "^\n", "")
		# window.run_command("save")

class RemoveSomeLinebreaksCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()
		ReplaceAll(edit, view, "\n\n+", "\n\n")
		# window.run_command("save")
