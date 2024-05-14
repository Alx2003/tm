from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable
import subprocess
import asyncio
import os

DATA_HEADINGS = [("CPU Utilization:",),]
KEYS = ["cpu_util",]

class TM(App):
   ENABLE_COMMAND_PALETTE = False
   BINDINGS = [("q", "quit", "Quit")]
   header = Header()
   table = DataTable(show_header=False, show_cursor=False)
   footer = Footer()

   # Compile/call the C program
   try:
      os.remove("backend.exe")
      subprocess.run(["gcc", "-o", "backend", "backend.c"])
   except Exception: {}
   process = subprocess.Popen(["./backend"], stdout=subprocess.PIPE, text=True)

   def compose(self) -> ComposeResult:
      yield self.header
      yield self.table
      yield self.footer

   async def on_mount(self) -> None:
      self.table.add_columns(*DATA_HEADINGS[0])
      self.table.add_row("CPU Utilization: Initializing", key="cpu_util")  
      asyncio.create_task(self.update_table())

   async def update_table(self) -> None:
      while(True):
         line = self.process.stdout.readline()
         for row in DATA_HEADINGS:
            self.table.remove_row("cpu_util")
            cpu_util = float(line.strip())
            table_line = [f"{row[0]} {cpu_util}%",]
            self.table.add_row(*table_line, key="cpu_util")
         await asyncio.sleep(1)
               
   async def action_quit(self) -> None:
      self.process.kill()
      self.exit()

def main():
   app = TM()
   app.run()

if __name__ == "__main__":
   main()