from pydantic import BaseModel,Field,StringConstraints
from typing import Annotated

 # TODO 1: 定义请求模型 EchoRequest
  # 要求:
  # - 字段: text: str
  # - 长度限制: 1~50 (使用 Field)
class EchoRequest(BaseModel):
      text: str = Field(min_length=1,max_length=50)
  # TODO 2: 定义响应模型 EchoResponse
  # 要求:
  # - original: str
  # - normalized: str
  # - length: int
class EchoResponse(BaseModel):
    original: str
    normalized: str
    length: int

class WordCountResponse(BaseModel):
    words: list[str]
    count: int 

class WordCountRequest(BaseModel):
    """ # 写法 A
  text: str = Field(min_length=1)

  # 写法 B
  text: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]

  核心区别：

  - 写法 A：只检查“原始字符串长度 >= 1”
    "   " 长度是 3，所以会通过校验。
  - 写法 B：先 strip() 再做长度检查
    "   " -> ""，长度 0，不通过，返回 422。

  3. 原理与取舍

  - min_length 本身不懂“业务语义”，它只看字符个数。
  - strip_whitespace=True 相当于告诉 Pydantic：先把首尾空白去掉，再按规则校验。
  - 所以当你希望“纯空格不算有效输入”时，B 是更正确的生产默认。
"""
    text:Annotated[str,StringConstraints(strip_whitespace=True,min_length=1)]