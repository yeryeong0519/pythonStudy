import wx

app = wx.App()

frame = wx.Frame(None, 0, "파이썬으로 만든 윈도우", wx.Point(100, 100), wx.Size(600, 400), wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
color = wx.Colour(0, 0, 255, 0)
frame.SetBackgroundColour(color)
def OnLeftDown(event):
    message = "(%d, %d)를 클릭했습니다 % (event.x, event.y)"

frame.Show(True)
app.MainLoop