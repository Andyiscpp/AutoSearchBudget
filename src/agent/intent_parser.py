# from langchain_openai import ChatOpenAI         # (如果你用的是OpenAI, 注释掉这行)
# from langchain_community.chat_models import ChatZhipuAI # (如果你用的是智谱, 注释掉这行)
from langchain_moonshot.chat_models import ChatOpenAI as ChatMoonshot     # <-- 1. 导入 Kimi (Moonshot)

from langchain_core.runnables import Runnable
from src.agent.prompts import get_intent_parser_prompt
from src.agent.parsers import SearchQueryParser
from src.core.config import settings  # 导入 settings 不变


def get_parsing_chain() -> Runnable:
    """
    构建并返回一个完整的“意图解析链”
    """
    # 获取 Prompt 和 Parser (这部分完全不变)
    prompt, parser = get_intent_parser_prompt()

    # --- 核心修改点 ---
    # 2. 初始化 LLM (替换为 Kimi)
    llm = ChatMoonshot(
        model_name="moonshot-v1-8k",  # Kimi 的模型名称。8k 上下文足够用于意图解析
        # api_key=settings.MOONSHOT_API_KEY,
        #temperature=0.0  # 设为 0.0 或 0.01 来保证结构化输出的稳定性
    )
    # --- 修改结束 ---

    # 3. 构建链 (这部分也完全不变)
    #    这就是 Langchain 的强大之处，无论后端是 OpenAI, Zhipu 还是 Kimi
    #    "链" (Chain) 的定义是完全一致的。
    chain = prompt | llm | parser

    return chain


def parse_user_intent(query: str) -> SearchQueryParser:
    """
    调用链来解析单个用户查询
    (此函数完全不需要修改)
    """
    print(f"--- 正在使用 Kimi 解析意图: '{query}' ---")  # (我只改了打印的文字)
    chain = get_parsing_chain()

    result = chain.invoke({"query": query})
    return result


# --- 用于独立测试此模块 ---
if __name__ == "__main__":
    # (这部分测试代码也完全不需要修改)
    if not settings.MOONSHOT_API_KEY:
        print("错误：MOONSHOT_API_KEY 未配置。请先在 .env 文件中设置它。")
    else:
        test_query = "我想要一个兵棋，预算在叁拾以内，最好是抗美援朝系列，性价比好，不用倒角"
        structured_intent = parse_user_intent(test_query)

        print("\n--- 解析成功 ---")
        print(structured_intent.model_dump_json(indent=2, ensure_ascii=False))