import wx

app = wx.App()

frame = wx.Frame(None,title = "버튼 배치 테스트")
btn1 = wx.Button(frame, label="첫번째버튼")
btn2 = wx.Button(frame, label="두번째버튼")
btn3 = wx.Button(frame, label="세번째버튼")
box = wx.BoxSizer(box)
box.Add(btn1)
box.Add(btn2)
box.Add(btn3)
frame.Show(True)
app.MainLoop()