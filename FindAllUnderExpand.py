import sublime, sublime_plugin

class FindAllUnderExpandCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()
		window.run_command("expand_selection")
		window.run_command("find_all_under")

# class FindAllUnderExpandCommand(sublime_plugin.WindowCommand):
# 	def run(self):
# 		self.window.run_command("expand_selection")
# 		self.window.run_command("find_all_under")
