from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class TM(App):
   ENABLE_COMMAND_PALETTE = False
   BINDINGS = [("q", "quit", "Quit")]

   def compose(self) -> ComposeResult:
      yield Header()
      yield Footer()

   def action_quit(self) -> None:
      self.exit()

def main():
   app = TM()
   app.run()

if __name__ == "__main__":
   main()