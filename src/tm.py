import subprocess
import pytermgui as ptg

BACKEND_PATH = "tm_backend.py"

def close_backend(backend_process):
   # Send close message
   backend_process.stdout.close()
   backend_process.stdin.close()
   backend_process.wait()

def main():

   # Run backend script
   backend_process = subprocess.Popen(['python', BACKEND_PATH], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

   # Test communication channel
   text = backend_process.stdout.readline().decode().strip()

   with ptg.WindowManager() as manager:
      tm = ptg.Window(
         ptg.Label("[100]TM"),
      )

      label = ptg.Label("")
      label.value = text
      tm._add_widget(label)
      
      manager.add(tm)
      manager.run()

   # Close backend
   close_backend(backend_process)

if __name__ == "__main__":
   main()