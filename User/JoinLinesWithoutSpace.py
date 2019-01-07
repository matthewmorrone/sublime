import sublime, sublime_plugin


class JoinLinesWithoutSpaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()
		window.run_command("join_lines")




		pt = self.view.sel()[0].begin()
		cprev = view.substr(sublime.Region(pt - 1, pt))
		cnext = view.substr(sublime.Region(pt, pt + 1))



		if cprev == " ":
			window.run_command("left_delete")
		if cnext == " ":
			window.run_command("left_delete")
		# self.window.run_command("")

