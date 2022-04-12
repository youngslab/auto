
import win32gui, win32con, win32api, win32process
import pynput


def add(x, y):
  return x + y

def find_window_handle(text):
    return win32gui.FindWindow(None, text)

def bring_window_to_top(hwnd):
  # find a current thread
  curr_tid = win32api.GetCurrentThreadId()

  # find a foreground window's thread
  fore_app = win32gui.GetForegroundWindow()
  fore_tid, fore_pid = win32process.GetWindowThreadProcessId(fore_app)

  # attach
  if fore_tid != curr_tid:
    win32process.AttachThreadInput(curr_tid, fore_tid, True)

  # show and bring to top
  win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
  win32gui.BringWindowToTop(hwnd)

  # detach
  if fore_tid != curr_tid:
    win32process.AttachThreadInput(curr_tid, fore_tid, False)

# x, y points are in application coordiate.
# You can find application coordinate by inspecting event via spy++
def click(hwnd, x, y):
    rect = win32gui.GetWindowRect(hwnd)
    app_x = rect[0]
    app_y = rect[1]

    mouse = pynput.mouse.Controller()    
    mouse.position = (app_x + x, app_y + y)
    mouse.click(pynput.mouse.Button.left, 1)

def type(text):
    # keyboard input
    keyboard = pynput.keyboard.Controller()
    keyboard.type(text)