import sublime, sublime_plugin

class WorkflowCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		window = sublime.active_window()

		# window.run_command("build")
		window.run_command("save")
		window.run_command("view_in_browser")
		window.run_command("browser_refresh", {
			"auto_save": true,
			"delay": 0.0,
			"activate_browser": true,
			"browser_name" : "all"
		})
		# window.run_command("")

