from ETS2LA.Plugin import *
from ETS2LA.UI import *

"""
This is an example plugin file for the new ETS2LA plugin system.
You can use this as a template for your own plugins.
"""

class Settings(ETS2LASettingsMenu):
    dynamic = False # False means that the page is built once and then cached. True means that the page is rebuilt every time the frontend asks for an update.
    # NOTE: True is not yet implemented!
    def render(self):
        Title("Plugin Settings")
        Description("This is a demo settings page for you to edit.")
        Button("This will call a function", Plugin.imports)
        
        with TabView():
            for i in range(3):
                with Tab(name=f"Tab {i+1}"):
                    with Group():
                        Input("Input", f"input_{i}", "string", default=f"default {i}", description=f"This is an input field {i}")
                        Button(f"Button {i}", Plugin.imports)
        
        return RenderUI()

class Plugin(ETS2LAPlugin):
    description = PluginDescription(
        name="TestPlugin",
        version="1.0",
        description="A test plugin",
        dependencies=[],
        compatible_os=["Windows", "Linux"],
        compatible_game=["ETS2", "ATS"],
        update_log={
            "0.1": "Initial release",
            "0.2": "Fixed some bugs",
            "1.0": "Added some features"
        }
    )

    author = Author(
        name="Tumppi066",
        url="https://github.com/Tumppi066"
    )
    
    settings_menu = Settings()
    
    def imports(self):
        """
        You should place all your (non ETS2LA) imports in this function. This is because during startup, 
        python has to read this file to get the information about the plugin.
        If you place large imports like torch outside of this function, it will drastically slow down 
        the entire startup process.

        NOTE: Some IDEs might not recognize imports here... so use vscode :)
        (looking at you PyCharm)
        """
        global json
        import json
    
    def run(self):
        #print(json.dumps(self.settings_menu.build(), indent=4))
        ...