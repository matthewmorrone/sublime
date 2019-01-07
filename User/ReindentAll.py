import sublime, sublime_plugin

class ReindentAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("select_all")
		self.view.run_command("reindent")
		self.view.run_command("invert_selection")

