

import sublime, sublime_plugin

class SetScratchCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()

		view.set_scratch(True)

		# window.run_command("")
		# window.run_command("", {"": "", "": 0})

		# brackets = reversed(view.find_all("{\n"))
		# for region in brackets:
			# view.replace(edit, region, "\n{\n")
