import sys
import logging

logging.basicConfig(format='[%(asctime)s - %(pathname)s - %(levelname)s] %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOG = logging.getLogger(__name__)

def get_formatted_chats(chats, app):
    formatted_chats = []
    LOG.info("get_formatted_chatss")
    LOG.info(chats)
    LOG.info(app)
    for chat in chats:
      LOG.info("get_formatted_chats for") 
      try:
        if isInt(chat):
          LOG.info("get_formatted_chats if")
          formatted_chats.append(int(chat))
        elif chat.startswith("@"):
          LOG.info("get_formatted_chats elif")
          formatted_chats.append(app.get_chat(chat.replace("@", "")).id)
        elif chat.startswith("https://t.me/c/") or chat.startswith("https://telegram.org/c/") or chat.startswith("https://telegram.dog/c/"):
          LOG.info("get_formatted_chats elif2") 
          chat_id = chat.split("/")[4]
          if isInt(chat_id):
            chat_id = "-100" + str(chat_id)
            chat_id = int(chat_id)
          else:
            chat_id = app.get_chat(chat_id).id
          formatted_chats.append(chat_id)
      except Exception as e:
        LOG.error(e)
        sys.exit(1)
    return formatted_chats

def get_formatted_chat(chat, app):
    LOG.info("get_formatted_chat")
    LOG.info(chats)
    LOG.info(app)
    try:
      if isInt(chat):
        LOG.info("get_formatted_chat if")
        return int(chat)
      elif chat.startswith("@"):
        return app.get_chat(chat.replace("@", "")).id
      elif chat.startswith("https://t.me/c/") or chat.startswith("https://telegram.org/c/") or chat.startswith("https://telegram.dog/c/"):
        chat_id = chat.split("/")[4]
        if isInt(chat):
          chat_id = "-100" + str(chat_id)
          chat_id = int(chat_id)
        else:
          chat_id = app.get_chat(chat_id).id
        return chat_id
      else:
        return None
    except Exception as e:
      return None

def isInt(value):
  try:
    int(value)
    return True
  except ValueError:
    return False
