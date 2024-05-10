from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable
import psutil as psu
import asyncio

DATA_HEADINGS = [("CPU Utilization:",),]
KEYS = ["cpu_util",]

class TM(App):
   ENABLE_COMMAND_PALETTE = False
   BINDINGS = [("q", "quit", "Quit")]
   header = Header()
   table = DataTable(show_header=False, show_cursor=False)
   footer = Footer()

   def compose(self) -> ComposeResult:
      yield self.header
      yield self.table
      yield self.footer

   def on_mount(self) -> None:
      self.table.add_columns(*DATA_HEADINGS[0])
      for row in DATA_HEADINGS:
         cpu_util = psu.cpu_percent(interval=1)
         line = [f"{row[0]} {cpu_util}%",]
         self.table.add_row(*line, key="cpu_util")

   #Update polled value

   def action_quit(self) -> None:
      self.exit()

def main():
   app = TM()
   app.run()

if __name__ == "__main__":
   main()