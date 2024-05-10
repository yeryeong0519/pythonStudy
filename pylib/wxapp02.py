import wx

app = wx.App()
frame = wx.Frame(None)
size = wx.Size(600, 400)
frame.SetSieze(size)
pos = wx.Point(100, 100)
frame.setPsition(pos)
color = wx.Colour(0, 0, 255, 0)
frame.SetBackgroundColour(color)
frame.SetTitle("파이썬으로 만든 윈도우")
frame.SetWindowStyle(wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
frame.Show(True)
app.MainLoop