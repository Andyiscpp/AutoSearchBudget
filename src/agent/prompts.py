from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from .parsers import SearchQueryParser  # 从同级目录的 parsers.py 导入


def get_intent_parser_prompt():
    """
    获取用于解析用户意图的 Prompt 模版
    """
    # 1. 实例化一个 Pydantic 解析器
    parser = PydanticOutputParser(pydantic_object=SearchQueryParser)

    # 2. 定义 Prompt 模版
    #    注意 {format_instructions} 和 {query} 这两个占位符
    template = """
    你是一个精通中文的购物意图分析助手。
    你的任务是分析用户的原始查询语句，并将其分解为结构化的数据。

    请严格按照以下格式指令进行输出：
    {format_instructions}

    用户的原始查询语句如下：
    {query}
    """

    # 3. 创建 PromptTemplate
    prompt = PromptTemplate(
        template=template,
        input_variables=["query"],
        # partial_variables (部分变量) 是一个很有用的技巧
        # 它允许我们提前将 'format_instructions' 插入到模版中
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    # 4. 返回 prompt 和 parser，以便后续使用
    return prompt, parser