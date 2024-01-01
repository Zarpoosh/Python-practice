# pip install segno

from tkinter import Scale
import segno
qrcode=segno.make_qr("https://github.com/Zarpoosh")
qrcode.save("zarpoosh-github.png" ,scale=5 ,border=1, light="#00a1ff" , dark="232323")