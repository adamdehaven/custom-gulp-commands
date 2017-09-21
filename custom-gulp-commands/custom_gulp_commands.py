import sublime
import sublime_plugin

class GulpDeleteCacheOnKill(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("gulp_kill")
        self.window.run_command("gulp_delete_cache")
