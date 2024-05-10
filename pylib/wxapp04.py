import wx

app = wx.App()

frame = wx.Frame(None,"위젯 테스트")
btn = wx.Button(frame, label="클릭해주세요")
def OnClick(event):
    wx.MessageBox("안녕하세요", "알림", wx.OK)
btn.Bind(wx.EVT_BUTTON, OnClick)
lbl = wx.StaticText(frame, label = "아래 버튼을 눌러보세요")
btn.SetPosition(wx.Point(150, 100))
btn.SetPosition(wx.Point(180, 60))
frame.Show(True)
app.MainLoop()