from app.chat import HiringChatbot

def test_init():
    bot = HiringChatbot()
    assert bot.model is not None
