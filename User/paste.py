import sublime, sublime_plugin, re



class NewlineClipboardListener(sublime_plugin.EventListener):
    def on_post_text_command(self, view, name, args):
        if name == 'copy' or name == 'cut':
            sublime.set_clipboard(re.sub(r"\n$", "", sublime.get_clipboard()))
            
