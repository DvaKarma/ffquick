import unittest, ffquick as f, io, contextlib
class T(unittest.TestCase):
    def run_(self,a):
        b=io.StringIO()
        with contextlib.redirect_stdout(b): f.main(["--dry"]+a)
        return b.getvalue()
    def test_cortar(self): self.assertIn("-ss 00:00:05 -to 00:00:10",self.run_(["cortar","a.mp4","00:00:05","00:00:10","b.mp4"]))
    def test_gif(self): self.assertIn("fps=12,scale=480:-1",self.run_(["gif","a.mp4","a.gif"]))
unittest.main()
