import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
# 我们假设 .env 文件在 src 目录的上一级 (即项目根目录)
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=env_path)

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    MOONSHOT_API_KEY: str = os.getenv("MOONSHOT_API_KEY")

settings = Settings()

# 检查一下密钥是否加载成功
if not settings.OPENAI_API_KEY:
    print("⚠️ 警告：OPENAI_API_KEY 未设置。请检查你的 .env 文件。")